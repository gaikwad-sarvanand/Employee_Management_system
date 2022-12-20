from django.urls import path
from . import views as v

app_name = "department"

urlpatterns = [
    path("add_department",v.add_dept,name="add-dept"),
    path("list_department",v.list_dept,name="list-dept"),
    path("<int:pk>/delete_dept/",v.delete_dept,name="delete-dept"),
    path("<int:pk>/update_dept/",v.update_dept,name="update-dept"),
]