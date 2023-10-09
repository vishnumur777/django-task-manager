from home.register.register import Users
from home.register.login import UsersLogin
from home.tasks.managetasks import ManagerTasks
from home.views import index
from django.urls import path

from drf_yasg.views import get_schema_view
from  rest_framework import permissions
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Swagger UI for Task manager",
        default_version="v1",
        description="Documentation for Task Manager",
    ),
    public=True,
)

urlpatterns = [
    path('index/',index),
    path('register/',Users.as_view()),
    path('login/',UsersLogin.as_view()),
    path('tasks/',ManagerTasks.as_view()),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name="swagger-schema")
]