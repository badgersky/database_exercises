from flask import Flask, request
from psycopg2 import connect, OperationalError


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'


def select_sql(db, sql_task):

    try:
        cnx = connect(user=USER, host=HOST, password=PASSWORD, database=db)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_task)
        if sql_task[:6].lower() == 'select':
            result = cursor.fetchall()
        else:
            result = None
    except OperationalError:
        print('There is error in execute_sql')
    else:
        cursor.close()
        cnx.close()
        return result


app = Flask(__name__)


@app.route('/')
def run_app():
    result = select_sql('exercises_db', 'SELECT * FROM products;')
    output = '<table>'
    for res in result:
        row = '<tr>'
        for data in res:
            row += f'<td>{data}</td>'
        output += row + '</tr>'
    return output + '</table>'


if __name__ == '__main__':
    app.run(debug=True)