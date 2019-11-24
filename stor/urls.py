
from django.urls import path
from .views import LoginView,DashboardView,RegisterView
from .views import StoreList,StoreDetail,StoreCreation,StoreUpdate,StoreDelete
from django.contrib.auth.models import Group


from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
app_name='stor'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login-view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('list/',StoreList.as_view(),name='list'),
    path('create/',StoreCreation.as_view(),name="index" ),
    path('detail/<int:pk>',StoreDetail.as_view(),name="detail" ),
    path('update/<int:pk>/',StoreUpdate.as_view(),name="update" ),
    path('delete/<int:pk>/',StoreDelete.as_view(),name="delete" ),

]
