from urllib import request
from wsgiref.validate import validator

from click import prompt
from fastapi import FastAPI, Depends
from app.services import database_service, prompt_service
from app.services.ollama_service import OllamaService
from app.models.schemas import QuestionRequest, QuestionResponse
from app.database.database import Base, engine, get_db
from app.models.chat_history import ChatHistory
from sqlalchemy.orm import Session
from app.services.database_service import DatabaseService
from app.services.prompt_service import PromptService
from app.services.sql_validator import SQLValidator

ollama_service = OllamaService()
app = FastAPI()
#creates the database tables if they don't exist
#metadata is a collection of Table objects and their associated schema constructs. The create_all() method generates the necessary SQL statements to create the tables in the database based on the defined models.
Base.metadata.create_all(bind=engine)  

@app.post("/ask")
def ask(request: QuestionRequest, db: Session = Depends(get_db)):

    answer = ollama_service.generate_response(
        request.question
    )
    

    new_chat_entry = ChatHistory(
        question=request.question,
        answer=answer
    )

    db.add(new_chat_entry)

    db.commit()

    return QuestionResponse(
        question=request.question,
        answer=answer
    )

@app.get("/")
def read_root():
    return {"message": "hello World"}


@app.get("/tables")
def get_tables(db: Session = Depends(get_db)):

    database_service = DatabaseService(db)

    tables = database_service.list_tables()

    return tables

@app.get("/schema/{table_name}")
def get_schema(
    table_name: str,
    db: Session = Depends(get_db)
    ):

        database_service = DatabaseService(db)

        schema = database_service.get_table_schema(table_name)

        return schema



@app.post("/generate-sql")
def generate_sql(request:QuestionRequest, db: Session = Depends(get_db)):
    database_service = DatabaseService(db)
    schema = database_service.get_table_schema("chat_history")
    
    prompt_service = PromptService()

    prompt = prompt_service.build_sql_prompt(
    table_name="chat_history",
    schema=schema,
    question=request.question
    )

    sql = ollama_service.generate_response(prompt)

    validator = SQLValidator()

    if validator.validate(sql):
        results = database_service.execute_query(sql)
        return {
        "generated_sql": sql,
        "results": results
        }

    return {
    "error": "Unsafe SQL detected.",
    "generated_sql": sql
    }