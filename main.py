from flask import Flask, render_template
from db import getTaskList


app = Flask(__name__)

# tasklist = [['Dishes', True], ['Take out trash', False], ['Walk Dog', False]]
tasklist = getTaskList()
@app.route('/')
def home():
    return render_template('index.html', TaskList = tasklist)

app.run(debug= True)
