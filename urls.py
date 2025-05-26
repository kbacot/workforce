from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from workforce import views  # pastikan untuk mengimpor views dari aplikasi workforce

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workforce.urls', namespace='workforce')),  # Semua routing ke app workforce
    path('accounts/login/', auth_views.LoginView.as_view(template_name='workforce/login.html'), name='login'),
    path('data/', views.data_crud, name='data_crud'),
    path('sign-in/', auth_views.LoginView.as_view(template_name='workforce/login.html'), name='sign_in'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

