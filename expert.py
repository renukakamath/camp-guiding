from flask import *
from database import *
import uuid
expert=Blueprint('expert',__name__)
@expert.route('/experthome',methods=['get','post'])
def experthome():
	return render_template('experthome.html')


@expert.route('/expert_addinternship',methods=['get','post'])
def expert_addinternship():
	data={}

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from intership where intership_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('expert.expert_addinternship'))

	if 'submit' in request.form:


		title=request.form['title']
		description=request.form['description']
		amount=request.form['amount']
		
		
		
		q="insert into intership values(null,'%s','%s','%s','%s',curdate(),'pending')"%(session['expert_id'],title,description,amount)
		res=insert(q)

		return redirect(url_for('expert.expert_addinternship'))
			
	q="select * from intership  "
	res=select(q)
	data['po']=res		
	return render_template('expert_addinternship.html',data=data)


@expert.route('/expert_addwork',methods=['get','post'])
def expert_addwork():
	data={}

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from works where works_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('expert.expert_addwork'))

	if 'submit' in request.form:


		des=request.form['des']
		
		file_path=request.files['file_path']
		path="static/"+str(uuid.uuid4())+file_path.filename
		file_path.save(path)

		
		q="insert into works values(null,'%s','%s','%s',curdate())"%(session['login_id'],des,path)
		res=insert(q)

		return redirect(url_for('expert.expert_addwork'))
			
	q="select * from works  where sender_id='%s'"%(session['login_id'])
	res=select(q)
	data['po']=res		
	return render_template('expert_addwork.html',data=data)



@expert.route('/expert_send_complaint',methods=['get','post'])
def expert_send_complaint():
    data={}
    if 'com_sub' in request.form:
        complaint=request.form['complaint']
        
        q="insert into complaints values(null,'%s','%s','pending',curdate())"%(session['login_id'],complaint)
        insert(q)
        flash("Send successfully")
        return redirect(url_for('expert.expert_send_complaint'))

    q="select * from complaints where sender_id='%s' "%(session['login_id'])
    data['view']=select(q)
    
    return render_template('expert_send_complaint.html',data=data)



@expert.route('/expert_viewrequest',methods=['get','post'])
def expert_viewrequest():
	data={}

	
	q="select * from request inner join products using (product_id) inner join photographer using (photographer_id) "
	res=select(q)
	data['po']=res		
	return render_template('expert_viewrequest.html',data=data)



@expert.route('/expert_viewphoto',methods=['get','post'])
def expert_viewphoto():
	data={}

	pid=request.args['pid']
	
	q="select * from photographer where photographer_id='%s'"%(pid)
	res=select(q)
	data['po']=res		
	return render_template('expert_viewphoto.html',data=data)

@expert.route('/expert_view_message')
def expert_view_message():
    data={}
    uid=session['login_id']
    q="SELECT * FROM `photographer` WHERE login_id IN (SELECT IF(sender_id = '%s',receiver_id,sender_id) FROM chat WHERE sender_id='%s' OR receiver_id='%s')"%(uid,uid,uid)
    print(q)
    res=select(q)
    data['res']=res
    return render_template('expert_view_message.html',data=data)

@expert.route('/expert_chat',methods=['get','post'])
def expert_chat():
    data={}
    uid=session['login_id']
    did=request.args['did']
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into chat values(NULL,'%s','%s','%s',now())"%(uid,did,name)
        insert(q)
        return redirect(url_for("expert.expert_chat",did=did))
    q="SELECT * FROM chat WHERE (sender_id='%s' AND receiver_id='%s') OR (sender_id='%s' AND receiver_id=('%s')) order by chat_id"%(uid,did,did,uid)
    # q="select * from chats where senderid='%s' and receiverid=( select login_id from doctors where doctor_id='%s' )"%(uid,did)
    print(q)
    res=select(q)
    data['ress']=res
    return render_template('expert_chat.html',data=data,uid=uid)
