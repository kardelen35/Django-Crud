from django.urls import path
from .views import UserListCreateView, UserDetailView, AllUsersListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),#post
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),#put
    path('users/all/', AllUsersListView.as_view(), name='all-users-list'), #get
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'), #delete
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'), #put
]
