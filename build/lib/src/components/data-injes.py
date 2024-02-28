import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation


## Initialize data ingetion Configuration

@dataclass
class DataInjestionconfig:
    tain_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## Creat a class for data injestion
    
class DataInjestion:
    def __init__(self):
        self.injestionconfig=DataInjestionconfig()

    def initiate_data_injeston(self):
        logging.info('Data injestion method starts')
        try:
            df=pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
        
            logging.info('Dataset read as pandas dataframe')

            os.makedirs(os.path.dirname(self.injestionconfig.raw_data_path),exist_ok=True)
            df.to_csv(self.injestionconfig.raw_data_path,index=False)
            
            logging.info('tarin test split')

            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.injestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestionconfig.test_data_path,index=False,header=True)

            logging.info('Data injestion completed')

            return(
                self.injestionconfig.tain_data_path,
                self.injestionconfig.test_data_path
            )


        except Exception as e:
            logging.info('Exception occrred at adata injestion stage ')
            raise CustomException(e,sys)
        
        




