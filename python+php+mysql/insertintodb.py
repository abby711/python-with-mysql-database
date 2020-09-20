import pymysql
def loadowners(cursor):
    ownersdata=open("docu1.txt")
    for rowline in ownersdata:
        row=rowline.split(",")
        sql= "INSERT INTO owners(name,phone) VALUES('{}','{}');".format(row[0],row[1])
        cursor.execute(sql)
    cursor.execute("SELECT * from owners;")
    print(cursor.fetchall())

def loadpets(cursor):
    petsdata=open("docu2.txt")
    for rowline in petsdata:
        row=rowline.split(",")
        sql="INSERT INTO pets(ownerid,name,gender,species,color,age) VALUES((SELECT id FROM owners WHERE name='{0}'),'{1}','{2}','{3}','{4}','{5}');".format(*row)
        cursor.execute(sql)
    
if __name__=="__main__":
    db=pymysql.connect(host="localhost",user="root1",passwd="root1",db="database1")
    cursor=db.cursor()
    loadowners(cursor)
    loadpets(cursor)
    db.commit()
    db.close()  
