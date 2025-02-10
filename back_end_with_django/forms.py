from django import forms

class LoginForm(forms.Form):

    email = forms.CharField(
        label="ایمیل",
        label_suffix=":",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "لطفا ایمیل خود را وارد کنید",
                "class": "form-control",
                "id": "email"
            }
        )
    )

    password = forms.CharField(
        label="رمز عبور",
        label_suffix=":",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "لطفا رمزعبور خود را وارد کنید",
                "class": "form-control",
                "id": "password"
            }
        )
    )