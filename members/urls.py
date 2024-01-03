from django.urls import path# import path function from django.urls module
from . import views # import views module from current directory
urlpatterns = [
	path('members/', views.members, name='members'),
	path('members/details/<int:id>', views.details, name='details'),
	path('', views.main, name='main'),
    path('findmember/', views.findmember, name='findmember')
]