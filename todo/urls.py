from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.new, name='new'),
    path('edit', views.edit, name='edit'),
    path('imprint', views.imprint, name='imprint'),
]
