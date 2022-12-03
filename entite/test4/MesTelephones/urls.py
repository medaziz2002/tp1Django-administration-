from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='MesTelephones'),
    path('MesTelephones/' ,views.index, name='MesTelephones'),
    path('types/', views.list_typ, name='types'),
    path('del_prod/<int:id>', views.del_prod, name='del_prod')
    ]