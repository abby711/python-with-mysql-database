import pymysql
html=""
def headhtml(html):
    html+="<html><head><title>OWNERS OF PETS</title></head><body>"
    return html
def foothtml(html):
    html+="<</body></html>"  
    return(html)

def ownerquery():
    print("start")
    db=pymysql.connect(host="localhost",user="root1",passwd="root1",db="database1")  
    cursor=db.cursor()
    sql="SELECT * FROM owners;"
    cursor.execute(sql)
    owners=cursor.fetchall()
    sql="SELECT column_name from information_schema.COLUMNS where TABLE_NAME='owners';"
    cursor.execute(sql)
    columns=cursor.fetchall()
    print(columns)
    return(owners,columns)
def ownertable(owners_list,column_names,ht):
    ht+="<table border='2'>"
    ht+="<tr>"
    i=0
    for name in column_names:
        ht+="<th>"+name[0]+"</th>"
        i+=1
    ht+="</tr>"
    for owner in owners_list:
        ht+="<tr>"
        r=0
        while r<i:
            ht+="<td>{0}</td>".format(owner[r]) 
            r+=1
        ht+="</tr>"
    ht+="</table>"
    return(ht)

def petquery():
    
    db=pymysql.connect(host="localhost",user="root1",passwd="root1",db="database1")  
    cursor=db.cursor()
    sql="SELECT * FROM pets;"
    cursor.execute(sql)
    pets=cursor.fetchall()
    sql="SELECT column_name from information_schema.COLUMNS where TABLE_NAME='pets';"
    cursor.execute(sql)
    columns=cursor.fetchall()
    return(pets,columns)

def petstable(pets_list,column_names,ht):
    ht+="<table border='2'>"
    ht+="<tr>"
    i=0
    for name in column_names:
        ht+="<th>"+name[0]+"</th>"
        i+=1
    ht+="</tr>"
    for pet in pets_list:
        ht+="<tr>"
        r=0
        while r<i:
            ht+="<td>{0}</td>".format(pet[r]) 
            r+=1
        ht+="</tr>"
    ht+="</table>"
    return(ht)

if __name__=="__main__":
    html=headhtml(html)
    (owners,headers)=ownerquery()
    html=ownertable(owners,headers,html)
    (pets,headers)=petquery()
    html=petstable(pets,headers,html)
    html=foothtml(html)

    outf=open("rendering.html","w")
    outf.write(html)
    outf.close()



