from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Accounts,Comments,DocCertificate,Groups,Post
from accounts.serializer import AccountSerializer,DocModelSerializer


class GroupSerializer(serializers.ModelSerializer):
    
    group_members = AccountSerializer(read_only= True, many = True)
    admin = DocModelSerializer
    class Meta:
        model = Groups
        fields = ('id','name','admin','group_members','group_description','group_profile_pic')

 

class PostSerializer(serializers.ModelSerializer):
    # liked_persons = AccountSerializer(many=True,read_only =True)
    liked_persons = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    groups = GroupSerializer(read_only = True)
    class Meta:
        model = Post
        fields = ('id','description','photo','likes','liked_persons','groups')
        







class CommentSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only = True)
    post = PostSerializer(read_only = True)

    class Meta:
        model = Comments
        fields = ('user','post','comment')










