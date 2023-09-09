from django.urls import path
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', RedirectView.as_view(url=reverse_lazy('polls:index')), name='base_redirect'),
    path('polls/', views.IndexView.as_view(), name='index'),
]
