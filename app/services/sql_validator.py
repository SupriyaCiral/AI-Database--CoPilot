class SQLValidator:

    def validate(self, sql: str):

        sql = sql.strip().upper()

        return sql.startswith("SELECT")