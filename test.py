import mysql.connector

db_params = { 
    "host" : "localhost",
    "database" : "fastapi",
    "user" : "root",
    "password" : "Lokendar$14"
}

sample_employees = [(1, 'John Doe', 50000),(2, 'Jane Smith', 60000),(3, 'Michael Johnson', 55000),(4, 'Emily Brown', 62000),(5, 'William Lee', 58000)]

try :

    conn = mysql.connector.connect(**db_params)

    cursor = conn.cursor()

    sql_query = "INSERT INTO employees (id,name,salary) VALUES (%s,%s,%s)"

    for employee in sample_employees:
        cursor.execute(sql_query,employee)
    
    conn.commit()

    cursor.close()



except mysql.connector.Error as error:
    print("error while connecting to mysql")

finally:
    if conn:
        conn.close()