
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    xyz=team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':xyz})