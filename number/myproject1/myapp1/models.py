from django.db import models
class FacultyModel(models.Model):  
    faculty_name = models.CharField(max_length=30)  
    subject_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10, unique=True)  
    email = models.EmailField()  
  
    def __str__(self):  
        return (self.faculty_name+' '+ self.subject_name)

# Create your models here.
