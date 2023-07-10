from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactDetails(models.Model):
    UserName = models.CharField(max_length=50, null=False)
    UserEmail=models.EmailField(default=None, null=True, blank=True)
    UserPhoneNumber = models.CharField(max_length=10,null=False)
    IsSpam=models.BooleanField(default=False)

    def __str__(self) :
        return self.UserNameUsersContact

class userDetails(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    UserPhoneNumer = models.CharField(max_length=10,null=False,unique=True)
    IsSpam= models.BooleanField(default=False)
    def __str__(self) :
        return self.UserName
    
class mapping_User_Contact(models.Model):
    User= models.ForeignKey(User,on_delete=models.CASCADE , null = False)
    UserContact= models.ForeignKey(ContactDetails, on_delete=models.CASCADE, null = False)

    def __str__(self) -> str:
        return f"{self.user} , {self.contact}"   