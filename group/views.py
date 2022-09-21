from unicodedata import name
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView



from .serializer import CommentSerializer, GroupSerializer, PostSerializer
from django.http.response import JsonResponse
from .models import Groups, Post
from accounts.models import DocCertificate,Accounts
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Groups,Post,Comments
from django.db.models import F

# Create your views here.
class CreateGroups(APIView):
    def post(self,request):
        data = request.data
        try:
            if data['group_members']:
                try:
                    admin = DocCertificate.objects.get(user__username = data['admin'] )
                    group = Groups.objects.create(name=data['name'],admin=admin)
                    user = Accounts.objects.get(username=data['group_members'])
                    print(user)
                    group.group_members.add(user)
                    group.save()
                    return JsonResponse('nice',safe=False)
                except Exception as e:
                    print(e)
                    return JsonResponse("group member can't be added",safe=False)
        
        except:
            try:
                # admin = DocCertificate.objects.get(user__username = data['admin'] )
                user = request.user
                print(user)
                admin = DocCertificate.objects.get(user__username = user )
                group = Groups.objects.create(name=data['name'],admin=admin)
                return JsonResponse('nice',safe=False)
            except Exception as e:
                print(e)
                return JsonResponse('only doctors can create groups',safe=False)
    

class GetGroups(generics.ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    model = Groups
    permission_classes = [IsAuthenticated]
    def list(self, request):
        print(request.user)
        print(request.auth)
        print(request.content_type)
        print(request.stream)
        try:
            user = request.user
        

            admins = DocCertificate.objects.get(user__username=user)
            # Note the use of `get_queryset()` instead of `self.queryset`
            queryset = self.model.objects.filter(admin=admins)
            serializer = GroupSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({'status':'this is doc view'},status=400)

class GroupEnterView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    model = Post
    permission_classes = [IsAuthenticated]
    def list(self, request,groups):
        
        
        try:
            data = request.data
            user = request.user
            
            
            print(data)
            admin = DocCertificate.objects.get(user__username = user)
            group = Groups.objects.get(id=groups,admin=admin)
            print(group)
            post = self.model.objects.filter(groups__id = group.id)
            print(post)
        except Exception as e:
            print(e)
            return JsonResponse('valid',safe=False)
            
        
        serializer = PostSerializer(post,many = True)
        
        return Response(serializer.data)


class ShowComments(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    model = Comments
    permission_classes = [IsAuthenticated]


    def list(self, request, *args, **kwargs):
        data = request.data
        post = Post.objects.get(id = data['post'])
        comments = Comments.objects.filter(post = post)
        serializer = CommentSerializer(comments,many = True)
        return Response(serializer.data)


# class CreateComment(generics.CreateAPIView):

        
class LikePost(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        user = request.user
        
        try:
            user_object = Accounts.objects.get(username = user)
            print(data['id'])
            if Post.objects.filter(id = data['id'],liked_persons = user).exists():
                return Response({'status':'already liked'},status=200)    
            post = Post.objects.get(id=data['id'])
            print('nice')
            # post.likes = F('likes')+1
            post.likes = post.likes + 1
            print('welcome')
            post.save()
            
            post.liked_persons.add(user_object)
            post.save()
        except Exception as e:
            print(e)
            return Response({'status':'error occured'})
        
        return Response({'status':'sucess'},status=200)

class RemoveLike(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        user = request.user
        
        try:
            user_object = Accounts.objects.get(username = user)
            print(data['id'])
            if Post.objects.filter(id = data['id'],liked_persons = user).exists():
                    
                post = Post.objects.get(id=data['id'])
                print('nice')
                # post.likes = F('likes')-1
                post.likes = post.likes - 1 
                print('welcome')
                post.save()

                post.liked_persons.remove(user_object)
                post.save()
                return Response({'status':'sucess'},status=200)
            return Response({'status':'invalide user'},status=200)
        except Exception as e:
            print(e)
            return Response({'status':'error occured'})
        
        

        
 
 
   