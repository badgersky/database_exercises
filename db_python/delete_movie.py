from psycopg2 import connect, OperationalError
from flask import Flask


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'


def delete_movie(movie_id):
    db = 'cinemas_db'
    sql = f'DELETE FROM movies WHERE id={movie_id}'
    try:
        cnx = connect(host=HOST, user=USER, password=PASSWORD, database=db)
        cnx.autocommit = True
        with cnx.cursor() as cursor:
            cursor.execute(sql)
    except OperationalError:
        return 'Error in delete_movie'
    else:
        cnx.close()
        return 'movie deleted'


app = Flask(__name__)


@app.route('/delete/<movie_id>')
def run_app(movie_id):
    return delete_movie(movie_id)


if __name__ == '__main__':
    app.run(debug=True)
