from django.urls import path
from .views import home, contact, about, article_details, article_update, article_delete

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('article-details/<int:pk>', article_details, name='article_details'),
    path('article-update/<int:pk>', article_update, name='article_update'),
    path('article-delete/<int:pk>', article_delete, name='article_delete')
]