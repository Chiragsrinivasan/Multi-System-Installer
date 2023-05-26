import sqlite3

# Create a connection to the database
conn = sqlite3.connect('database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the 'machines' table
cursor.execute('''
    CREATE TABLE machines (
        machine_id INTEGER PRIMARY KEY,
        ip_address VARCHAR(15) NOT NULL,
        port_no INTEGER NOT NULL,
        username VARCHAR(50) NOT NULL,
        os_type VARCHAR(50) NOT NULL,
        path VARCHAR(255) NOT NULL,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        machine_type VARCHAR(20) NOT NULL,
        CONSTRAINT machines_email_format CHECK (email LIKE '%_@__%.__%'),
        CONSTRAINT machines_machine_type CHECK (machine_type IN ('user', 'admin', 'software_repo'))
    )
''')

# Create the 'software_repository' table
cursor.execute('''
    CREATE TABLE software_repository (
        software_id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        version VARCHAR(50) NOT NULL,
        description VARCHAR(50),
        os_type VARCHAR(10),
        extension VARCHAR(10),
        CONSTRAINT unique_software_name_version UNIQUE (name, version),
        CONSTRAINT software_os_type CHECK (os_type IN ('Windows', 'Mac', 'Linux'))
    )
''')

# Create the 'scheduled_jobs' table
cursor.execute('''
    CREATE TABLE scheduled_jobs (
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        machine_id INTEGER,
        software_id VARCHAR(100) NOT NULL,
        scheduled_time DATETIME NOT NULL,
        CONSTRAINT fk_scheduled_jobs_machine
            FOREIGN KEY (machine_id)
            REFERENCES machines (machine_id)
            ON DELETE CASCADE,
        CONSTRAINT fk_scheduled_jobs_software
            FOREIGN KEY (software_id)
            REFERENCES software_repository (software_id)
    )
''')

cursor.execute('''
    CREATE TRIGGER check_user_machine
    BEFORE INSERT ON scheduled_jobs
    FOR EACH ROW
    WHEN NEW.machine_id NOT IN (SELECT machine_id FROM machines WHERE machine_type = 'user')
    BEGIN
        SELECT RAISE(IGNORE);
    END;
''')

# Create the 'completed_jobs' table
cursor.execute('''
    CREATE TABLE completed_jobs (
        job_id INTEGER PRIMARY KEY,
        machine_id INTEGER,
        software_id VARCHAR(100) NOT NULL,
        status VARCHAR(20) NOT NULL,
        completion_time DATETIME NOT NULL,
        error_message TEXT,
        CONSTRAINT fk_completed_jobs_machine
            FOREIGN KEY (machine_id)
            REFERENCES machines (machine_id)
            ON DELETE CASCADE,
        CONSTRAINT fk_completed_jobs_software
            FOREIGN KEY (software_id)
            REFERENCES software_repository (software_id)
    )
''')



# machine table contents
cursor.execute("insert into machines (machine_id,ip_address,port_no,username,os_type,path,password,email,machine_type)  values(?, ?, ?, ?, ?, ?, ?, ?, ?)", (1001,'192.168.0.103',22,'Sumukha','windows',r'C:\Users\LENOVO\Desktop\final','2416109','sumukharamesh15@gmail.com','software_repo'))
cursor.execute("insert into machines (machine_id,ip_address,port_no,username,os_type,path,password,email,machine_type)  values(?, ?, ?, ?, ?, ?, ?, ?, ?)", (1002,'192.168.0.102',22,'sumukha0','ubuntu','2416109','/home/sumukha0','sumukharamesh15@gmail.com','admin'))
cursor.execute("insert into machines (machine_id,ip_address,port_no,username,os_type,path,password,email,machine_type)  values(?, ?, ?, ?, ?, ?, ?, ?, ?)", (1003,'192.168.0.107',22,'sumukha1','ubuntu','2416109','/home/sumukha1','sumukharamesh15@gmail.com','user'))

#software repo contents
cursor.execute("insert into software_repository (software_id,name,version,description,os_type,extension)  values(?, ?, ?, ?, ?,?)", (1,'vs.deb','17.0.1','VS-Code for ubuntu','Linux','.db'))

#schedule job contents
cursor.execute("insert into scheduled_jobs (job_id,machine_id,software_id,scheduled_time)  values(?,?,?,?)", (1,1003,1,'.2023-05-25T23:15:28.984255Z'))




# Commit the changes and close the connection
conn.commit()
conn.close()
