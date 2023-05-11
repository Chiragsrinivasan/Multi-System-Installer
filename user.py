import sqlite3

# create a connection to the database
conn = sqlite3.connect("software.db")

# create a cursor object to execute SQL statements
cursor = conn.cursor()
sql='''CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host VARCHAR(255) NOT NULL,
    port int,
    username varchar(40),
    password VARCHAR(50) NOT NULL,
    path VARCHAR(100) NOT NULL
);'''
# create a table
cursor.execute(sql)

cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (1,'169.254.170.114',22,'ubuntu','ubuntu@1','/home/ubuntu'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (2,'169.322.121.212',22,'reshma01','reshma','Reshmakka'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (3,'192.168.0.106',22,'sumukha0','2416109','/home/sumukha0'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (4,'192.168.0.107',22,'sumukha1','2416109','/home/sumukha1'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (5,'169.254.170.114',22,'chirag','chirag01','chirag1'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (6,'192.168.02.106',22,'amogh','passwordword','amogh'))
# commit the changes to the database
conn.commit()

# close the connection
conn.close()