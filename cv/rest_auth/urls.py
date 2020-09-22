from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', csrf_exempt(PasswordResetView.as_view()),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', csrf_exempt(PasswordResetConfirmView.as_view()),
        name='rest_password_reset_confirm'),
    url(r'^login/$', csrf_exempt(LoginView.as_view()), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', csrf_exempt(LogoutView.as_view()), name='rest_logout'),
    url(r'^user/$', csrf_exempt(UserDetailsView.as_view()), name='rest_user_details'),
    url(r'^password/change/$',csrf_exempt(PasswordChangeView.as_view()),
        name='rest_password_change'),
]
