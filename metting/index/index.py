import datetime

from flask import request, render_template, session, redirect, Blueprint

# from metting.utils.db_helper import SQLHelper
from metting.utils.db import Sqlcaozuo
#@app.route('/index',methods=['GET','POST'],endpoint='n2')
index1=Blueprint('index',__name__)
@index1.route('/index',methods=['GET','POST'], endpoint='index')
def index():
<<<<<<< HEAD
    time = SQLHelper.fetch_all('Select id,datetime from time ', [])
    room = SQLHelper.fetch_all('Select id,name from room ', [])
    user = session.get('user_info').get('name')
=======
    # time = SQLHelper.fetch_all('Select id,datetime from time ', [])
    time = Sqlcaozuo.time_fetch_all()
    # room = SQLHelper.fetch_all('Select id,name from room ', [])
    room = Sqlcaozuo.room_fetch_all()
    user = session.get('user')[0]
>>>>>>> 7683bebf28bddfc6a97a7602a4bb44a9f2730cb4
    if request.method=='GET':
        dt=datetime.datetime.today().strftime('%Y/%m/%d')
        # reseve_list = SQLHelper.fetch_all('Select rid,tid,name from reseve  INNER JOIN user ON reseve.uid=user.id WHERE reseve.date=%s', [dt])
        reseve_list = Sqlcaozuo.reseve_fetch_all(dt)
        reseve_dict = {}
        for item in reseve_list:
            if reseve_dict.get(item[0]):
                reseve_dict[item[0]]['time'][item[1]]=item[2]
            else:
                reseve_dict[item[0]] = {'time': {item[1]:item[2]}}
        return render_template('index.html',time_list=time,room_list=room,user=user,reseve_dict=reseve_dict,dt=dt)
    else:

        date=request.form.get('datetime')
        if date:
            dt=datetime.date(*map(int, date.split('/')))
            # reseve_list=SQLHelper.fetch_all('Select rid,tid,name from reseve  INNER JOIN user ON reseve.uid=user.id WHERE reseve.date=%s', [dt])
            reseve_list = Sqlcaozuo.reseve_fetch_all(dt)
            reseve_dict={}
            for item in reseve_list:
                if reseve_dict.get(item[0]):
                    reseve_dict[item[0]]['time'][item[1]] = item[2]
                else:
                    reseve_dict[item[0]] = {'time': {item[1]: item[2]}}
            return render_template('index.html',time_list=time,room_list=room,user=user,reseve_dict=reseve_dict,dt=date)
        else:
            return redirect('/index')
