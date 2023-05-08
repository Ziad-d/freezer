from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_detail),
]

#get the data in JSON by adding '.json' at the end of url
urlpatterns = format_suffix_patterns(urlpatterns)