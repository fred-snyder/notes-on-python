from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# initialize Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # 4 slashes are absolute paths
# initialize Database
db = SQLAlchemy(app) # how to create the SQLite db: activate venv | start Python shell | from app import db | db.create_all()

# database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #### repr: something with string conversion
    #### output the value of an instance of an object by using a print statement
    def __repr__(self):
        return f'Task {self.id}'

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        # new_task = Todo(content=task_content) # create new Todo object
        new_task  = Todo()
        new_task.content = task_content # this is the same as the line above
        new_task.test_attribute = "some content" # Python let's you add custom attributes to a class-instance/object

        # try to add the object to the database
        try:
            db.session.add(new_task)
            db.session.commit() # what db.session # what do you need to know about this?
            return redirect('/') # redirect back to the index page
        except:
            return 'There was an issue adding the task to the database'
    
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks) # pass the object to the template

@app.route("/delete/<int:id>") # pass a variable in the URL
def delete(id): # pass id as a parameter (otherwise you cannot use it)
    # create an object of the Todo item that you want to delete
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return 'There was an issue deleting the task from the database'
    

@app.route("/update/<int:id>", methods=['POST', 'GET']) # also specify the HTTP request method # we also want to use the /update URL to update the data based on the form.
def update(id):
    task_to_update = Todo.query.get_or_404(id)

    if request.method == 'POST':
        # since task_to_update is an instance of the object we want to update
        task_to_update.content = request.form['content']

        try:
            db.session.commit() # we don't have to update the database # only commit the changes
            return redirect("/") # return redirect to the index
        except:
            return 'Something went wrong when updating the task'
    else:
        return render_template("update.html", task=task_to_update)

if __name__ == "__main__":
    app.run(debug=True)
