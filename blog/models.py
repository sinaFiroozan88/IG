from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
import os
import random
from django.utils import timezone

#
# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext
#
#
# def upload_image_path(instance, filename):
#     name, ext = get_filename_ext(filename)
#     final_name = f"{instance.id}-{instance.title}{ext}"
#     return f"blog/{final_name}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/')
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='post_author', blank=True, null=True,
                               verbose_name='کاربر')
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    pdf = models.FileField(default='Answer.pdf', null=True, blank=True)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def snippet(self):
        return self.text[:500] + " ..."

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=True, null=True,
                               related_name='Comment_author', verbose_name='کاربر')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    # class ProductsManager(models.Manager):
    #     def search(self, query):
    #         lookup = (
    #                 Q(title__icontains=query) |
    #                 Q(text__icontains=query) |
    #                 Q(tag__title__icontains=query)
    #         )
    #         return self.get_queryset().filter(lookup, active=True).distinct()

    # def get_absolute_url(self):
    #     return f"/products/{self.id}/{self.title.replace(' ', '-')}"
    #
    # objects = ProductsManager()

#
# class ContactUs(models.Model):
#     full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
#     email = models.EmailField(max_length=100, verbose_name='ایمیل')
#     subject = models.CharField(max_length=200, v
#     erbose_name='عنوان پیام')
#     text = models.TextField(verbose_name='متن پیام')
#     is_read = models.BooleanField(verbose_name='خوانده شده / نشده')
#
#     class Meta:
#         verbose_name = 'تماس با ما'
#         verbose_name_plural = 'تماس های کاربران'
#
#     def __str__(self):
#         return self.subject
