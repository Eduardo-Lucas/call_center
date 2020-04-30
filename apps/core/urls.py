from django.urls import path

from apps.core.views import index, under_construction

urlpatterns = [

    path('', index, name='index'),
    path('under_construction', under_construction,
         name='under_construction'),

]
