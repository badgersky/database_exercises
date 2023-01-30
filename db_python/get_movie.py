from flask import Flask
from psycopg2 import connect, OperationalError


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'


def get_row(movie_id):
    db = 'cinemas_db'
    sql = f'SELECT * FROM movies WHERE id={movie_id};'
    try:
        cnx = connect(host=HOST, user=USER, password=PASSWORD, database=db)
        with cnx.cursor() as cursor:
            cursor.execute(sql)
            if cursor.rowcount > 0:
                result = cursor.fetchall()
    except OperationalError:
        return 'Error in get_row'
    else:
        cnx.close()
        return result


app = Flask(__name__)


@app.route('/movie/<movie_id>')
def run_app(movie_id):
    result = get_row(movie_id)
    output = '<table><tr>'
    for row in result:
        for value in row:
            output += f'<td>{value}</td>'
    return output + '</tr></table>'


if __name__ == '__main__':
    app.run(debug=True)