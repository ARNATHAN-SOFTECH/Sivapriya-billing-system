from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('billing/',views.billing_page,name="billing"),
    path('billing/bills/',views.bill_list,name="bill_list"),
    path('billing/bill/<int:bill_id>/',views.bill_detail,name="bill_detail"),
    path('billing/patient/<int:patient_id>/',views.patient_details,name="patient_details"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"
),

    path('op-registration/', views.op_registration, name='op_registration'),

]