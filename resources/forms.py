from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Resource, User


class SignupForm(UserCreationForm):
    """
    Signup form with role selection (Lecturer / Student)
    """
    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Bootstrap classes automatically
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class ResourceForm(forms.ModelForm):
    """
    Form used for uploading and editing resources
    """
    class Meta:
        model = Resource
        fields = ["title", "description", "file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
