from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Student.models import MedicineInfo,User



class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter email"}),
		}

class ChpwdForm(PasswordChangeForm):
		old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"old password"}))
		new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"new password"}))
		new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
		class Meta:
			model=User
			fields=['oldpassword','newpassword','confirmpassword']

class ImForm(forms.ModelForm):
	class Meta:
		model=User
		fields=["first_name","last_name","age","gender","impf","organization_name","phone_no","pan_no","address",]
		widgets={
		"first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First name"}),
		"last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last name"}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update your age"}),
 		"gender":forms.Select(attrs={"class":"form-control","placeholder":"select your gender"}),
		"organization_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter organization name"}),
		"phone_no":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone number"}),
		"pan_no":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pan number"}),
		"address":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter address"}),
		}

class Medform(forms.ModelForm):
	class Meta:
		model=MedicineInfo
		fields=['medicine_name','quantity','batch_no','category','production_date','entry_date','expiry_date']
		widgets={
		"medicine_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Medicine name"}),
		"quantity":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Quantity"}),
		"batch_no":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Batch number"}),
		"category":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter category"}),
		"production_date":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Production date"}),
		"entry_date":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter entry date"}),
		"expiry_date":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter expiry date"}),

		}

