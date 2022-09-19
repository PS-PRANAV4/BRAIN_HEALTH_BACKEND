

from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
import uuid
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,phone_number,designation,email,password=None):
        if not email:
            raise ValueError('user must have an email')
        if  password is None:
            raise ValueError('must need password')
        
        if not username:
            raise ValueError('must need username')
        user = self.model(email = self.normalize_email(email),username=username,first_name=first_name,last_name=last_name,phone_number=phone_number,designation=designation)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,first_name,last_name,phone_number,designation,email,username,password = None):
        
        user = self.create_user(email =self.normalize_email(email),first_name = first_name,last_name = last_name,username = username,phone_number = phone_number,designation = designation,password = password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user








choice = (("DOC","DOCTOR"),("CUSTOMER","CUSTOMER"),("ADMIN","ADMIN"))


class Accounts(AbstractBaseUser):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=32,unique=True)
    phone_number = models.CharField(max_length=13,unique=True)
    

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    referal_code = models.UUIDField(default=uuid.uuid4,null=True,blank=True)
    designation = models.CharField(choices=choice, max_length=8)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','first_name','last_name','phone_number','designation']

    objects = AccountManager()
    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True


class DocCertificate(models.Model):
    certi = models.ImageField(upload_to='user/',blank = True, null = True)
    user = models.ForeignKey(Accounts, on_delete= models.CASCADE) 

    def __str__(self):
        return self.user.username
