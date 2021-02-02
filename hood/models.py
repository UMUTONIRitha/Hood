from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hood_image = models.ImageField(upload_to='images/')
    description = models.TextField(default='')
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search_by_location(cls, search_term):
        certain_user=cls.objects.filter(location__icontains=search_term)
        return certain_user
    def __str__(self):
        return self.location

class Profile(models.Model):
    profile_image = models.ImageField(default='default.png',upload_to='profile_pic')
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    neighbourhoods = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    business_name = models.CharField(max_length=60)
    description = models.CharField(max_length=200) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def create_business(self):
        self.save()
    def delete_business(self):
        self.delete()

class Post(models.Model):
    post = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
