from .models import Department

def departments(request):
    dep = Department.objects.all()
    return dict(dep=dep)