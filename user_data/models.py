from django.db import models
from django.contrib.auth.models import User
from localflavor.br.models import BRStateField


    
class Employeer(models.Model):    
    company_name = models.CharField(max_length=100,blank=False,null=False,unique=True)
    admin_user = models.OneToOneField(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=100,default='Brazil')
    state = BRStateField()
    city = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.company_name
    

class Positions(models.Model):
    company_name = models.ForeignKey(Employeer,on_delete=models.CASCADE)
    position = models.CharField(max_length=100, blank=True,null=True,unique=True)
    level = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.position

class Users_Data(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    born_date = models.DateField(blank=False,null=False)
    active = models.BooleanField(default=True)
    admission_date = models.DateField(blank=False,null=False)
    position = models.ForeignKey(Positions, on_delete=models.SET_NULL, null=True)
    employeer = models.ForeignKey(Employeer,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
