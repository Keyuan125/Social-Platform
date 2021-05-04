from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Note: (Custom Label)
        #      1. 'username' and 'email' is the field name in the database,
        #         which we get from get_user_model (built-in method)
        #      2. 'Display Name' and 'Email Address' are the name that will
        #         be shown on the website

        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"
