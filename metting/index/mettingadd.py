import json

from flask import request, session, Response,Blueprint

# from metting.utils.db_helper import SQLHelper
from metting.utils.db import Sqlcaozuo
#@app.route('/add',methods=['POST'],endpoint='n4')
mettingadd1=Blueprint('mettingadd1',__name__)
@mettingadd1.route('/add',methods=['POST'], endpoint='add')
def add():
    if request.method=='POST':
        rid=request.form.get('rid')
        tid = request.form.get('tid')
        date=request.form.get('date')
        uid=session.get('user')[1]
        user=session.get('user')[0]
        # row=SQLHelper.add('INSERT INTO reseve(rid, date, tid,uid) VALUES (%s, %s, %s,%s)',[rid,date,tid,uid])
        row = Sqlcaozuo.add(rid, date, tid, uid)
        ret={'stude':row,'user':user}
        return Response(json.dumps(ret))