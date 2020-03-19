# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Patient
# class PatientCreationForm(UserCreationForm):
#     email=forms.EmailField(required=True)
#     name=forms.CharField(max_length=30)
#     id=forms.IntegerField()
#     class Meta:
#         model=User
#         fields=('username','email','first_name','last_name','password1','password2')
#
#     def save(self, commit=True):
#         user=super().save(commit=False)
#         user.email=self.cleaned_data['email']
#         user.name=self.cleaned_data['username']
#         user.id=self.cleaned_data['password1']
#         if commit:
#             user.save()
#         return  user
