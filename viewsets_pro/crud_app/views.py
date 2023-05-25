from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ViewSet):
    #http_method_names = ['post','get','delete', 'patch']

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        obj = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        obj = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        obj = get_object_or_404(Post, pk=pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)