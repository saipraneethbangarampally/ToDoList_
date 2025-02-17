from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)

# Define the database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Move the route function outside the class
@app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)  # For debugging
    return render_template('base.html', todo_list=todo_list)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # Insert a sample todo only if the table is empty
        if not Todo.query.first():
            new_todo = Todo(title="todo 1", complete=False)
            db.session.add(new_todo)
            db.session.commit()

    app.run(debug=True)
