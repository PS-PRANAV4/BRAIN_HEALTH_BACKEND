from email.policy import default
from django.db import models

# Create your models here.
from django.db import models
from accounts.models import DocCertificate,Accounts
# Create your models here.











class Groups(models.Model):
    name = models.CharField(max_length=30)
    admin = models.ForeignKey(DocCertificate,on_delete=models.CASCADE,related_name='admin')
    group_members = models.ManyToManyField(Accounts,null=True,blank=True,related_name="user_conections")
    group_description = models.TextField(blank=True, null=True)
    group_profile_pic = models.ImageField(upload_to = 'group/group_profile_pic', blank = True, null = True)
    


    def __str__(self):
        return self.name


class Post(models.Model):
    description = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to = 'media/post',blank = True,null = True)
    likes = models.IntegerField(null=True,blank=True,default = 0)
    liked_persons = models.ManyToManyField(Accounts, null=True,blank=True)
    groups = models.ForeignKey(Groups,on_delete=models.CASCADE,related_name='groups')


class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name='user')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post')