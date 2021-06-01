#this is our entry point

from flask import Flask, render_template, request  #render_template let us render our html, request deals with requestm parameters
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail #using the send mail function in send_mail.py

app = Flask(__name__) #intialise my app

ENV = 'prod'

if ENV=='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']="postgresql://aiwkzlryteanux:92571fc127c7d404ffc8a36956116e728af133d5a7676ce7befe127f2a215c61@ec2-23-23-128-222.compute-1.amazonaws.com:5432/dchqdompslh6od"
else:                                       #sqlalchely error:no longer accepts postgres:// only postgresql://
    app.debug =False
    app.config['SQLALCHEMY_DATABASE_URI']="postgres://aiwkzlryteanux:92571fc127c7d404ffc8a36956116e728af133d5a7676ce7befe127f2a215c61@ec2-23-23-128-222.compute-"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db= SQLAlchemy(app) #use this to query our database

class Feedback(db.Model): #making a model/extends db with model
    __tablename__="feedback"
    id = db.Column(db.Integer, primary_key=True)
    customer= db.Column(db.String(200), unique=True)
    dealer= db.Column(db.String(200), unique=False)
    rating= db.Column(db.Integer)
    comments= db.Column(db.Text())

    def __init__(self, customer,dealer,rating,comments):  #similar to a constructor, self is like keywordf this in javascript
        self.customer= customer
        self.dealer= dealer
        self.rating= rating
        self.comments= comments

@app.route('/')  #our home page
def index():                                   #our method or funciton
    return render_template('index.html')         #renders our html element


@app.route('/submit', methods=['POST'])  #submmit is the route on the front end , needs an array of methods
def submit():
    if request.method == "POST":
        customer = request.form['customer']  #customer is the name of the field from the form
        dealer= request.form['dealer']
        rating= request.form['rating']
        comments= request.form['comments']
        print(customer,dealer,rating, comments)
        if customer=="" or dealer=="":        #if these string are empty render the home page
            return render_template('index.html', message="please enter required field")
        if db.session.query(Feedback).filter(Feedback.customer ==customer).count()==0: #means that if that customer does not exist then
            data= Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='you have already submitted feedback')



        return render_template('success.html')  # render the success page


if __name__ == '__main__':       
    app.run()                     #should allow us to run server

   