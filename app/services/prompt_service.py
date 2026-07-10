class PromptService:

    def build_sql_prompt(
        self,
        table_name: str,
        schema: list,
        question: str
    ):

        schema_text = ""

        for column in schema:

            schema_text += (
                f"- {column['column_name']} "
                f"({column['data_type']})\n"
            )

        prompt = f"""
You are an expert SQLite SQL Generator.

Database Table:
{table_name}

Columns:
{schema_text}

User Question:
{question}

Rules:
1. Generate ONLY valid SQLite SQL.
2. Do not explain the SQL.
3. Do not use Markdown.
4. Return only the SQL statement.
"""

        return prompt