from django.contrib import admin
from django.urls import path, include
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('post/<int:id>/', views.view_post, name='view_post'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/edit/<int:id>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
