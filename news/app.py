#!/usr/bin/env python3
import os
from flask import Flask,render_template,request
import json

app=Flask(__name__)

def jsonread(jsonname):
    with open(jsonname+'.json','r') as file:
        new_courses = json.loads(file.read())
    return new_courses

@app.route('/')

def index():
    path=os.getcwd()
    dirs=os.listdir(path)
    jsonnewval=[]
    filenamenew=''
    for jsonval in dirs:
        if jsonval.find('json')>0:
            jsonnewval.append(jsonval)
    for filename in jsonnewval:
        filenamenew+='<a href="/files/'+filename.replace('.json','')+'">'+filename+'</a> <br />'
#    filenamenew.pop(0)
    return filenamenew

@app.route('/files/<filename>')
def file(filename):

    path=os.getcwd()
    dirs=os.listdir(path)
    jsonnewval=[]
    filenamenew=''
    for jsonval in dirs:
        if jsonval.find('json')>0:
            jsonnewval.append(jsonval)
    if filename+'.json' in jsonnewval:
#        filenamenew=filename
        filelist=jsonread(filename)
    else:        
        return render_template('404.html'),404
    print(filelist)
    return render_template('file.html',  filelist=filelist)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run(
        port=3000,
        debug=True
        )

