import sqlite3

# create connection and cursor
conn = sqlite3.connect('software.db')
cursor = conn.cursor()

# create table
cursor.execute('''CREATE TABLE IF NOT EXISTS software (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                version TEXT NOT NULL,
                install_date TEXT NOT NULL)''')

cursor.execute("INSERT INTO software (id, name, version, install_date) VALUES (?, ?, ?, ?)",
               (1, "daisy-player.deb", "6.10.22", "2022-06-04"))
cursor.execute("INSERT INTO software (id, name, version, install_date) VALUES (?, ?, ?, ?)",
               (2, "vs.deb", "17.5.4", "2022-06-01"))
cursor.execute("INSERT INTO software (id, name, version, install_date) VALUES (?, ?, ?, ?)",
               (3, "python3-qal.deb", "98.0.4758.102", "2022-06-02"))
cursor.execute("INSERT INTO software (id, name, version, install_date) VALUES (?, ?, ?, ?)",
               (4, "JMyOggRadioPlayer.deb", "8.2.4", "2022-06-03"))
cursor.execute("INSERT INTO software (id, name, version, install_date) VALUES (?, ?, ?, ?)",
               (5, "reiser4progs.deb", "6.10", "2022-06-04"))

# commit changes
conn.commit()

# fetch data from table and make a list
cursor.execute("SELECT * FROM software")
rows = cursor.fetchall()
software_list = []
for row in rows:
    software_list.append(list(row))

# close connection
conn.close()

# print software list
print(software_list)
