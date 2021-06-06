from django.urls import path, include
from cases import views

app_name = 'case'

urlpatterns = [
    path('', views.CaseListView.as_view(), name='c_list'),
    path('case_detail/<int:pk>', views.CaseDetailView.as_view(), name='c_detail'),
    path('create/', views.CaseCreateView.as_view(), name='c_create'),
    path('update/<int:pk>', views.CaseUpdateView.as_view(), name='c_update'),
    path('delete/<int:pk>', views.CaseDeleteView.as_view(), name='c_delete'),
]
