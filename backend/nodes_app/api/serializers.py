from rest_framework import serializers
from nodes_app.models import Node

class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Node
        fields = '__all__'