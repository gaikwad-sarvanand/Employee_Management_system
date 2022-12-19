from django.shortcuts import render, HttpResponse,redirect,reverse
from.forms import Employee,EmployeeForm,Role,RoleForm,Department,DepartmentForm
from django.views import generic

# Create your views here.


def index(request):
    return render(request, "index.html")

# def add_employee(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if(form.is_valid):
#             form.save()
#             return redirect("/")
#     else:
#         form = EmployeeForm()
#         context = {'form':form}
#         return render(request,"add_emp.html",context)
    
    
class EmployeeCreateView(generic.CreateView):
    template_name = "add_emp.html"
    form_class = EmployeeForm
    
    def get_success_url(self):
        return reverse("employee:index")
    
# def list_employee(request):
#     emp = Employee.objects.all()
#     context = {"emp":emp}
#     return render(request,"list_emp.html",context)


class EmployeeListView(generic.ListView):
    template_name = "list_emp.html"
    queryset = Employee.objects.all()
    context_object_name = "emp"
    
    

# def delete_emp(request,pk):
#     emp = Employee.objects.get(id=pk)
#     emp.delete()
#     return redirect("/")
    
class EmployeeDeleteView(generic.DeleteView):
    template_name = "delete_emp.html"
    queryset = Employee.objects.all()

    def get_success_url(self):
        return reverse("employee:list-emp")
    
def update_emp(request,pk):
    emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST , instance=emp)
        if form.is_valid():
            form.save()
            return redirect("employee:list-emp")
    form = EmployeeForm(instance=emp)
    context = {
            "form":form,
            "emp":emp
        }
    return render(request,"update_emp.html",context)