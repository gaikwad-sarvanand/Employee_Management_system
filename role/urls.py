from django.urls import path
from . import views as v

app_name = "role"

urlpatterns = [
    path('add_role',v.add_role,name="add-role"),
    path('list_role',v.list_role,name="list-role"),
    path('<int:pk>/update/',v.update_role,name="update-role"),
    path('<int:pk>/delete/',v.delete_role,name="delete-role"),
]