from django.db import models
from django.utils.text import slugify

class Biography(models.Model):
    title           = models.CharField(max_length=100)
    name            = models.CharField(max_length=70)
    
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    gender          = models.CharField(choices=GENDER, max_length=20, default='male')
    place_of_birth  = models.CharField(max_length=50)
    date_of_birth   = models.DateField(auto_now=False, auto_now_add=False)
    description     = models.TextField()
    photo           = models.ImageField(upload_to='images')
    slug            = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Biography, self).save(*args, **kwargs)

    def __str__(self):
        return self.name