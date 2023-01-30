from psycopg2 import connect, OperationalError
from flask import Flask, request, render_template


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'


def insert_into_db(db, sql):
    cnx = connect(host=HOST, user=USER, password=PASSWORD, database=db)
    cnx.autocommit = True
    try:
        with cnx.cursor() as cursor:
            cursor.execute(sql)
    except OperationalError:
        print('Error in insert_into_db')
    cnx.close()


app = Flask(__name__)


@app.route('/add_movie', methods=['GET', 'POST'])
def run_app():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form.get('name')
        desc = request.form.get('desc')
        rate = float(request.form.get('rating'))
        if type(name) != str or len(name) > 255:
            raise Exception(f'Invalid movie name: {name}')
        if type(desc) != str:
            raise Exception(f'Invalid description: {desc}')
        if rate < 0 or rate > 10:
            raise Exception(f'Invalid rate: {rate}')

        sql = f"INSERT INTO movies(name, description, rating) VALUES('{name}', '{desc}', {rate});"
        db = 'cinemas_db'
        insert_into_db(db, sql)
        return 'added'


if __name__ == '__main__':
    app.run(debug=True)