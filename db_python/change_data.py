from psycopg2 import connect, OperationalError
from flask import Flask, request, render_template


HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'coderslab'
DB = 'cinemas_db'


def execute_sql(sql_task):
    try:
        cnx = connect(user=USER, host=HOST, password=PASSWORD, database=DB)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_task)
        if sql_task[:6].lower() == 'select':
            result = cursor.fetchall()
        else:
            result = None
    except OperationalError:
        return 'wrong id'
    else:
        cursor.close()
        cnx.close()
        return result


app = Flask(__name__)


@app.route('/<movie_id>', methods=['GET', 'POST'])
def run_app(movie_id):
    if request.method == 'GET':
        sql = f'SELECT * FROM movies WHERE id={movie_id};'
        data = execute_sql(sql)
        try:
            return render_template('form.html', data=data)
        except:
            return 'Wrong id'
    else:
        n = request.form.get('name')
        d = request.form.get('desc')
        r = int(request.form.get('rate'))
        sql = f"UPDATE movies SET name='{n}', description='{d}', rating={r} WHERE id={movie_id};"
        try:
            execute_sql(sql)
        except:
            return 'Ops... something went wrong'
        else:
            return 'Data changed successfully'


if __name__ == '__main__':
    app.run(debug=True)
