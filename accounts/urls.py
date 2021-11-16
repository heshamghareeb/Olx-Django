from django.urls import path
from django.contrib.auth import views as auth_views

#from . import views

app_name = 'product'

urlpatterns = [
    # path('login/',auth_views.LoginView.as_view() , name='login'),#<int:id><type:varibale>
    # path('password_change/',auth_views.PasswordChangeView.as_view() , name='password_change'),#<int:id><type:varibale>
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view() , name='password_change_done'),#<int:id><type:varibale>
    # path('password_reset/',auth_views.PasswordResetView.as_view() , name='password_reset'),#<int:id><type:varibale>
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view() , name='password_reset_done'),#<int:id><type:varibale>

]

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

