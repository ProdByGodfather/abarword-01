from django.urls import path
from main import views

urlpatterns = [
    path("",views.home,name='home'),
    path('posts/<int:id>/',views.post,name='post'),
    # path('<slug:slug>/')
]