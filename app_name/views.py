# from django.shortcuts import render

# # Create your views here.

# from django.views.generic import TemplateView   
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import PageContent

# class PageContentView(APIView):
#     def get(self, request):
#         page_content = PageContent.objects.first()
#         if page_content:
#             data = {
#                 "mission": page_content.mission,
#                 "vision": page_content.vision,
#                 "objectives": page_content.objectives,
#             }
#             return Response(data)
#         return Response(status=404)    

from django.views.generic import TemplateView      
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PageContent
from .serializer import PageContentSerializer


class HomePageView(TemplateView):
    template_name = 'app_name/home.html'

class PageContentView(APIView):
    def get(self, request):
        page_content = PageContent.objects.first()
        if page_content:
            serializer = PageContentSerializer(page_content)
            return Response(serializer.data)
        return Response(status=404)
