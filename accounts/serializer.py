from dataclasses import field, fields
from pyexpat import model
from wsgiref.validate import validator
from .models import Accounts,DocCertificate
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('username','password','email','phone_number','designation','first_name','last_name',)
        extra_kwargs = {
            
            'password': {'write_only': True}
        }


    def validate(self, validated_data):
        email = validated_data.get('email',None)
        username = validated_data.get('username',None)
        phone_number = validated_data.get('phone_number',None)
        print('validating')
        if Accounts.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already exist')})
        if Accounts.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exist')})
        if Accounts.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number':('phone number already exist')})
        
        return super().validate(validated_data)
    

    def create(self, validated_data):
        return Accounts.objects.create_user(**validated_data)





# class DocSerializer(serializers.Serializer):
#     certi = serializers.FileField()
    
class DocSerializer(serializers.Serializer):
    # user = AccountSerializer()
    certi = serializers.FileField()
    def create(self,validated_data,*args,**kwargs):
        print(*args,**kwargs)
        # user = self.context['request'].user
        print('veri_good')
        if 'certi' in (self.context['request'].FILES):
            print('good')
            print(validated_data)
            certi = (self.context['request'].FILES).getlist('certi')
            DocCertificate.objects.bulk_create([DocCertificate(user=validated_data['owner'],certi=i) for i in certi])
        return validated_data


class DocModelSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only = True, many = True)
    class Meta:
        model = DocCertificate
        fields = ('certi','user')
        