import sqlite3

conn = sqlite3.connect('employee_database.db')
print('Database has been opened')

# pass sql code
conn.execute('''CREATE TABLE employees
(EMP_ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
DEPARTMENT_NAME CHAR(40) NOT NULL,
REGION CHAR(50),
SALARY REAL);''')

print("table created")

conn.close()