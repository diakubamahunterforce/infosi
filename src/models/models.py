import  sqlite3 as  Sq

import  os

class  db_query():
    def __iter__(self) :
        pass
    @classmethod
    def insert_values(cls , links, discricao):
       
            sql = sql = f"INSERT INTO  registro (links, discricao ) VALUES ('{links}','{discricao}');"
            database = Sq.connect('DB.db')
           
       



       
            cursor = database.execute(sql)
            database.commit()

            print(f"{cursor.rowcount} registro(s) inserido(s).")
            database.close()

            return 'registrado'

       
    @classmethod
    def search_data(cls, links) :

        database = Sq.connect('DB.db')
        sql=f"SELECT  links ,discricao FROM registro  WHERE links=='{links}'"
        cursor=database.cursor()
        cursor.execute(sql)
        dados=cursor.fetchall()
        database.close()
        if dados==[]:
             return []
        else:
          return  dados[0][1]
    


#db_query.insert_values('test1','test0')














