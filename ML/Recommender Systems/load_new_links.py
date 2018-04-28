import sqlalchemy
import pandas as pd
from scipy import sparse
import numpy as np
class Database:
    def __init__(self, user='root', password='MyNewPass',localhost='127.0.0.1',port='8889', database='movielens'):
        self.engine = sqlalchemy.create_engine('mysql+mysqldb://'+user+':'+password+'@'+localhost+':'+port+'/'+database+'?charset=utf8mb4')

    def get(self, table, columns = ['*'],where = ''):
        return  pd.read_sql('SELECT ' + ','.join(columns) + ' FROM '+table, self.engine)

    def save_entire_df(self, frame, table_name, already_exists = 'replace'):
        frame.to_sql(table_name, self.engine, if_exists=already_exists)

db = Database()

#/Users/ankushchoubey/Downloads/ml-latest/links.csv
a = pd.read_csv('/Users/ankushchoubey/Downloads/ml-latest/links.csv')

db.save_entire_df(a, 'links')
