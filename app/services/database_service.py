from unittest import result

from sqlalchemy.orm import Session
from sqlalchemy import text


class DatabaseService:

    def __init__(self, db: Session):
        self.db = db
    
    
    def list_tables(self):
        query = text(
        "SELECT name FROM sqlite_master WHERE type='table';"
        )
        result = self.db.execute(query)

        tables = result.fetchall()

        return [table[0] for table in tables]
    
    def get_table_schema(self, table_name: str):

        query = text(
            f"PRAGMA table_info({table_name});"
        )

        result = self.db.execute(query)

        rows = result.fetchall()

        schema = []

        for row in rows:

            schema.append(
                {
                    "column_name": row[1],
                    "data_type": row[2],
                    "primary_key": bool(row[5])
                }
            )

        return schema
    
    def execute_query(self, sql: str):
        result = self.db.execute(text(sql))
        columns = result.keys()
        rows = result.fetchall()
        data = []
        for row in rows:
            data.append(dict(zip(columns, row)))
        return data