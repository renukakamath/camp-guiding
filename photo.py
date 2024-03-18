from flask import *
from database import *
import uuid
photo=Blueprint('photo',__name__)
@photo.route('/photohome',methods=['get','post'])
def photohome():
	return render_template('photohome.html')



@photo.route('/photo_addwork',methods=['get','post'])
def photo_addwork():
	data={}

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from works where works_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('photo.photo_addwork'))

	if 'submit' in request.form:


		des=request.form['des']
		
		file_path=request.files['file_path']
		path="static/"+str(uuid.uuid4())+file_path.filename
		file_path.save(path)

		
		q="insert into works values(null,'%s','%s','%s',curdate())"%(session['photographer_id'],des,path)
		res=insert(q)

		return redirect(url_for('photo.photo_addwork'))
			
	q="select * from works  where sender_id='%s'"%(session['photographer_id'])
	res=select(q)
	data['po']=res		
	return render_template('photo_addwork.html',data=data)

@photo.route('/photo_viewphotograher',methods=['get','post'])
def photo_viewphotograher():
	data={}
	
	q="select * from photographer"
	res=select(q)
	data['po']=res		
	return render_template('photo_viewphotograher.html',data=data)

@photo.route('/photo_viewexperts',methods=['get','post'])
def photo_viewexperts():
	data={}
	
	q="select * from experts"
	res=select(q)
	data['cr']=res	
	return render_template('photo_viewexperts.html',data=data)
@photo.route('/adviewusers',methods=['get','post'])
def adviewusers():
	data={}
	q="select *,concat(fname,' ',lname)as NAME from users"
	res=select(q)
	data['us']=res
	return render_template('adviewusers.html',data=data)

@photo.route('/adviewcomplaints',methods=['get','post'])
def adviewcomplaints():
	data={}
	q="SELECT * FROM complaints INNER JOIN  login on login.login_id=complaints.sender_id"
	res=select(q)	
	data['com']=res
	return render_template('adviewcomplaints.html',data=data)


@photo.route('/sendreply',methods=['get','post'])
def sendreply():
	data={}

	cid=request.args['cid']
	if "submit" in request.form:
		reply=request.form['reply']
		q="update complaints set reply ='%s'  where complaint_id='%s'"%(reply,cid)
		update(q)
		return redirect(url_for('photo.adviewcomplaints'))
	return render_template('sendreply.html',data=data)



@photo.route('/photo_viewscholarship',methods=['get','post'])
def photo_viewscholarship():
	data={}
	
			
	q="select * from scholarship"
	res=select(q)
	data['po']=res		
	return render_template('photo_viewscholarship.html',data=data)



@photo.route('/photo_agecategory',methods=['get','post'])
def photo_agecategory():
	data={}
	
			
	q="select * from age_category"
	res=select(q)
	data['po']=res		
	return render_template('photo_agecategory.html',data=data)



@photo.route('/photo_addcompatition',methods=['get','post'])
def photo_addcompatition():
	data={}

	aid=request.args['aid']
	
			
	q="select * from competition  inner join age_category using (age_category_id)"
	res=select(q)
	data['po']=res		
	return render_template('photo_addcompatition.html',data=data)

@photo.route('/photo_viewnewcamera',methods=['get','post'])
def photo_viewnewcamera():
	data={}

	
	
	q="select * from newproduct_techonology"
	res=select(q)
	data['po']=res		
	return render_template('photo_viewnewcamera.html',data=data)



@photo.route('/photo_viewintership',methods=['get','post'])
def photo_viewintership():
	data={}

	
	
	q="select * from intership  "
	res=select(q)
	data['cr']=res	
	return render_template('photo_viewintership.html',data=data)



@photo.route('/photo_viewtutorial',methods=['get','post'])
def photo_viewtutorial():
	data={}

	tid=request.args['tid']

	
			
	q="select * from tutorials  where product_techonology_id='%s'"%(tid)
	res=select(q)
	data['po']=res		
	return render_template('photo_viewtutorial.html',data=data)




@photo.route('/photo_viewproduct',methods=['get','post'])
def photo_viewproduct():
	data={}




			
	q="select * from products  where status='rent'"
	res=select(q)
	data['po']=res	



	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']	


	else:
		action=None

	if action=="request":
		q="insert into request values(null,'%s','%s',curdate(),'pending')"%(pid,session['photographer_id'])
		insert(q)
		return redirect(url_for('photo.photo_viewproduct'))



	return render_template('photo_viewproduct.html',data=data)




@photo.route('/adviewfeedback',methods=['get','post'])
def adviewfeedback():
	data={}
	q="select *,concat(fname,' ',lname)as NAME from feedback inner join users using(user_id)"
	res=select(q)
	data['feed']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			reply=request.form['reply'+str(i)]
			q="UPDATE feedback SET reply='%s' WHERE feedback_id='%s'" %(reply,res[j]['feedback_id'])
			update(q)
			return redirect(url_for('photo.adviewfeedback')) 	
		j=j+1
	return render_template('adview_feedback.html',data=data)



@photo.route('/photo_send_complaint',methods=['get','post'])
def photo_send_complaint():
    data={}
    if 'com_sub' in request.form:
        complaint=request.form['complaint']
        
        q="insert into complaints values(null,'%s','%s','pending',curdate())"%(session['login_id'],complaint)
        insert(q)
        flash("Send successfully")
        return redirect(url_for('photo.photo_send_complaint'))

    q="select * from complaints where sender_id='%s' "%(session['login_id'])
    data['view']=select(q)
    
    return render_template('photo_send_complaint.html',data=data)




@photo.route('/photo_chat',methods=['get','post'])
def photo_chat():
    data={}
    uid=session['login_id']
    did=request.args['did']
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into chat values(NULL,'%s','%s','%s',now())"%(uid,did,name)
        insert(q)
        return redirect(url_for("photo.photo_chat",did=did))
    q="SELECT * FROM chat WHERE (sender_id='%s' AND receiver_id='%s') OR (sender_id='%s' AND receiver_id=('%s')) order by chat_id"%(uid,did,did,uid)
    # q="select * from chats where senderid='%s' and receiverid=( select login_id from doctors where doctor_id='%s' )"%(uid,did)
    print(q)
    res=select(q)
    data['ress']=res
    return render_template('photo_chat.html',data=data,uid=uid)


@photo.route('/photo_view_message')
def photo_view_message():
    data={}
    uid=session['login_id']
    q="SELECT * FROM `experts` WHERE login_id IN (SELECT IF(sender_id = '%s',receiver_id,sender_id) FROM chat WHERE sender_id='%s' OR receiver_id='%s')"%(uid,uid,uid)
    print(q)
    res=select(q)
    data['res']=res
    return render_template('photo_view_message.html',data=data)




@photo.route('/photo_addtocart',methods=['post','get'])
def photo_addtocart():
	data={}
	st=request.args['stock']
	pname=request.args['pname']
	data['pname']=pname

	

	pamo=request.args['pamo']
	data['pamo']=pamo


	if "cart" in request.form:
		tot=request.form['total']	
		pid=request.args['pid']
		cid=session['photographer_id']

		qty=request.form['quantity']	
		


		if int(st)< int(qty):
			flash('enter less quantity')
		else:


			q="select * from order_master where photographer_id='%s' and status='pending'"%(cid)
			res=select(q)
			if res:
				omid=res[0]['order_master_id']

			else:

				q="insert into order_master values(null,'%s','0',curdate(),'pending')"%(cid)
				omid=insert(q)


			q="select * from order_child where product_id='%s' and order_master_id='%s'"%(pid,omid)
			res=select(q)
			if res:
				odid=res[0]['order_child_id']

				a=res[0]['quantity']
				qty=request.form['quantity']




				c=int(a)+int(qty)
				print(c)

				if int(c) > int(st):
					
					flash('Out Of Stock')
					return redirect(url_for('photo.photo_viewcart'))
					

				else:

		
					q="update order_child set quantity=quantity+'%s' , amount=amount+'%s' where order_child_id='%s'"%(qty,tot,odid)
					update(q)

			else:

				q="insert into order_child values(null,'%s','%s','%s','%s')"%(omid,pid,qty,tot)
				insert(q)

			q="update order_master set total_amount=total_amount+'%s' where order_master_id='%s'"%(tot,omid)
			update(q)

			flash('successfully')

			return redirect(url_for('photo.photo_viewcart'))

	return render_template('photo_addtocart.html',data=data)


@photo.route('/photo_viewcart',methods=['get','post'])
def photo_viewcart():
	data={}
	cid=session['photographer_id']



	q="SELECT * FROM `order_child` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `products` USING (`product_id`) INNER JOIN `photographer` USING (photographer_id)  where order_master.status='pending' and photographer_id='%s'"%(cid)
	res=select(q)
	data['len']=len(res)
	data['cart']=res

	for i in range(1,len(res)+1):
		if 'btn'+str(i) in request.form:
			oid=request.form['oid'+str(i)]
			pid=request.form['pid'+str(i)]

			q="update order_master set total_amount=total_amount-(select amount from order_child where product_id='%s' and order_master_id='%s') where order_master_id='%s'"%(pid,oid,oid)
			print(q)
			update(q)
			q="delete from order_child where order_master_id='%s' and product_id='%s'"%(oid,pid)
			delete(q)
			q=" select * from order_master where order_master_id='%s' and total_amount='0'"%(oid)
			ves=select(q)
			if ves:
				q="delete from order_master where order_master_id='%s'"%(oid)
				delete(q)


			flash('successfully')
			
			return redirect(url_for("photo.photo_viewcart"))

	return render_template('photo_viewcart.html',data=data)

@photo.route('/photo_makepayment',methods=['post','get'])	
def photo_makepayment():
	data={}
	cid=session['photographer_id']

	amt=request.args['amt']
	data['amt']=amt

	

	if "payment" in request.form:
		
		omid=request.args['omid']
		amt=request.args['amt']


		q="insert into payment values(null,'%s','%s',curdate())"%(omid,amt)
		insert(q)
		q="update order_master set status='Paid' where order_master_id='%s'"%(omid)
		update(q)

		q="select * from order_child where order_master_id='%s'"%(omid)
		res=select(q)

		for i in res:

			quantity=i['quantity']
			item_id=i['product_id']
			q="update products set quality=quality-'%s' where product_id='%s'"%(quantity,item_id)
			update(q)

			flash('successfully')

		return redirect(url_for('photo.photoviewmyorders'))

	return render_template('photo_makepayment.html',data=data,amt=amt)



@photo.route('/photo_addamount',methods=['post','get'])	
def photo_addamount():
	data={}

	

	if "submit" in request.form:
		
		bid=request.args['bid']
		des=request.form['des']
		


		q="update booking set amount='%s'  where booking_id='%s'  "%(des,bid)
		update(q)
		

		return redirect(url_for('photo.photograph_viewbookings'))

	return render_template('photo_addamount.html',data=data)



@photo.route('/photo_makeproposal',methods=['post','get'])	
def photo_makeproposal():
	data={}
	bid=request.args['bid']
		

	q="select * from proposal  where booking_id='%s'"%(bid)
	res=select(q)
	data['stt']=res

	

	if "submit" in request.form:
		
		
		des=request.form['product_name']
		


		q="insert into proposal  values(null,'%s','%s',curdate(),'pending')"%(bid,des)
		insert(q)
		

		return redirect(url_for('photo.photo_makeproposal',bid=bid))

	return render_template('photo_makeproposal.html',data=data)


@photo.route('/photoviewmyorders')
def photoviewmyorders():
	data={}
	cid=session['photographer_id']

	q="SELECT * FROM `order_child` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `products` USING (`product_id`) INNER JOIN `photographer` USING (photographer_id)  where ( photographer_id='%s' and order_master.status='Paid')  or (photographer_id='%s'  and order_master.status='Picked') or (photographer_id='%s'  and order_master.status='Delivered')"%(cid,cid,cid)
	res=select(q)
	print(q)
	data['myorder']=res
	return render_template('photoviewmyorders.html',data=data)


@photo.route('/photo_viewuser')
def photo_viewuser():
	data={}
	

	q="SELECT * FROM `user` inner join login using (login_id) "
	res=select(q)
	print(q)
	data['myorder']=res
	return render_template('photo_viewuser.html',data=data)



@photo.route('/photograph_viewbookings')
def photograph_viewbookings():
	data={}
	

	q="SELECT * FROM `booking` inner join photographer using (photographer_id) inner join user using (user_id) "
	res=select(q)
	print(q)
	data['myorder']=res
	return render_template('photograph_viewbookings.html',data=data)


@photo.route('/photo_chatuser',methods=['get','post'])
def photo_chatuser():
    data={}
    uid=session['login_id']
    did=request.args['did']
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into chat values(NULL,'%s','%s','%s',now())"%(uid,did,name)
        insert(q)
        return redirect(url_for("photo.photo_chatuser",did=did))
    q="SELECT * FROM chat WHERE (sender_id='%s' AND receiver_id='%s') OR (sender_id='%s' AND receiver_id=('%s')) order by chat_id"%(uid,did,did,uid)
    # q="select * from chats where senderid='%s' and receiverid=( select login_id from doctors where doctor_id='%s' )"%(uid,did)
    print(q)
    res=select(q)
    data['ress']=res
    return render_template('photo_chatuser.html',data=data,uid=uid)