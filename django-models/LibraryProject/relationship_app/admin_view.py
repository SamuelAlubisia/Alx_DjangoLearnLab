from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    if not user.is_authenticated:
        return False
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse(f"User: {request.user.username}, Role: {request.user.userprofile.role}")
