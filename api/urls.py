from home.register.register import Users
from home.register.login import UsersLogin
from home.tasks.managetasks import ManagerTasks
from home.views import index
from django.urls import path

urlpatterns = [
    path('index/',index),
    path('register/',Users.as_view()),
    path('login/',UsersLogin.as_view()),
    path('tasks/',ManagerTasks.as_view())
]