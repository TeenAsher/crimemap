from db_helper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
DB = DBHelper()

@app.route('/')
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as ex:
        print(ex)
        data = None
    return render_template('home.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.form.get('userinput')
        DB.add_input(data)
    except Exception as ex:
        print(ex)
    return home()

@app.route('/clear')
def clear():
    try:
        DB.clear_all()
    except Exception as ex:
        print(ex)
    return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True)