from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_cinema, name='create_cinema'),
    path('list/', views.cinemas_list, name='cinemas_list'),
    path('<int:cinema_id>/', views.view_cinema, name='view_cinema'),
    path('<int:cinema_id>/update/', views.update_cinema, name='update_cinema'),
    path('<int:cinema_id>/delete/', views.delete_cinema, name='delete_cinema'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

