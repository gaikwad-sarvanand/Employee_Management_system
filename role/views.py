from django.shortcuts import render,redirect
from.forms import Role,RoleForm


def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee:index")
    else:
        form = RoleForm()
        context = {'form':form}
        return render(request,"add_role.html",context)
    
    
def list_role(request):
    roles = Role.objects.all()
    context = {"roles":roles}
    return render(request,"list_role.html",context)


def update_role(request, pk):
    role = Role.objects.get(id = pk) 
    if request.method == 'POST':
        form = RoleForm(request.POST, instance =role)
        if form.is_valid():
            form.save()
            return redirect("role:list-role")
    else:
        form = RoleForm(instance=role)
        context = {'form':form}
        return render(request,"update_role.html",context)
    
def delete_role(request,pk):
    role = Role.objects.get(id=pk)
    role.delete()
    return redirect("role:list-role")