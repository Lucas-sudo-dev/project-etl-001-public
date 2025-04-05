import pandas as pd

class Transform:

    def __init__(self):
        self.dataframe = None


    def transform_columns(self, dataframe, convert:str):
        '''
        Método criado para padronizar o nome das colunas

        Retorna um data frame pandas
        '''
        self.dataframe = dataframe

        list_columns = list(self.dataframe.columns)

        if convert.lower() == "upper":
            new_list = [name.replace(")", "").replace("(", "").replace("_%", "").upper() for name in list_columns]

        elif convert.lower() == "lower":
            new_list = [name.replace(")", "").replace("(", "").replace("_%", "").lower() for name in list_columns]

        keys = list_columns
        values = new_list
        new_dictionary = {}

        for i in range(len(keys)):
            new_dictionary[keys[i]] = values[i]
        
        dataframe_renamed = self.dataframe.rename(columns=new_dictionary)
        return dataframe_renamed