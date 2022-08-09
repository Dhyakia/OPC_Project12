from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from users.models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'role')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):

    add_form = UserCreationForm
    list_display = ['id', 'email', 'password', 'role', 'date_created', 'date_updated', 'is_superuser']


admin.site.register(User, UserAdmin)