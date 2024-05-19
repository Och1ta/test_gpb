import requests
from datetime import datetime
import pandas as pd
from pydantic import BaseModel, ValidationError, field_validator
from typing import List, Any


class RowModel(BaseModel):
    key1: int
    key2: datetime
    key3: str


class APIResponseModel(BaseModel):
    Columns: List[str]
    Description: str
    RowCount: int
    Rows: List[List[Any]]

    @field_validator('Rows')
    def validate_rows(cls, v):
        for row in v:
            RowModel(key1=row[0], key2=row[1], key3=row[2])
        return v


def fetch_data():
    url = "https://api.gazprombank.ru/very/important/docs"
    params = {
        "documents_date": int(datetime.combine(datetime.today(), datetime.min.time()).timestamp())
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


data = fetch_data()

if data:
    try:
        validated_data = APIResponseModel(**data)
    except ValidationError as e:
        print(e.json())
        exit(1)

    columns = validated_data.Columns
    rows = validated_data.Rows

    df = pd.DataFrame(rows, columns=columns)

    df.rename(columns={
        "key1": "document_id",
        "key2": "document_dt",
        "key3": "document_name"
    }, inplace=True)

    df['load_dt'] = datetime.now()

    print(df)
else:
    print("Failed to fetch data from the API.")
