import pymysql
class datab():
    def __init__ (self,databaseName,servername,username,password):
        self.n=databaseName
        db=pymysql.connect(host=servername,user=username,passwd=password)
        cursor=db.cursor()
        self.cursor=cursor
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(self.n))
        cursor.execute("use {};".format(self.n))

    def addtable(self,tableName,**columns):
        sql="CREATE TABLE IF NOT EXISTS "+tableName+"( "
        for c,t in columns.items():
            sql+="%s %s, " % (c,t)
        sql=sql[:-2]+");"
        self.cursor.execute(sql)

    def addelement(self,tableName,**values):
        sql="INSERT INTO "+tableName+" ( " 
        columns=[]
        value=[]
        for k,v in values.items():
            columns.append(k)
            value.append(v)
        for i in columns:
            sql+="%s, " % i
        sql=sql[:-2]+") VALUES ("
        for v in value:
            sql+=" '%s', " % v
        sql=sql[:-2]+");"
        self.cursor.execute(sql) 

    def viewtable(self,tableName):
        self.cursor.execute("SELECT * from %s" % tableName)
        print(self.cursor.fetchall())  


newdb=datab("database1","localhost","root1","root1")
#newdb.addtable("newtable",rollno="int NOT NULL AUTO_INCREMENT PRIMARY KEY",name="varchar(20)",dept="varchar(10)")
newdb.addelement("newtable",name="abirami",dept="it")
newdb.addelement("newtable",name="kundana",dept="cse")
newdb.addelement("newtable",name="dharini",dept="ece")
newdb.viewtable("newtable")

