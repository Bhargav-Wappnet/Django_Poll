from django.urls import path
from Poll_System import views

app_name = 'Poll_System'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
