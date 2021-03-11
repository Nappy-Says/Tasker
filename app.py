from peewee import Value
from models import added, tasks
from datetime import datetime
from flask import Flask, render_template, redirect
from flask.globals import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    liist = tasks.select()
    return render_template('index.html', liist=liist)

@app.route('/get', methods=['POST'])
def poooost():
    task = request.form.get("textmsg")
    added(text=task, date=datetime.now(), done=False)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_item():
    idtask = request.form.get('delete')
    # print(type(a), str(a))
    row = tasks.get(tasks.id == idtask).delete_instance()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5000)