from django.urls import path
from .views import ContactView, ContactDataView, ContactDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('writeus/', ContactView.as_view(), name = 'contact'),
    path('allmessages/',login_required(ContactDataView.as_view(), login_url='/admin'), name = 'messages'),
    path('allmessages/',login_required(ContactDataView.as_view(), login_url='/admin'), name = 'messages'),
    path('delete/<int:pk>', login_required(ContactDelete.as_view(), login_url='/admin'), name = 'deleteMessage'),
]