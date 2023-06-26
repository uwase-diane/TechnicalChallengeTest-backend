from django.urls import path
from .views import PageContentView,HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/page-content/', PageContentView.as_view(), name='page-content'),
]
