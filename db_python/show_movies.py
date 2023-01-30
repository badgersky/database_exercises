from psycopg2 import connect, OperationalError
from flask import Flask


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'


def get_data(db, sql):
    try:
        cnx = connect(host=HOST, user=USER, password=PASSWORD, database=db)
        cnx.autocommit = True
        with cnx.cursor() as cursor:
            cursor.execute(sql)
            if cursor.rowcount > 0:
                result = cursor.fetchall()
    except OperationalError:
        return f'Error in get_data'
    else:
        cnx.close()
        return result


app = Flask(__name__)


@app.route('/movies')
def run_app():
    database = 'cinemas_db'
    sql = 'SELECT * FROM movies;'
    result = get_data(database, sql)
    output = '<table>'
    for res in result:
        row = '<tr>'
        for element in res:
            row += f'<td>{element}</td>'
        output += row + '</tr>'
    return output + '</table>'


if __name__ == '__main__':
    app.run(debug=True)
