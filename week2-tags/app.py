#!/usr/bin/env python3
import os
from flask import Flask,render_template,request
import json
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient
client=MongoClient('127.0.0.1',27017)
dbm=client.shiyanlou

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)


class File(db.Model):
    __tablename__='File'
    id=db.Column(db.Integer,primary_key=True,unique=True)
    title=db.Column(db.String(80))
    created_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('Category.id'))
    category=db.relationship('Category',uselist=False)
    content=db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title=title
        self.created_time=created_time
        self.content=content
        self.category=category
    def add_tag(self,tag_name):
        file_item=dbm.files.find_one({'file_id':self.id})
        if file_item:
            tags=file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            dbm.files.update_one({'file_id':self.id},{'$set':{'tags':tags}})
        else:
            tags=[tag_name]
            dbm.files.insert_one({'file_id':self.id,'tags':tags})
        return tags

    def remove_tag(self,tag_name):

        file_item=dbm.files.find_one({'file_id':self.id})
        if file_item:
            tags=file_item['tags']
            try:
                new_tags=tags.remove(tag_name)
            except ValueError:
                return tags
            dbm.files.update_one({'file_id':self.id},{'$set',{'tags':new_tags}})
            return new_tags
        return {}

    @property
    def tags(self):
        file_item=dbm.files.find_one({'file_id':self.id})
        if file_item:
            print(file_item)
            return file_item['tags']
        else:
            return []


class Category(db.Model):
    __tablename__='Category'
    id=db.Column(db.Integer,unique=True,primary_key=True)
    name=db.Column(db.String(80))
    files=db.relationship('File')
    def __init__(self,name):
        self.name=name

db.create_all()
java=Category('Java')
python=Category('Python')
file1=File('Hello Java',datetime.utcnow(),java,'File Content - Java is cool!')
file2=File('Hello Python',datetime.utcnow(),python,'File Content - Python is cool!')
#db.create_all()
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()
file1.add_tag('tech')
file1.add_tag('java')
file1.add_tag('linux')
file2.add_tag('tech')
file2.add_tag('python')

@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())

@app.route('/files/<file_id>')
def file(file_id):
    file_item=File.query.get_or_404(file_id)
    return render_template('file.html',  file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',404)

if __name__=='__main__':
    app.run(
        port=3000,
        debug=True
        )

