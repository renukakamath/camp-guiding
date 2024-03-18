from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)
@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/admin_viewphotograher',methods=['get','post'])
def admin_viewphotograher():
	data={}
	
	q="select * from photographer"
	res=select(q)
	data['po']=res		
	return render_template('admin_viewphotograher.html',data=data)


@admin.route('/admin_viewrequest',methods=['get','post'])
def admin_viewrequest():
	data={}
	pid=request.args['pid']
	
	q="select * from request inner join photographer using (photographer_id) where product_id='%s'"%(pid)
	res=select(q)
	data['po']=res		
	return render_template('admin_viewrequest.html',data=data)

@admin.route('/admin_viewexperts',methods=['get','post'])
def admin_viewexperts():
	data={}
	
	q="select * from experts"
	res=select(q)
	data['cr']=res	
	return render_template('admin_viewexperts.html',data=data)
@admin.route('/adviewusers',methods=['get','post'])
def adviewusers():
	data={}
	q="select *,concat(fname,' ',lname)as NAME from users"
	res=select(q)
	data['us']=res
	return render_template('adviewusers.html',data=data)

@admin.route('/adviewcomplaints',methods=['get','post'])
def adviewcomplaints():
	data={}
	q="SELECT * FROM complaints INNER JOIN  login on login.login_id=complaints.sender_id"
	res=select(q)	
	data['com']=res
	return render_template('adviewcomplaints.html',data=data)


@admin.route('/sendreply',methods=['get','post'])
def sendreply():
	data={}

	cid=request.args['cid']
	if "submit" in request.form:
		reply=request.form['reply']
		q="update complaints set reply ='%s'  where complaint_id='%s'"%(reply,cid)
		update(q)
		return redirect(url_for('admin.adviewcomplaints'))
	return render_template('sendreply.html',data=data)



@admin.route('/admin_addscholarship',methods=['get','post'])
def admin_addscholarship():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from scholarship where scholarship_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('admin.admin_addscholarship'))

	if 'submit' in request.form:
		sname=request.form['title']
		place=request.form['description']
		q="insert into scholarship values(null,'%s','%s',curdate(),'pending')"%(sname,place)
		res=insert(q)

		return redirect(url_for('admin.admin_addscholarship'))
			
	q="select * from scholarship"
	res=select(q)
	data['po']=res		
	return render_template('admin_addscholarship.html',data=data)



@admin.route('/admin_agecategory',methods=['get','post'])
def admin_agecategory():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from age_category where age_category_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('admin.admin_agecategory'))

	if 'submit' in request.form:
		
		age_category=request.form['age_category']
		q="insert into age_category values(null,'%s')"%(age_category)
		res=insert(q)

		return redirect(url_for('admin.admin_agecategory'))
			
	q="select * from age_category"
	res=select(q)
	data['po']=res		
	return render_template('admin_agecategory.html',data=data)



@admin.route('/admin_addcompatition',methods=['get','post'])
def admin_addcompatition():
	data={}

	aid=request.args['aid']
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		aid=request.args['aid']

		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from competition where competition_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('admin.admin_addcompatition',aid=aid))

	if 'submit' in request.form:
		
		title=request.form['title']
		description=request.form['description']

		date=request.form['date']
		venu=request.form['venu']

		q="insert into competition values(null,'%s','%s','%s','%s','%s',curdate(),'pending')"%(aid,title,description,date,venu)
		res=insert(q)

		return redirect(url_for('admin.admin_addcompatition',aid=aid))
			
	q="select * from competition  inner join age_category using (age_category_id)"
	res=select(q)
	data['po']=res		
	return render_template('admin_addcompatition.html',data=data)

@admin.route('/admin_addnewtech',methods=['get','post'])
def admin_addnewtech():
	data={}

	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		

		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from newproduct_techonology where product_techonology_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('admin.admin_addnewtech'))

	if 'submit' in request.form:
		title=request.form['title']
		description=request.form['description']

		image=request.files['image']
		path="static/"+str(uuid.uuid4())+image.filename
		image.save(path)

		q="insert into newproduct_techonology values(null,'%s','%s','%s')"%(title,description,path)
		res=insert(q)

		return redirect(url_for('admin.admin_addnewtech'))
			
	q="select * from newproduct_techonology"
	res=select(q)
	data['po']=res		
	return render_template('admin_addnewtech.html',data=data)



@admin.route('/admin_addproductcategory',methods=['get','post'])
def admin_addproductcategory():
	data={}

	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from product_category where product_category_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('admin.admin_addproductcategory'))

	if 'submit' in request.form:
		
		product_category=request.form['product_category']
		
		q="insert into product_category values(null,'%s')"%(product_category)
		res=insert(q)

		return redirect(url_for('admin.admin_addproductcategory'))
			
	q="select * from product_category "
	res=select(q)
	data['cr']=res		
	return render_template('admin_addproductcategory.html',data=data)



@admin.route('/admin_addtutorial',methods=['get','post'])
def admin_addtutorial():
	data={}

	tid=request.args['tid']

	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		tid=request.args['tid']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from tutorials where tutorials_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('admin.admin_addtutorial',tid=tid))

	if 'submit' in request.form:
		
		title=request.form['title']
		description=request.form['description']

		image=request.files['image']
		path="static/"+str(uuid.uuid4())+image.filename
		image.save(path)

		q="insert into tutorials values(null,'%s','%s','%s','%s')"%(tid,title,path,description)
		res=insert(q)

		return redirect(url_for('admin.admin_addtutorial',tid=tid))
			
	q="select * from tutorials  inner join newproduct_techonology using (product_techonology_id)  where product_techonology_id='%s'"%(tid)
	res=select(q)
	print(q)
	data['crss']=res		
	return render_template('admin_addtutorial.html',data=data)




@admin.route('/admin_addproduct',methods=['get','post'])
def admin_addproduct():
	data={}

	pid=request.args['pid']


	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		pid=request.args['pid']
		
	else:
		action=None	
	
	if 	action=="delete":
		q="delete from products where product_id='%s'"%(id)
		delete(q)
		
		return redirect(url_for('admin.admin_addproduct',pid=pid))

	if 'submit' in request.form:
		
		product_name=request.form['product_name']
		description=request.form['description']
		amount=request.form['amount']
		status=request.form['status']

		
		q="insert into products values(null,'%s','%s','%s','%s','%s')"%(pid,product_name,description,amount,status)
		res=insert(q)

		return redirect(url_for('admin.admin_addproduct',pid=pid))
			
	q="select * from products inner join product_category using (product_category_id)  where product_category_id='%s'"%(pid)
	res=select(q)
	data['po']=res		
	return render_template('admin_addproduct.html',data=data)




@admin.route('/adviewfeedback',methods=['get','post'])
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
			return redirect(url_for('admin.adviewfeedback')) 	
		j=j+1
	return render_template('adview_feedback.html',data=data)