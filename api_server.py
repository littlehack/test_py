from flask import Flask, make_response, request,session
import time,os
import uuid
from juice import *
app = Flask(__name__)


app.secret_key = "d6ab27dbb2e4490e845a0e1952ceac1f"

@app.route('/login' , methods = ['GET','POST'])



#用户登录
#参数
#@param uname  pwd

def checkLogin():
    if request.method == "GET":
        data  = {
            'code':'401',
            'msg':'Method Not Allowed'
        }
        return data
    username = request.form['uname']
    password = request.form['pwd']
    if username == "admin" and password == "admin":
        id = str(uuid.uuid1())
        data  = {
            'code':200,
            'msg':'Success',
            'user': {
                'id':id,
                'privilege':1
            }
        }
        response = make_response(data)
        response.set_cookie('niktname',str(id),time.time()+60*60)
        response.headers['Authorization'] = "E5C91D2C-A937-4FCC-9CD9-3274AD761FCF"
        session["username"] = username
        return response
    else:
        data  = {
            'code':'500',
            'msg':'Failed'
        }
        return data

#用户注册
#参数
#@param uname pwd repwd
@app.route('/register',methods = ['GET','POST'])

def register():
    uname = request.form['uname']
    pwd = request.form['pwd']
    repwd = request.form['repwd']
    if repwd != pwd:
        data = {
            'code':-1,
            'msg':"The entered passwords are inconsistent"
        }
        return data
    data = {
        'code':1,
        'msg':'Registered successfully',
        'user':{
            'uname':uname,
            'verbose':"Simple User"
        }
    }
    return data


#用户展示用户数据（固定数据未做校验）
@app.route('/home/list')

def showList():
    #身份校验
    if session.get('username') != "admin":
        data = {
            'code':401,
            'msg':"unauthorized,Please Login"
        }
        return data
    #模拟用户列表数据
    data = {
        'code':1,
        'id':str(uuid.uuid1()),
        'uList':[
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice1')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice2')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice3')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice4')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice5')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice6')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice7')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice8')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice9')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice10')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice11')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice12')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice13')),
            str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice14'))
        ],
        "total":15
    }
    return data

#用户查询
#参数
#@param uname
@app.route('/search',methods = ['POST'])

def search():
    #身份校验
    if session.get('username') != "admin":
        data = {
            'code':401,
            'msg':"unauthorized,Please Login"
        }
        return data
    #模拟用户数据
    userInfo = {
        'juice1':str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice1')),
        'juice2':str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice2')),
        'juice3':str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice3')),
        'juice4':str(uuid.uuid3(uuid.NAMESPACE_DNS,'juice4'))
    }
    if request.form['uname'] not in userInfo.keys():
        msg = {
            'code':-1,
            'msg':"User Not Found"
        }
        return msg
    if request.form['uname'] in userInfo.keys():
        msg = {
            'code':1,
            'msg':"Success",
            'id':userInfo[request.form['uname']]
        }
        return msg

@app.route('/home/uploadImage',methods = ['POST'])

#用户头像上传
#参数
#@param file
def upload():
    #身份校验
    if session.get('username') != "admin":
        data = {
            'code':401,
            'msg':"unauthorized,Please Login"
        }
        return data
    reponse = request.files['file']
    whilteList = ['jpg','png','gif']
    if reponse.filename.split('.')[-1] not in whilteList:
        data = {
            'code':-1,
            'msg':'failed upload',
            'allowtype':whilteList
        }
        return data
    savepath = "./file/" + reponse.filename
    reponse.save(os.path.join(savepath))
    data  = {
        'code':1,
        'msg':'success upload',
        'allowtype':whilteList,
        'path':savepath
    }
    return data

    







app.run(host="0.0.0.0",port=8080,debug=True)