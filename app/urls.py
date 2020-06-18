from django.urls import path
from . import views

app_name = 'magic'
urlpatterns = [
    path('',views.index,name='main'),
    path('group/<str:slug>',views.group_detail,name='detail'),
    path('type/<int:type_id>',views.type_detail,name='type_detail'),
    path('article/<int:pk>',views.post_detail,name='post_detail'),
    path('politic/',views.politic,name='politic'),
    path('contact/',views.contact,name='contact'),
]