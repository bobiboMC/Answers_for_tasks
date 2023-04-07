import psycopg2

# establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

# create the necessary tables
cur = conn.cursor()
cur.execute('''
    CREATE TABLE DEPARTMENT (
        ID INTEGER PRIMARY KEY,
        NAME VARCHAR(255),
        LOCATION VARCHAR(255)
    );
''')
cur.execute('''
    CREATE TABLE EMPLOYEE (
        ID INTEGER PRIMARY KEY,
        NAME VARCHAR(255),
        SALARY INTEGER,
        DEPT_ID INTEGER REFERENCES DEPARTMENT(ID)
    );
''')

# insert the sample data
cur.execute('''
    INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES
        (1, 'Executive', 'Sydney'),
        (2, 'Production', 'Sydney'),
        (3, 'Resources', 'Cape Town'),
        (4, 'Technical', 'Texas'),
        (5, 'Management', 'Paris');
''')
cur.execute('''
    INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID) VALUES
        (1, 'Candice', 4685, 1),
        (2, 'Julia', 2559, 2),
        (3, 'Bob', 4405, 4),
        (4, 'Scarlet', 2350, 1),
        (5, 'Ileana', 1151, 4);
''')
conn.commit()

# perform the query
cur.execute('''
    SELECT DEPARTMENT.NAME,COUNT(EMPLOYEE.ID) AS num_of_employees
    FROM DEPARTMENT
    LEFT JOIN EMPLOYEE
    ON DEPARTMENT.ID=EMPLOYEE.DEPT_ID
    GROUP BY DEPARTMENT.NAME
    ORDER BY COUNT(EMPLOYEE.ID) DESC,DEPARTMENT.NAME ASC;
''')
rows = cur.fetchall()

# print the results
for row in rows:
    print(f"{row[0]}: {row[1]}")
    
# close the cursor and connection
cur.close()
conn.close()
