
from django.db import models
from django.contrib.auth.models import User
import django
from django.utils.timezone import now
# Create your models here.

Vehicle_Type = [
    ('single_excel', 'single_Excel'),
    ('multi_excel', 'multi_excel'),
]

Carriage_Type = [
    ('Clinker', 'Clinker'),
    ('Cement', 'Cement'),
]

class Devices(models.Model):
    User=models.ForeignKey(to=User,on_delete=models.CASCADE)
    iOS='iOS'
    Android='Android'
    CategoryChoices=[
        (iOS,'iOS'),
        (Android,'Android'),
    ]
    DeviceToken=models.CharField(max_length=250,blank=True,null=True)
    DeviceType=models.CharField(max_length=500,choices=CategoryChoices)
    DateAdded=models.DateTimeField(default=django.utils.timezone.now)

from django.core.validators import RegexValidator
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class Add_Vehicle(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    vehicle_type=models.CharField(max_length=100,choices=Vehicle_Type,blank=True,null=True)
    vehicle_image=models.ImageField(upload_to='vehicle_image',blank=True,null=True)
    carriage_type=models.CharField(max_length=100,choices=Carriage_Type,blank=True,null=True)
    vehicle_number=models.CharField(max_length=100,blank=True,null=True)
    insurance_start_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    insurance_close_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    goods_tax=models.BooleanField(default=False)
    permit_tax=models.BooleanField(default=False)

    created_at = models.DateTimeField(default=django.utils.timezone.now)
    updated_at = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.vehicle_number

Back_Load_Material = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
]

class Updated_Deisel_Price(models.Model):
    deisel_price=models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.deisel_price


class Route(models.Model):
    destination=models.CharField(max_length=250,null=True,blank=True)
    km=models.CharField(max_length=250,null=True,blank=True)
    # deisel=models.CharField(max_length=250,null=True,blank=True)
    # updated_deisel_price=models.ForeignKey(Updated_Deisel_Price,on_delete=models.CASCADE,null=True,blank=True)
    driver_expense=models.CharField(max_length=250,null=True,blank=True)
    # deisel_expense=models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.destination
    

class Back_Load_Material(models.Model):
    back_load_material=models.CharField(max_length=250,choices=Back_Load_Material,blank=True,null=True)
    price=models.CharField(max_length=250,null=True,blank=True)
    # tonn=models.CharField(max_length=250,null=True,blank=True)

class Income_Per_Route(models.Model):

    vehicle=models.ForeignKey(Add_Vehicle,on_delete=models.CASCADE,null=True,blank=True)
    route=models.ForeignKey(Route,on_delete=models.CASCADE,null=True,blank=True)
    deisel=models.CharField(max_length=250,null=True,blank=True)
    updated_deisel_price=models.ForeignKey(Updated_Deisel_Price,on_delete=models.CASCADE,null=True,blank=True)
    deisel_price=models.CharField(max_length=250,null=True,blank=True)
    extra_expenses=models.CharField(max_length=250,null=True,blank=True)
    total_expense=models.CharField(max_length=250,null=True,blank=True)
    payment_per_route=models.CharField(max_length=250,null=True,blank=True)
    total_earning_per_route=models.CharField(max_length=250,null=True,blank=True)

    back_load=models.BooleanField(default=False)
    back_load_material=models.ForeignKey(Back_Load_Material,on_delete=models.CASCADE,null=True,blank=True)
    tonn=models.CharField(max_length=250,null=True,blank=True,default=0)


    def save(self, *args, **kwargs):
        """
        Calculate deisel price and total expenses.
        """
        self.deisel_price=int(self.deisel) * int(self.updated_deisel_price.deisel_price)
        if self.extra_expenses:
          self.total_expense = int(self.route.driver_expense) + int(self.deisel_price) +int(self.extra_expenses)
        else:
          self.total_expense = int(self.route.driver_expense) + int(self.deisel_price)  

        self.total_earning_per_route1=int(self.payment_per_route)-int(self.total_expense)

        if self.back_load:
            self.total_earning_per_route=int(self.total_earning_per_route1)+(int(self.back_load_material.price) * int(self.tonn))
        else:
            self.total_earning_per_route=int(self.payment_per_route)-int(self.total_expense)

        # print(self.total_earning_per_route)    

        super(Income_Per_Route, self).save(*args, **kwargs)





