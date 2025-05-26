from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')
        
        # Validate form data
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'signup.html')
        
        # Create user
        try:
            user = User.objects.create_user(username=username, password=password1)
            
            # Assign role
            if role == 'admin':
                admin_group, created = Group.objects.get_or_create(name='Admin')
                user.groups.add(admin_group)
            else:
                user_group, created = Group.objects.get_or_create(name='User')
                user.groups.add(user_group)
            
            # Log the user in
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to home page after successful signup
            
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'signup.html')