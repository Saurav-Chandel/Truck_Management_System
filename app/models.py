from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Vehicle_Type = [
    ('single_excel', 'single_Excel'),
    ('multi_excel', 'multi_excel'),
]

Carriage_Type = [
    ('Clinker', 'Clinker'),
    ('Cement', 'Cement'),
]

class Add_Vehicle(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_type=models.CharField(max_length=100,choices=Vehicle_Type,blank=True,null=True)
    carriage_type=models.CharField(max_length=100,choices=Carriage_Type,blank=True,null=True)
    vehicle_number=models.CharField(max_length=100,blank=True,null=True)
    insurance_start_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    insurance_close_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    goods_tax=models.BooleanField(default=False)
    permit_tax=models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

Back_Load_Material = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
]

class Route(models.Model):
    destination=models.CharField(max_length=250,null=True,blank=True)
    km=models.CharField(max_length=250,null=True,blank=True)
    deisel=models.CharField(max_length=250,null=True,blank=True)
    driver_expense=models.CharField(max_length=250,null=True,blank=True)
    deisel_expense=models.CharField(max_length=250,null=True,blank=True)
  

class Back_Load_Material(models.Model):
    back_load_material=models.CharField(max_length=250,choices=Back_Load_Material,blank=True,null=True)
    price=models.CharField(max_length=250,null=True,blank=True)
    tonn=models.CharField(max_length=250,null=True,blank=True)

class Income_Per_Route(models.Model):
    vehicle=models.ForeignKey(Add_Vehicle,on_delete=models.CASCADE,null=True,blank=True)
    route=models.ForeignKey(Route,on_delete=models.CASCADE,null=True,blank=True)
    deisel=models.CharField(max_length=250,null=True,blank=True)
    expense=models.CharField(max_length=250,null=True,blank=True)
    earning=models.CharField(max_length=250,null=True,blank=True)
    back_load=models.BooleanField(default=False)
    back_load_material=models.ForeignKey(Back_Load_Material,on_delete=models.CASCADE,null=True,blank=True)
    tonn=models.CharField(max_length=250,null=True,blank=True)