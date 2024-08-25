from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    decorator = user_passes_test(lambda user: user.userprofile.role == 'Admin')
    return decorator(view_func)

