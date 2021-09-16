from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name')