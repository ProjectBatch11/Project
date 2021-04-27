from django.urls import path
from Student import views
from django.contrib.auth import views as v
urlpatterns=[
	path('',views.management,name="mag"),
	path('home/',views.HomePage,name="home"),
	path('login/',v.LoginView.as_view(template_name="htfiles/AdminPage.html"),name="log"),
	path('lgo/',v.LogoutView.as_view(template_name='htfiles/logout.html'),name="logo"),
	path('registration/',views.registration,name="reg"),
	path('registration1/',views.registration1,name="nreg"),
	path('donate/',views.donate,name="don"),
	path('org/',views.organization,name="og"),
	path('chpwd/',views.cgf,name="cg"),
	path('reset/',v.PasswordResetView.as_view(template_name="htfiles/resetpassword.html"),name="reset_password"),
	path('rst_done/',v.PasswordResetDoneView.as_view(template_name='htfiles/resetpassworddone.html'),name="password_reset_done"),
	path('ret_cf/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(template_name='htfiles/resetpasswordconfirm.html'),name="password_reset_confirm"),
	path('rst_cmplt/',v.PasswordResetCompleteView.as_view(template_name="htfiles/reset_password_complete.html"),name="password_reset_complete"),
	path('role/',views.role,name="ro"),
	path('userpage/',views.userpage,name="up"),
]