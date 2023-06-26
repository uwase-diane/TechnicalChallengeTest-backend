from rest_framework import serializers
from .models import PageContent

class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ('mission', 'vision', 'objectives')
