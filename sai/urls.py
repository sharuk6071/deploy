from django.urls import path
from sai import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('',views.index,name='index'),
    path('ido/',views.Listido.as_view()),
    path('idoview/',views.Viewido.as_view()),

]
