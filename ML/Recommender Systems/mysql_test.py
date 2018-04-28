import MySQLdb
import pandas as pd
import numpy as np
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqldb://root:MyNewPass@127.0.0.1:8889/movielens')

"""db = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                     passwd="MyNewPass",
                     db="movielens",
                    port = 8889)
"""
#cur = db.cursor()
#cur.execute("SELECT * FROM examples")
output = pd.read_sql("SELECT * FROM examples", engine)
print(output)

# print the first and second columns
#for row in cur.fetchall():
#  print(row)

#cur.execute("""ALTER TABLE examples
#ADD COLUMN vendor_group INT NOT NULL;""")

table1 = pd.DataFrame(np.random.rand(10,20));
#print(table1)
table1.to_sql('random_numbers', engine,if_exists="replace");
