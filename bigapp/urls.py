from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('test', views.test,name='test'),
    path('nominate', views.nominate,name='nominate'),
    path('Q&A', views.question,name='question'),
    path('logic', views.logic,name='logic'),
    path('result', views.result,name='result'),
    path('question', views.question,name='question')
]