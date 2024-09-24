import sqlite3

conn = sqlite3.connect('employee_database.db')
print('Database has been opened')

# pass sql code
# conn.execute('''CREATE TABLE employees
# (EMP_ID INT PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# DEPARTMENT_NAME CHAR(40) NOT NULL,
# REGION CHAR(50),
# SALARY REAL);''')

# print("table created")
#
# conn.close()

# PART 2

# conn.execute("INSERT INTO employees (EMP_ID, NAME, DEPARTMENT_NAME, REGION, SALARY) VALUES (3, 'Jack', 'Executive', 'UK', 50000.00)");
#
# conn.execute("INSERT INTO employees (EMP_ID, NAME, DEPARTMENT_NAME, REGION, SALARY) VALUES (4, 'Alexis', 'HR', 'UK', 32000.00)");
#
# conn.execute("INSERT INTO employees (EMP_ID, NAME, DEPARTMENT_NAME, REGION, SALARY) VALUES (5, 'Peter', 'Technology', 'US', 36000.00)");
#
# conn.execute("INSERT INTO employees (EMP_ID, NAME, DEPARTMENT_NAME, REGION, SALARY) VALUES (6, 'Louis', 'Marketing', 'Norway', 25000.00)");
#
# conn.commit()
#
# print("Records were inserted")
#
# conn.close()


# PART 3

# print("opened database")
#
# cursor = conn.execute("SELECT EMP_ID, NAME, DEPARTMENT_NAME, REGION, SALARY FROM EMPLOYEES WHERE EMP_ID = 6")
#
# for row in cursor:
#     print("EMP_ID = ", row[0])
#     print("NAME = ", row[1])
#     print("DEPARTMENT_NAME = ", row[2])
#     print("REGION = ", row[3])
#     print("SALARY = ", row[4], "\n")
#
# print("operation done")
# conn.close()


# PART 4

print("Opened")
conn.execute("UPDATE EMPLOYEES SET SALARY = 30000.00 WHERE EMP_ID = 6")
conn.commit()
print("Number of rows affected by update:", conn.total_changes)