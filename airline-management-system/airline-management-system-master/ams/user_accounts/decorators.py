from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def passenger_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="/user_accounts/login/"):
    """
    Decorator for views that checks that the logged in user is a passenger,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_Passenger,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="/user_accounts/login/"):
    """
    Decorator for views that checks that the logged in user is a manager,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_Manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
