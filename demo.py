import mysql.connector

""" mydb = mysql.connector.connect(     #----------- showing all DB -----------------
    user='root',
    password='123456',
    host='localhost',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("Show databases;")
for i in mycursor: 
    print(i) """



""" mydb = mysql.connector.connect(    #----------- showing particular Table Content from a particular DB -----------------
    user='root',
    password='123456',
    host='localhost',
    auth_plugin='mysql_native_password',
    database = "swastik"    #----- name of DB --------------
)

mycursor = mydb.cursor() 

mycursor.execute("select * from students;")   #--------------- name of Table inside DB -------------------
for i in mycursor: 
    print(i) """




mydb = mysql.connector.connect(    
    user='root',
    password='123456',
    host='localhost',
    auth_plugin='mysql_native_password',
    database = "swastik"    #----- name of DB --------------
)

mycursor = mydb.cursor() 

mycursor.execute("insert into students values(2, 'SWAS');")   #--------------- name of Table inside DB -------------------
mycursor.execute("select * from students;") 

result = mycursor.fetchall()

#result = mycursor.fetchone()      #only to fetch the first item

for i in result: 
    print(i)
