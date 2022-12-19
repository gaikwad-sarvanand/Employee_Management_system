from django.urls import path
from . import views as v

app_name = "employee"

urlpatterns = [
    path('', v.index,name="index"),
    # path('add_emp', v.add_employee,name="add-emp"),
    path('add_emp', v.EmployeeCreateView.as_view(),name="add-emp"),
    # path('list_emp', v.list_employee,name="list-emp"),
    path('list_emp', v.EmployeeListView.as_view(),name="list-emp"),
    # path('<int:pk>/delete_emp/', v.delete_emp,name="delete-emp"),
    path('<int:pk>/delete_emp/', v.EmployeeDeleteView.as_view(),name="delete-emp"),
    path('<int:pk>/update_emp/', v.update_emp,name="update-emp"),
    
    
]
