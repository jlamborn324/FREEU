
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from . import settings as setting


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketplace.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/<username>/', user_views.get_user_profile, name='profile'),
    
    path('profile/', user_views.profile, name='profile'),   # url that works 

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
    auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', 
    auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', 
    auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('chat/', include('chat.urls')),
    path('activate/<uidb64>/<token>/', user_views.activate, name='activate')

] + static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)
