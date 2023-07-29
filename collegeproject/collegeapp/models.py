from django.db import models
# from django.db.models.base import Model
# from django.db.models.deletion import CASCADE

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40)
    link = models.URLField(null=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=40)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

PURPOSE = (
    ('Enquiry', 'Enquiry'),
    ('Place Order', 'Place Order'),
    ('Return', 'Return'),
)

class Person(models.Model):
    name = models.CharField(max_length=250,unique=True)
    dob= models.DateField(null=True,blank=True)
    age=models.IntegerField()
    gender = models.CharField(choices=GENDER,max_length=30)
    number = models.CharField(max_length=12)
    email=models.EmailField()
    address=models.CharField(max_length=250,unique=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    purpose= models.CharField(max_length=30, choices=PURPOSE)
    Notebook = models.BooleanField(default=False)
    Pen = models.BooleanField(default=False)
    Exam_papers = models.BooleanField(default=False)


    def __str__(self):
        return self.name










