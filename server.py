from flask import Flask, render_template, request, redirect
from utils import write_to_database_csv

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_database_csv(data)
            return redirect('./thank_you.html')
        except Exception:
            return f'Did not save to Database: {Exception}'
    else:
        return 'Somethng went wrong'
