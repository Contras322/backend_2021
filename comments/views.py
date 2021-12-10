from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from comments.models import Comment
from comments.serializer import CommentSerializer
from application.views import user_id_auth


class CommentViewSet(viewsets.ViewSet):
    @user_id_auth
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)

        return Response(serializer.data)

    @user_id_auth
    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)

        return Response(serializer.data)

    @user_id_auth
    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.create(validated_data=request.data)
            serializer = CommentSerializer(comment)

            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors)

    @user_id_auth
    def update(self, request, pk=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            Comment.objects.filter(pk=pk).update(**self.request.data)

            return Response({"data": serializer.data})

        return Response({"errors": serializer.errors})

    @user_id_auth
    def delete(self, request, pk=None):
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()

        return Response({"status": "success", "message": None})
