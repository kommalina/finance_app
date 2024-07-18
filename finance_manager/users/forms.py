from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
#Форма дял регистрации пользователя
class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
