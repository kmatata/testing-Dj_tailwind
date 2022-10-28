from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('',views.test),
    path('test/',views.test2),
    path('test3/',views.test3),
]