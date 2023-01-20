from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

#class CustomUserRegistrationForm(forms.ModelForm):
#    email = forms.EmailField(label = 'Email*')
#    password = forms.CharField(label = 'Password*', min_length = 5, max_length = 50, widget = forms.PasswordInput)
#    password2 = forms.CharField(label = 'Confirm Password*', min_length = 5, max_length = 50, widget = forms.PasswordInput)
#
#    class Meta:
#        model = CustomUser
#        fields = ('email', 'password')
#
#    def clean_email(self):
#        email = self.cleaned_data['email'].lower()
#        user_list = CustomUser.objects.filter(email=email)
#        if user_list.count():
#            raise ValidationError('There is already an account associated with that email.')
#        return email
#
#    def clean_password2(self):
#        password1 = self.cleaned_data['password']
#        password2 = self.cleaned_data['password2']
#        if (password1 and password2) and (password1 != password2):
#            raise ValidationError('Passwords do not match.')
#        return password2
#
#    def save(self, commit=True):
#        context = {
#            'email':self.cleaned_data['email'],
#            'password':self.cleaned_data['password'],
#        }
#        custom_user = CustomUser.objects.create_user(
#            context['email'],
#            context['password']
#        )
#        return custom_user
#
#class CustomUserChangeForm(UserChangeForm):
#    email = forms.EmailField(label = 'New Email')
#    old_password = forms.CharField(label = 'Current Password', min_length = 5, max_length = 50, widget = forms.PasswordInput)
#    new_password = forms.CharField(label = 'New Password', min_length = 5, max_length = 50, widget = forms.PasswordInput)
#    new_password2 = forms.CharField(label = 'Confirm New Password', min_length = 5, max_length = 50, widget = forms.PasswordInput)
#
#    class Meta:
#        model = CustomUser
#        exclude = []
#
#    def clean_new_password(self):
#        new_password = self.cleaned_data['new_password']
#        new_password2 = self.cleaned_data['new_password2']
#        if (new_password and new_password2) and (new_password != new_password2):
#            raise ValidationError('Passwords do not match.')
#        if not (new_password and new_password2):
#            raise ValidationError('Please enter new password twice.')
#        return new_password
#
#    def clean_email(self):
#        email = self.cleaned_data['email']
#        email_list = CustomUser.objects.filter(email=email)
#        if email_list.count():
#            raise ValidationError('There is already an account associated with that email.')
#        return email

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"



