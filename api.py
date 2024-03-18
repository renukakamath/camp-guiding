from flask import *
from database import *
import demjson
import uuid
api=Blueprint('api',__name__)
@api.route('/logins')
def logins():
	data={}
	u=request.args['username']
	p=request.args['password']
	q1="select * from login where username='%s' and `password`='%s'"%(u,p)
	print(q1)
	res=select(q1)
	if res:
		data['data']=res
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)



@api.route('/Userregistration')	
def Userregistration():
	data={}
	fname=request.args['fname']
	lname=request.args['lname']
	phone=request.args['phone']
	email=request.args['email']
	
	place=request.args['place']
	

	user=request.args['username']
	psw=request.args['password']

	q="insert into login values(null,'%s','%s','User')"%(user,psw)
	id=insert(q)
	q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
	insert(q)
	data['status']="success"
		
	return str(data)



@api.route('/viewphotograph')
def viewphotograph():
	data={}
	
	q="SELECT * FROM `photographer`  INNER JOIN login using (login_id)"
	res=select(q)
	if res:
		data['data']=res
		
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)


@api.route('/booknow')
def booknow():
	data={}
	log_id=request.args['log_id']
	pid=request.args['pid']

	q="insert into booking values(null,(select user_id from user where login_id='%s'),'%s','0',curdate(),'pending')"%(log_id,pid)
	insert(q)
	
	
	data['status']='success'
	return str(data)


@api.route('/user_view_crime/')
def user_view_crime():
	data={}
	
	q="SELECT * FROM `crimes` INNER JOIN `crime_type` USING(`crime_type_id`) INNER JOIN `stations` USING(`station_id`)"
	res=select(q)
	if res:
		data['data']=res
		
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)


@api.route('/user_view_criminals/')
def user_view_criminals():
	data={}
	
	q="SELECT *,CONCAT(`fname`,' ',`lname`) AS c_name FROM `criminals` INNER JOIN `crimes` USING(`crime_id`) INNER JOIN `crime_type` USING(`crime_type_id`)"
	res=select(q)
	if res:
		data['data']=res
		
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)


@api.route('/report/',methods=['get','post'])	
def report():
	data={}
	place=request.args['place']
	des=request.args['des']
	crim_id=request.args['crim_id']
	logid=request.args['logid']


	q="INSERT INTO `found_report` VALUES(NULL,'%s',(SELECT `user_id` FROM `users` WHERE `log_id`='%s'),'%s',NOW(),'%s')"%(crim_id,logid,place,des)
	insert(q)
	
	data['status']="success"
		
	return str(data)

@api.route('/viewproposal')
def viewproposal():
	data={}
	logid=request.args['log_id']
	bid=request.args['bid']
	q="SELECT * FROM `proposal` WHERE `booking_id`='%s'"%(bid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)


@api.route('/accept')
def accept():
	data={}
	logid=request.args['log_id']
	pid=request.args['pid']

	q="update  proposal set status='accept'  where proposal_id='%s'"%(pid)
	update(q)
	data['status']='success'
	
	return str(data)


@api.route('/reject')
def reject():
	data={}
	logid=request.args['log_id']
	pid=request.args['pid']

	q="update  proposal set status='reject'  where proposal_id='%s'"%(pid)
	update(q)
	data['status']='success'
	
	return str(data)


@api.route('/send_message/')
def send_message():
	data={}
	msg=request.args['msg']
	logid=request.args['logid']
	q="INSERT INTO `message` VALUES(NULL,(SELECT `user_id` FROM `users` WHERE `log_id`='%s'),'%s','pending',NOW())"%(logid,msg)
	insert(q)
	
	data['method']='send_message'
	data['status']='success'

	return str(data)

@api.route('/viewbooking/')
def user_view_feedback():
	data={}
	logid=request.args['log_id']
	q="SELECT * FROM `booking`  inner join photographer using (photographer_id) WHERE `user_id`=(SELECT `user_id` FROM `user` WHERE `login_id`='%s')"%(logid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['method']='user_view_feedback'
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)

@api.route('/complaint')	
def complaint():
	data={}
	lid=request.args['lid']
	c=request.args['complaint']
	q="insert into `complaints` values(null,'%s','%s','pending',now())"%(lid,c)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="complaint"
	return str(data)

@api.route('/viewcomplaints')
def viewcomplaints():
	data={}
	lid=request.args['lid']
	q="select * from complaints inner join user on user.login_id=complaint.user_id where login_id='%s'"%(lid)
	res=select(q)
	data['data']=res
	data['status']="success"
	data['method']="viewcomplaints"
	return str(data)

@api.route('/chatdetail')
def chatdetail():
	data={}
	sender_id=request.args['sender_id']
	receiver_id=request.args['receiver_id']
	
	gg="SELECT * FROM chat INNER JOIN login ON `login`.`Login_id`=`chat`.`sender_id` where `sender_id`='%s' AND `receiver_id`='%s'  or (`sender_id`='%s' AND `receiver_id`='%s' )"%(receiver_id,sender_id,sender_id,receiver_id)
	
	res=select(gg)
	if res:
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	data['method']='chatdetail'
	return str(data)



@api.route('/chat',methods=['get','post'])
def chat():
	data={}
	
	sender_id=request.args['sender_id']
	receiver_id=request.args['receiver_id']
	details=request.args['details']

	

	q="insert into chat values(null,'%s','%s','%s',curdate())"%(sender_id,receiver_id,details)
	insert(q)


	data['status']='success'
	data['method']='chat'


	return str(data)



@api.route('/Makepayment')
def Makepayment():
	data={}
	lid=request.args['login_id']
	amt=request.args['amount']
	pid=request.args['pid']
	name=request.args['name']
	bid=request.args['bid']

	
	q="insert into phpayment values(null,'%s','%s',now(),'paid')"%(pid,amt)
	insert(q)
	q="update  proposal set status='paid'  where proposal_id='%s'  "%(pid)
	update(q)
	q="update  booking set status='paid'  where booking_id='%s'  "%(bid)
	update(q)
	data['status']='success'
	return str(data)

	