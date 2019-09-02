from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# #set namespace
app_name = 'registration'

# urlpatterns = [
#     path('^', include('django.contrib.auth.urls')),
# ]
urlpatterns = [   
    path('', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', success_url = reverse_lazy('registration:password_reset_done')), name='password_reset'),
    path('done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views. PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html", success_url = reverse_lazy('registration:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
]
# link is available in terminal, we have to copy and paste it directly.