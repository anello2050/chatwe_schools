from django.db import models
# ... 
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey,  GenericRelation
from django.contrib.contenttypes.models import ContentType


from django.db.models import Q




class User(AbstractUser):
    pass
       


class UserAssets(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="assets",
    )
    screen_name= models.CharField(max_length=50, default=None, blank=True, null=True)
    desc= models.TextField(default=None, blank=True, null=True)
    account_type= models.IntegerField(default=None, blank=True, null=True)


class UnactivatedAccounts(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    activation_code= models.CharField(max_length=100)


class AboutUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="about")
    content = models.TextField()


