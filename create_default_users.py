# Jalankan script ini dengan: python manage.py shell < create_default_users.py

from django.contrib.auth.models import User

# Buat user biasa
if not User.objects.filter(username='user').exists():
    User.objects.create_user(username='user', password='123')
    print("User 'user' dibuat.")

# Buat superuser admin
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(username='admin', password='123', email='admin@example.com')
    print("User 'admin' (superuser) dibuat.")