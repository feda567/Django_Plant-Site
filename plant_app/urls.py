from django.urls import path
from . import views


urlpatterns = [
  path('',views.index,name="index"),
  path('register/',views.register,name="register"),
  path('getdata/',views.getdata,name="getdata"),
  path('viewdata/',views.viewdata,name="viewdata"),
  path('login/',views.login,name="login"),
  path('booking/',views.booking,name='booking'),
  path('getbooking/',views.getbooking,name="getbooking"),
  path('getlogin/',views.getlogin,name="getlogin"),
  path('loginhome/',views.loginhome,name="loginhome"),
  path('Logout/',views.Logout,name="Logout"),
  path('edit/<int:did>',views.edit,name="edit"),
  path('update/<int:did>',views.update,name="update"),
  path('delete/<int:did>',views.delete,name="delete"),
  path('addplant/',views.addplant,name="addplant"),
  path('getplant/',views.getplant,name="getplant"),
  path('viewplant/',views.viewplant,name="viewplant"),
  path('view/<int:did>',views.view,name="view"),
  path('viewbooking/',views.viewbooking,name="viewbooking"),




]
