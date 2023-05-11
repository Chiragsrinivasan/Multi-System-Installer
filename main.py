import getpass
import paramiko
from scp import SCPClient
import os
import mysql.connector
import sqlite3

def accessdata():
    sqliteConnection = sqlite3.connect("software.db")
    cursor = sqliteConnection.cursor()
    a = []
    d = {}
    for row in cursor.execute('SELECT * FROM user;'):
        a.append(row)
    print(a)
    d = {}
    for i in a:
        d[i[0]] = i[1]
    return (d)

def dbcon():
    conn = sqlite3.connect("software.db")
    return conn

def user(conn):
    cursor = conn.cursor()
    query = "SELECT username FROM user"
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result[0])
    user1 = input("Enter the username: ")
    sql = "SELECT host, port, username, password, path FROM user WHERE username = ?"
    cursor.execute(sql, (user1,))
    result = cursor.fetchone()
    print(len(result))
    return result



def insert(q):
    sqliteConnection = sqlite3.connect("software.db")
    cursor = sqliteConnection.cursor()
    print("In")
    sql = '''INSERT INTO User(host, port, username, pass) VALUES(?,?,?,?)'''
    cursor.execute(sql, q)
    sqliteConnection.commit()
    cursor.close()


def server_credential():
    host = input("Enter Host IP Address: ")
    port = int(input("Enter port number(preferred 22): "))
    username = input("Enter Username: ")
    password = getpass.getpass("Enter password")
    return host,port,username,password


def connectionbuild(s_host,s_port,s_username,s_password):
    # Create a new ssh client
    ssh_client = paramiko.SSHClient()

    # Set the policy to accept the SSH key automatically
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_client.connect(hostname=s_host, port=s_port, username=s_username, password=s_password)





def select():
    os.system('cls')
    conn = sqlite3.connect("software.db")
    cursor = conn.cursor()
    query = "SELECT name FROM software"
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result[0])
    cursor.close()
    conn.close()

    folder_path = r"C:\Users\LENOVO\Desktop\hpe2"

    for filename in os.listdir(folder_path):
        files = os.listdir(folder_path)

    name = input("\n \n Enter the name of the file from the above list: ")
    if name in files:
        return name
    else:
        print("File not found")


def installer(i,s_host,s_port,s_username,s_password):
    ssh_client = connectionbuild(s_host,s_port,s_username,s_password)
    cmd = f'echo "2416109" | sudo -S apt install ./{i} -y'
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    err = stderr.read().decode("utf-8")
    output = stdout.read().decode("utf-8")
    print(output)


def remove(i,s_host,s_port,s_username,s_password):
    ssh_client = connectionbuild(s_host,s_port,s_username,s_password)
    cmd = f'echo "2416109" | sudo -S apt remove {i} -y'
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    output = stdout.read().decode("utf-8")
    print(output)
    x = 0
    #sendmail(i,x)

def update(i):
    pass



# Transfer a file from the local machine to the remote machine
def send(i,s_host,s_port,s_username,s_password,s_path):

    ssh_client = connectionbuild(s_host,s_port,s_username,s_password)
    # Create an SCP client
    scp = SCPClient(ssh_client.get_transport())
    print(i)
    # local_path = 'C:\\Users\\Chirag K S\\Desktop\\abc.txt'
    local_path = os.path.join(r'C:\Users\LENOVO\Desktop\hpe2', i)
    remote_path = s_path
    scp.put(local_path, remote_path)
    # ssh_client.connect(hostname=host, port=port, username=username, password=password)
    # ssh_client.connect(host, username=username, password=password)
    #sendmail(i,x)
    scp.close()
    ssh_client.close()



# # Transfer a file from the remote machine to the local machine
def receive(s_host,s_port,s_username,s_password):
  

    # Create an SCP client
    ssh_client = connectionbuild(s_host,s_port,s_username,s_password)
    scp = SCPClient(ssh_client.get_transport())
    remote_path =     input = ("Enter the path of the file: ")
    local_path = r'C:\Users\USER\Desktop'
    scp.get(remote_path, local_path)
    scp.close()
    ssh_client.close()


def main():

   while(True):
    os.system('cls')
    print("\t\t\t______________________MULTI-SYSTEM_INSTALLER______________________")
    cmd = input("\nEnter '1' to list the systems  \n\nEnter '2' to select operation \n\nEnter '3' to Exit ")

    if cmd == '1':
     os.system('cls')
     conn = dbcon()
     s_host,s_port,s_username,s_password,s_path =  user(conn)
     
    elif cmd == '2':
        os.system('cls')
        cmd1 = input("\n  '4' : file send \n  '5' : file receive \n  '6' : install software \n  '7' : remove software' \n  '8' : List users \n")
        if cmd1 == '4':
            name = select()
            send(name,s_host,s_port,s_username,s_password,s_path)
        elif cmd1 == '5':
            receive(s_host,s_port,s_username,s_password)
        elif cmd1 == '6':
            name = select()
            installer(name,s_host,s_port,s_username,s_password) 
        elif cmd1 == '7':
            name = input("Enter the file name : ")
            remove(name,s_host,s_port,s_username,s_password)   
        elif cmd1== '8':
            accessdata()        

    elif(cmd == '3'):
        conn.close()
        break
    else:
        print("\n Invalid keyword")
        main()

if __name__ == "__main__":    
    main()