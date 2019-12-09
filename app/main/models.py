from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=2000)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    class class Meta:
        ordering=["-name"]
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=2000)
    company = models.ForeignKey(Company, no_delete=models.CASCADE)

    class class Meta:
        ordering = ["-name"]
    
    def __str__(self):
        return self.name
    
    
