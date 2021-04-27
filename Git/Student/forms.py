from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms



class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter password"})
		}

class ChpwdForm(PasswordChangeForm):
		old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"old password"}))
		new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"new password"}))
		new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
		class Meta:
			model=User
			fields=['oldpassword','newpassword','confirmpassword']