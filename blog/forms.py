from django import forms
from .models import Post, Comment
# from django.core import validators

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
     class Meta:
         model = Comment
         fields={'author', 'text',}

# class CreateContactForm(forms.Form):
#     full_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
#         label='full name',
#         validators=[
#             validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کاراکتر باشد')
#         ]
#     )
#
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'class': 'form-control'}),
#         label='email',
#         validators=[
#             validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیشتر از 100 کاراکتر باشد')
#         ]
#     )
#
#     subject = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان خود را وارد نمایید', 'class': 'form-control'}),
#         label='subject',
#         validators=[
#             validators.MaxLengthValidator(200, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
#         ]
#     )
#
#     text = forms.CharField(
#         widget=forms.Textarea(
#             attrs={'placeholder': 'your Comments', 'class': 'form-control', 'rows': '8',
#                    'cols': '20'}),
#         label='your Comments'
#     )
