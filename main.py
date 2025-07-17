from flask import Flask, render_template, request, redirect, url_for
from db import getTaskList, addTask, updateTask, deleteTask


app = Flask(__name__)

# tasklist = [['Dishes', True], ['Take out trash', False], ['Walk Dog', False]]
@app.route('/')
def home():
    tasklist = getTaskList()
    return render_template('index.html', TaskList = tasklist)

@app.route('/add', methods=['POST'])
def add():
    taskName = request.form['taskName']
    dueDate = request.form['dueDate']
    addTask(taskName, dueDate)
    
    return redirect(url_for('home'))

@app.route('/update',methods=['POST'])
def update():
    updatedTaskName = request.form['taskName']
    id = request.form['id']
    button = request.form['saveOrDelete']
    if button == 'save' :
        updateTask(updatedTaskName, id)
    elif button == 'x':
        deleteTask(id)
    return redirect(url_for('home'))

app.run(debug= True)
