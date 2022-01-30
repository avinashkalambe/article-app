from django.urls import path
from .views import AuthorListV, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path('', AuthorListV.as_view(), name='author_list'),
    path('<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('create/', AuthorCreateView.as_view(), name='author_create'),
    path('update/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),
]

