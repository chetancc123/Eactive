from flask import Flask, render_template, request, redirect, url_for, abort
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'user'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/users')
def users():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
                       (name, email, role))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('users'))
    return render_template('new_user.html')

@app.route('/user_details_input', methods=['GET', 'POST'])
def user_details_input():
    if request.method == 'POST':
        user_id = request.form['user_id']
        return redirect(url_for('user_detail', id=user_id))
    return render_template('user_details_input.html')

@app.route('/users/<int:id>')
def user_detail(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    if user is None:
        abort(404)
    return render_template('user_detail.html', user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
