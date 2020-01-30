from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='profile/no_images.png', upload_to='profile')

    def get_absolute_url(self):
        return reverse('user:login')

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            img = img.resize((400,400), Image.ANTIALIAS )
            img.save(self.photo.path)