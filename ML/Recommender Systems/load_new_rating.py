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

#/Users/ankushchoubey/Downloads/ml-latest/ratings.csv
def load_movie_lens(location, override = True):

    file = np.genfromtxt(location, delimiter=',')

    row = file[:,0]-1
    all_elements = set(row)
    print(all_elements)
    complete = []
    count = 0
    for i in list(all_elements):
        complete.append([count,i])
    return pd.DataFrame(complete, columns=['our_id','movielens_id'])
    #col = file[:,1]-1
    #rating = file[:,2]

    #matrix = sparse.csr_matrix((rating, (row, col)))
    #matrix = pd.DataFrame(matrix.toarray())

    #return matrix

a = load_movie_lens('/Users/ankushchoubey/Downloads/ml-latest-small/ratings.csv')
db.save_entire_df(pd.read_csv(a), 'user_id_mapper')
