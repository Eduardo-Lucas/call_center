from django.urls import path

from apps.core.views import index, under_construction, precos

urlpatterns = [

    path('', index, name='index'),
    path('precos', precos, name='precos'),
    path('under_construction', under_construction,
         name='under_construction'),

]
