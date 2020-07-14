from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Contact(models.Model):
    your_name = models.CharField(max_length=2000)
    your_email = models.EmailField(null=True, blank=True)
    
    your_message = models.CharField(max_length=5000)
        
    def __str__(self):
        return self.your_email


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    phone = models.IntegerField(default=0,null=True)
    Class = models.CharField(max_length=50, blank=True)
    Class_teacher = models.CharField(max_length=20, blank=True)
    Admission_No = models.CharField(max_length=50, blank=True)
    
    image = models.ImageField(blank=True,null=True)
    School_fees_status = models.CharField(max_length=58, blank=True)
    Number_of_time_present_and_absent_in_school = models.CharField(max_length=50, blank=True)
    Total_number_in_class = models.CharField(max_length=50, blank=True) 
    Student_Academic_Status25= models.CharField(blank=True,null=True,max_length=50)
    Student_Academic_Status100 = models.CharField(blank=True,null=True,max_length=50)
    notifcations = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.user.username


class Result(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    Class = models.CharField(max_length=50, blank=True)
    Mathematics = models.CharField(blank=True,null=True,max_length=50)
    English_language = models.CharField(blank=True,null=True,max_length=50)
    Basic_Tech = models.CharField(blank=True,null=True,max_length=50)
    Business_Studies = models.CharField(blank=True,null=True,max_length=50)
    Home_Economics = models.CharField(blank=True,null=True,max_length=50)
    Agric_Science = models.CharField(blank=True,null=True,max_length=50)
    Physical_Education= models.CharField(blank=True,null=True,max_length=50)
    Yoruba = models.CharField(blank=True,null=True,max_length=50)
    French = models.CharField(blank=True,null=True,max_length=50)
    Computer_Science = models.CharField(blank=True,null=True,max_length=50)
    CRK = models.CharField(blank=True,null=True,max_length=50)
    Fine_Art = models.CharField(blank=True,null=True,max_length=50)
    Basic_Science = models.CharField(blank=True,null=True,max_length=50)
    Social_Studies = models.CharField(blank=True,null=True,max_length=50)
    Civic_Education = models.CharField(blank=True,null=True,max_length=50)
    Senior_result = models.CharField(blank=True,null=True,max_length=50)
    Mathematics = models.CharField(blank=True,null=True,max_length=50)
    English_language = models.CharField(blank=True,null=True,max_length=50)
    CRK = models.CharField(blank=True,null=True,max_length=50)
    Physics_or_Office_practice = models.CharField(blank=True,null=True,max_length=50)
    Chemistry_or_Insurance = models.CharField(blank=True,null=True,max_length=50)
    Biology = models.CharField(blank=True,null=True,max_length=50)
    Agriculture_Science = models.CharField(blank=True,null=True,max_length=50)
    Commerce = models.CharField(blank=True,null=True,max_length=50)
    Account = models.CharField(blank=True,null=True,max_length=50)
    Government = models.CharField(blank=True,null=True,max_length=50)
    Geography = models.CharField(blank=True,null=True,max_length=50)
    Computer_Science = models.CharField(blank=True,null=True,max_length=50)
    Literature_In_English = models.CharField(blank=True,null=True,max_length=50)
    Further_Mathematics = models.CharField(blank=True,null=True,max_length=50)
    Photography = models.CharField(blank=True,null=True,max_length=50)
    Dyeing_and_Bleaching = models.CharField(blank=True,null=True,max_length=50)
    Clothing_and_Textile = models.CharField(blank=True,null=True,max_length=50)
    Food_and_Nutrition = models.CharField(blank=True,null=True,max_length=50)
    Animal_Husbandry = models.CharField(blank=True,null=True,max_length=50)
    Civic_Education = models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):
        return self.user.username


    
