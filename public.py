from flask import *
from database import *
public=Blueprint('public',__name__)
@public.route('/',methods=['get','post'])
def publichome():
	return render_template('index.html')
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['log_id']=res[0]['login_id']
			if res[0]['user_type']=="admin":
				return redirect(url_for('admin.adminhome'))

			if res[0]['user_type']=="expert":
				q="select * from experts where login_id='%s'"%(session['log_id'])
				session['login_id']=select(q)[0]['login_id']
				session['expert_id']=select(q)[0]['experts_id']
				flash("Login Succeessfully")
				return redirect(url_for('expert.experthome'))


			if res[0]['user_type']=="photo":
				q="select * from photographer where login_id='%s'"%(session['log_id'])
				session['login_id']=select(q)[0]['login_id']

				session['photographer_id']=select(q)[0]['photographer_id']
				flash("Login Succeessfully")
				return redirect(url_for('photo.photohome'))
	
	return render_template('login.html')



@public.route('/expertreg',methods=['get','post'])
def expertreg():
    data={}
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        
        phone=request.form['phone']
        email=request.form['email']
       
        q="select * from login where username='%s'"%(username)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values (null,'%s','%s','expert')"%(username,password)
            id=insert(q)
            q="insert into experts values (null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
            insert(q)
            return redirect(url_for("public.login"))
    return render_template('expertreg.html',data=data)


@public.route('/photoreg',methods=['get','post'])
def photoreg():
    data={}
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        
        phone=request.form['phone']
        email=request.form['email']
       
        q="select * from login where username='%s'"%(username)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values (null,'%s','%s','photo')"%(username,password)
            id=insert(q)
            q="insert into photographer values (null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
            insert(q)
            return redirect(url_for("public.login"))
    return render_template('photoreg.html',data=data)