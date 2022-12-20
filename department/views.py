from django.shortcuts import render,redirect,reverse 
from .forms import Department,DepartmentForm

# Create your views here.
def add_dept(request):
    if request.method=='POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = DepartmentForm
        context = {"form":form}   
        return render(request,"add_dept.html",context) 
        
def list_dept(request):
    dept = Department.objects.all()
    context = {"dept":dept}
    return render(request,"list_dept.html",context)

def delete_dept(request,pk):
    dept = Department.objects.get(id = pk)
    dept.delete()
    return redirect("department:list-dept")

def update_dept(request,pk):
    dept = Department.objects.get(id =pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST ,instance = dept)
        if form.is_valid():
            form.save()
            return redirect("department:list-dept") 
    context = {"form":DepartmentForm(instance=dept)}
    return render(request,"update_dept.html",context)