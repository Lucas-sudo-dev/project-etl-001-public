import os
from sqlalchemy import create_engine

class Load:

    def __init__(self):
        self.dataframe =  None
        self.table = None
        self.database = os.getenv("DATABASE")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")

    
    def load_database_pandas(self, dataframe, table:str):

        self.dataframe = dataframe
        self.table = table

        engine = create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}")
        
        try:
            self.dataframe.to_sql(name=self.table, con=engine, if_exists='append', index=False)
            message = f"Dados inseridos com sucesso na tabela '{self.table}'!"
        
        except Exception as e:
            message = "Ocorreu um erro ao inserir os dados:", e
            pass
        return message
