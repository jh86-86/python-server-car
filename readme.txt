This is my first python server to do with cars selling feedback. It is a simple app but built to introduce me to the fundamentals 
of python, flask and deploying a pythin server to Heroku.

it will use postgres and flask: 

it's current dependcies are:
flask = as a framework
psycopg2 = PostgreSQL database adapter
psycopg2--binary = apparanty sometimes this is needed in addition to psycopg2

flask-sqlalchemy = a library that facilitates the communication between Python programs and databases.
 Most of the times, this library is used as an Object Relational Mapper (ORM) tool that translates Python classes to 
tables on relational databases and automatically converts function calls to SQL statements.

gunicorn = Python WSGI HTTP Server for UNIX

It is also connected to a fake email for the purpose of sending an email. It is my first time using such a service. 

It is now successfully deployed on Heroku at: https://jjpythonserver.herokuapp.com/submit
