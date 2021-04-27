from django.shortcuts import render,redirect
from Student.forms import UsForm,ChpwdForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def management(request):
	return render(request,'htfiles/management.html')

def HomePage(rt):
	
	return render(rt,'htfiles/HomePage.html')

def registration(fh):
	if fh.method=="POST":
		d=Reg(fh.POST)
		if d.is_valid():
			d.save()
			messages.success(fh,"You have registered successfully")
			return redirect('/login')
	d=Reg()
	return render(fh,'htfiles/registration.html',{'t':d})

def registration1(fh):
	if fh.method=="POST":
		d=UsForm(fh.POST)
		if d.is_valid():
			d.save()
			messages.success(fh,"You have registered successfully")
			return redirect('/login')
	d=UsForm()
	return render(fh,'htfiles/lg.html',{'t':d})

def donate(rf):
	return render(rf,'htfiles/donate.html')

def organization(request):
	return render(request,'htfiles/organization.html')

@login_required
def cgf(request):
	if request.method=="POST":
		print("Yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/login')
	c=ChpwdForm(user=request)
	return render(request,'htfiles/passwordchange.html',{'t':c})

def role(request):
	return render(request,'htfiles/role.html')

def userpage(request):
	return render(request,'htfiles/userpage.html')