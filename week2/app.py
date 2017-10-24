#!/usr/bin/env python3
import os
from flask import Flask,render_template,request
import json
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)


class File(db.Model):
#    __tablename__='File'
    id=db.Column(db.Integer,primary_key=True,unique=True)
    title=db.Column(db.String(80))
    created_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('Category.id'))
    content=db.Column(db.Text)

class Category(db.Model):
#    __tablename__='Category'
    id=db.Column(db.Integer,unique=True,primary_key=True)
    name=db.Column(db.String(80))
    def __init__(self,name):
        self.name=name

#db.create_all()
java=Category('Java')
db.Category.all()
python=Category('Python')
file1=File('Hello Java',datetime.utcnow(),java,'File Content - Java is cool!')
file2=File('Hello Python',datetime,utcnow(),python,'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files/<file_id>')
def file(file_id):

    return render_template('file.html',  filelist=filelist)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run(
        port=3000,
        debug=True
        )

