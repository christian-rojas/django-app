from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:user_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:user_id>/vote/', views.vote, name='vote'),
]