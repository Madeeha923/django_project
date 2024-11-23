from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, default=0)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    


class department(models.Model):
    dep_id = models.CharField(max_length=20, primary_key=True)
    dept = models.CharField(max_length=100) 
    def __str__(self):
        return self.dept
    

class course(models.Model):
    c_id = models.CharField(max_length=50, primary_key= True)
    name = models.CharField(max_length=70, null=False)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    duration = models.IntegerField()
    def __str__(self):
        return self.name
    
class Studnt(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    course =models.ForeignKey(course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    phoneno = models.IntegerField (default=0)
    email = models.EmailField(max_length=254, default=0)

    
    def __str__(self):
        return self.name

    

# Create your models here.
