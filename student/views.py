from django.shortcuts import render, redirect
from student.models import Contact, Studnt, course, department 

# Create your views here.
def add(request):
     return redirect('admin/student/studnt/add/')

def std(request):
     s = Studnt.objects.all()
     context = {
          's': s
     }
     print(context)
     
     return render(request, 'std.html', context)






def index(request):
     return render(request, 'index.html',{})
def user(request):
     std = Studnt.objects.all()
     context = {
          'std': std
     }
     print(context)
     
     return render(request, 'user.html', context)
def about(request):
     return render(request, 'about.html', {})
def services(request):
     if request.method == 'POST':
          name = request.post.get('name')
          student_id = request.post.get('student_id')
          course = request.post.get('course')
          semester = request.post.get('semester')
          add = Studnt(name=name, student_id=student_id, course=course, semester=semester)
          add.save()
         
     
     return render(request, 'services.html', {})
def contact(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          message = request.POST.get('message')
          
          contact = Contact(name=name, email=email, message=message)
          contact.save()
     
     return render(request, 'contact.html', {})
# def admin(request):
#      return render(request,  'admin.py', {})