from flask import Flask, render_template, request, redirect				
from flask_sqlalchemy import SQLAlchemy			
from sqlalchemy.sql import func                         
from flask_migrate import Migrate		

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_db_name_here.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())  
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

@app.route("/")
def index():
    user1 = User.query.all()

    return(render_template('index.html', user1=user1))

@app.route("/add", methods=["POST"])
def add():
    new_instance_of_a_user = User(first_name=request.form['FN'], last_name=request.form['LN'], email=request.form['EM'], age=request.form['AG'])
    db.session.add(new_instance_of_a_user)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)