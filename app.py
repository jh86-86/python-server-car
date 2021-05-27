#this is our entry point

from flask import Flask, render_template, request  #render_template let us render our html, request deals with requestm parameters

app = Flask(__name__) #intialise my app

@app.route('/')  #our home page
def index():                                   #our method or funciton
    return render_template('index.html')         #renders our html element

if __name__ == '__main__':       
    app.debug =True              #will keep reloading whilst we are in development
    app.run()                     #should allow us to run server

   