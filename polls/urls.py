from django.urls import path
from polls import views

urlpatterns = [
    path('', views.home, name='polls-home'),
    path('polls/<int:id>/', views.details, name='polls-details'),
    path('<int:id>/vote/', views.vote, name='polls-vote'),
    path('<int:id>/results/', views.results, name='polls-results'),
]
