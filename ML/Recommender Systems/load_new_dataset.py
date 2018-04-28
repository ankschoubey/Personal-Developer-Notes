import pandas as pd
# coding: latin1

set_categories = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama',
                  'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War',
                  'Western', '(no genres listed)']


def get_matrix(raw_category):
    this_movie_category = []
    #print(raw_category)
    for i in set_categories:
        if i in raw_category:
            this_movie_category.append(1)
        else:
            this_movie_category.append(0)
    return this_movie_category

def seperate_movie_name_and_year(raw):
    raw= ','.join(raw)
    temp = raw.split('(')
    if len(temp[-1])!= 5 or len(temp)==1:
        return [raw, '']
    print(temp)

    return [''.join(temp[:-1]), int(temp[-1].replace(')',''))]

table = []
with open('/Users/ankushchoubey/Downloads/ml-latest-small/movies.csv') as file:
    count = 0;
    for i in file.readlines()[1:]:
        split = i.split(',')
        #print(split)
        final = [count,int(split[0])]#+seperate_movie_name_and_year(split[1:-1])+get_matrix(split[-1])
        table.append(final)
        count+=1

names = ['our_id','movielens_id']#['id','title','year']+set_categories

df = pd.DataFrame(table, columns=names)
print(df)

import sqlalchemy

class Database:
    def __init__(self, user='root', password='MyNewPass',localhost='127.0.0.1',port='8889', database='movielens'):
        self.engine = sqlalchemy.create_engine('mysql+mysqldb://'+user+':'+password+'@'+localhost+':'+port+'/'+database+'?charset=utf8mb4')

    def get(self, table, columns = ['*'],where = ''):
        return  pd.read_sql('SELECT ' + ','.join(columns) + ' FROM '+table, self.engine)

    def save_entire_df(self, frame, table_name, already_exists = 'replace'):
        frame.to_sql(table_name, self.engine, if_exists=already_exists)

db = Database()

db.save_entire_df(df,'movies_id_mapper')
