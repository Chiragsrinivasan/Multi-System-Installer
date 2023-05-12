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
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (2,'192.168.251.218',22,'reshmar','pass1234word','/home/reshmar'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (3,'192.168.0.106',22,'sumukha0','2416109','/home/sumukha0'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (4,'192.168.0.107',22,'sumukha1','2416109','/home/sumukha1'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (5,'169.254.170.114',22,'chirag','chirag01','chirag1'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (6,'192.168.02.106',22,'amogh','passwordword','amogh'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (7,'10.60.210.124',22,'ml20\student','student','amogh'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (8,'10.60.210.130',22,'ml23\student','student','amogh'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (9,'10.60.223.113',22,'ml1\student','student','amogh'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (10,'10.60.210.151',22,'ml13\student','student','amogh'))
cursor.execute("insert into user (id,host,port,username,password,path)  values(?, ?, ?, ?, ?, ?)", (11,'10.60.210.127',22,'ml21\student','student','amogh'))
# commit the changes to the database
conn.commit()

# close the connection
conn.close()