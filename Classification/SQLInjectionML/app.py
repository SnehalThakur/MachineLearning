from flask import Flask
from flask import render_template
from flask import request
import utils.SQLiteDB as dbHandler

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    dbHandler.createTableIfNotExist()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('index.html', users=users)
    else:
        return render_template('index.html')


@app.route("/user")
def users():
    return dbHandler.retrieveUsers()

@app.route("/register", methods=['POST', 'GET'])
def registerUsers():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
    return dbHandler.registerUsers(username, email, password)


@app.route("/userWithUsername", methods=['POST', 'GET'])
def userWithUsername():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return dbHandler.retrieveUsersWithUsername(username)


@app.route("/order/<orderID>")
def order(orderID):
    return 'This is the Order page with {}'.format(orderID)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
