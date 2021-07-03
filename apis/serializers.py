from rest_framework import serializers
from todo import models


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Todo
        fields = ['id', 'title', 'description', 'created', 'updated', 'work_status']
        read_only_fields = ['id', 'created', 'updated']


#

