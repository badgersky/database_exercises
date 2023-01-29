from psycopg2 import connect, OperationalError


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'


def execute_sql(db, sql_task):
    try:
        cnx = connect(user=USER, host=HOST, password=PASSWORD, database=db)
        with cnx.cursor() as cursor:
            cursor.execute(sql_task)
            result = None
            if cursor.rowcount > 0:
                result = cursor.fetchall()

    except OperationalError:
        print('There is error in execute_sql')
    else:
        cursor.close()
        cnx.close()
        return result


results = execute_sql('exercises_db', 'SELECT * FROM products;')
for res in results:
    print(res)