from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', user_views.register , name='register-page'),
    path('profile/', user_views.profile , name='profile-page'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name='logout-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
