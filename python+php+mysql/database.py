import pymysql
server=pymysql.connect(host="localhost",user="root1",passwd="root1")
cursor=server.cursor()
sql="CREATE DATABASE IF NOT EXISTS database1;"
cursor.execute(sql)
sql="USE database1;"
cursor.execute(sql)
# sql='''CREATE TABLE IF NOT EXISTS owners(id integer NOT NULL AUTO_INCREMENT,
#                                           name varchar(20) NOT NULL,
#                                           phone varchar(10),
#                                           PRIMARY KEY (id));'''
# cursor.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS pets (petid integer NOT NULL AUTO_INCREMENT,
                                       ownerid integer,
                                       gender varchar(20),
                                       species varchar(10),
                                       color varchar(10),
                                       age integer,
                                       PRIMARY KEY (petid) ,
                                       FOREIGN KEY(ownerid) REFERENCES owners(id));'''
cursor.execute(sql)
sql="SHOW tables;"  
cursor.execute(sql)
print(cursor.fetchall())                                        
