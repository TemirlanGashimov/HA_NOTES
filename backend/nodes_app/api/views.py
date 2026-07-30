from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import NodeSerializer
from nodes_app.models import Node

from rest_framework import viewsets

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class NodeViewSetNew(viewsets.ViewSet):
    queryset = Node.objects.all()

    def list(self,request):
        serializers = NodeSerializer(self.queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        node = get_object_or_404(self.queryset, pk=pk)
        serializer = NodeSerializer(node)
        return Response(serializer.data)


    def create(self, request):
        serializer = NodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        node = get_object_or_404(self.queryset, pk=pk)
        serializer = NodeSerializer(node)
        node.delete()
        return Response(serializer.data)
    