from psycopg2 import connect, OperationalError


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'


def execute_sql(db, sql_task):
    try:
        cnx = connect(user=USER, host=HOST, password=PASSWORD, database=db)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_task)
        if sql_task[:6].lower() == 'select':
            result = cursor.fetchall()
        else:
            result = None
    except:
        print('There is error in execute_sql')
    else:
        cursor.close()
        cnx.close()
        return result


results = execute_sql('exercises_db', 'SELECT * FROM products;')
for res in results:
    print(res)

execute_sql('exercises_db', "INSERT INTO products VALUES(4, 'i3', '5th generetion', 500, 5);")

results = execute_sql('exercises_db', 'SELECT * FROM products;')
for res in results:
    print(res)
