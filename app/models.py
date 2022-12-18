from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.CharField(max_length=20,unique=True)
    address = models.CharField(max_length=200,null=True)
    phone_number=models.CharField(max_length=10)
    company_name=models.CharField( max_length=100)
    date_of_joining=models.DateField(null=True)
    date_of_leaving=models.DateField(null=True)
    department=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="employee")
    
    def __str__(self) :
        name=self.first_name+' '+self.last_name
        return name

    
   


   
    
    


