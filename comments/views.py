from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from comments.models import Comment
from comments.serializer import CommentSerializer


class CommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)

        return Response(serializer.data)

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.create(validated_data=request.data)
            serializer = CommentSerializer(comment)

            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors)

    def update(self, request, pk=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            Comment.objects.filter(pk=pk).update(**self.request.data)

            return Response({"data": serializer.data})

        return Response({"errors": serializer.errors})

    def delete(self, request, pk=None):
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()

        return Response({"status": "success", "message": None})
