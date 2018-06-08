from flask import Flask, flash, render_template, request

from access import HoundifyAccessObject
from config import Config
from utils import QueryForm

app = Flask(__name__)
app.config.from_object(Config)

hound = HoundifyAccessObject()

@app.route('/')
@app.route('/query', methods=['GET', 'POST'])
def query():
    form = QueryForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Please ask a question.')
            return render_template('query.html', title = Config.TITLE, form = form, answer = '')
        else:
            querytext = form['querytext'].data
            response = hound.query(querytext)
            answer = response['AllResults'][0]['SpokenResponseLong']
            return render_template('query.html', title = Config.TITLE, form = form, answer = answer)
    elif request.method == 'GET':
        return render_template('query.html', title = Config.TITLE, form = form, answer = '')

if __name__ == '__main__':
    app.run()

