import pandas as pd

class Extract:

    def __init__(self):
        self.file_source = None
        self.file_name = None


    def extract_csv(self, file_source:str, file_name:str, file_encoding:str):
        '''
        Método criando para extrair arquivos do tipo csv

        Retorna um data frame pandas
        '''
        if file_encoding is None:
            file_encoding = "UTF-8"

        self.file_source = file_source
        self.file_name = file_name
        
        data_frame_extract_csv = pd.read_csv('{0}/{1}'.format(self.file_source, self.file_name), encoding=file_encoding)
        
        return data_frame_extract_csv
    
    @property
    def get_file_source(self):
        return self.file_source