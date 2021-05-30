from django.urls import path
from . import views
from django.urls import path


app_name = 'team'

urlpatterns = [
    path('', views.MemeberListView.as_view(), name='m_list'),
    path('m_create/', views.MemberCreateView, name='m_create'),
    path('<int:pk>/m_delete/', views.MemberDeleteView.as_view(), name='m_delete'),
]
