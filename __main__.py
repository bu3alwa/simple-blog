import sys
from flask import Flask


app = Flask(__name__)
if __name__ == "__main__":
    app.run()

@app.route("/")
def main():
    return render_template('show_entries.html')

@app.route("/login")
def login_request():
    username = request.args.get('username')
    password = request.args.get('password')
    cursor = mysql.connect().cursor()
    data = cursor.fetchone()



