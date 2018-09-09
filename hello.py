from flask import Flask, request,url_for
import json
import os
import uuid
pw='ddd'
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def all():
    if request.method == 'GET':
        output=''
        files = os.listdir(os.getcwd())
        for file in files:
            if file[-5:]=='.json':
                with open(file,'r') as fi:   
                    output=output+'\n'+fi.read()+'   '+url_for('collection',id=file[:-5],_external=True)
        return output
    else:

        if request.headers.get('Authorization')!=pw:
            return 'Authorisation failed'
        if request.method == 'DELETE':
            files = os.listdir(os.getcwd())
            for file in files:
                if file[-5:]=='.json':
                    os.remove(file)
            return 'all deleted'
        elif request.method == 'POST':
            datax = request.form.to_dict()
            idnum=uuid.uuid1()
        #   datax['id']=idnum
            with open(str(idnum)+'.json','w') as f:
                json.dump(datax,f)
            content=str(datax)
            return content+'\n'+url_for('collection',id=idnum,_external=True)
        elif request.method == 'PUT':
            return 'specific uuid only'

@app.route('/users/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def collection(id):
    if request.method == "GET":
        with open(str(id)+'.json','r') as f:
            return f.read()
    
    else:
        if request.headers.get('Authorization')!=pw:
            return 'Authorisation failed'
        if request.method == "POST":
            return 'only allow no ID'

        elif request.method == 'DELETE':
            try:
                os.remove(str(id)+'.json')
                return str(id)+' deleted'
            except:
                return 'error'
        elif request.method == 'PUT':
            olddict={}
            try:
                with open(str(id)+'.json','r') as fi:            
                    olddict=dict(fi)
            except:
                pass
            datax = request.form.to_dict()
            for x in datax:
                olddict[x]=datax[x]
            content=str(olddict)
            with open(str(id)+'.json','w') as f:
                json.dump(olddict,f)
            return content


'''
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username




@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath



 $env:FLASK_APP = "hello.py"
 flask run
'''