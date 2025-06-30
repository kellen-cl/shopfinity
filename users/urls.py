from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    #path('create/', views.create_user, name='create_user'),
    #path('detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),   
    #path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]