from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('a', views.addUser, name='add'),
     path('b/<int:id>', views.editUser, name='edit'),
     path('c/<int:id>', views.deleteUser, name='delete')
]