from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import signals
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify


class Ebook(models.Model):
    
    title = models.CharField(max_length=140)
    description = models.TextField()
    publication_date = models.DateField()
    slug = models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ebook = models.ForeignKey(Ebook,on_delete=models.CASCADE,related_name='reviews')    
    review = models.TextField(blank=True)
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(1),MaxValueValidator(5)
    ])




@receiver(signals.pre_save,sender=Ebook)
def add_slug(sender,instance,**kwargs):
    instance.slug = slugify(instance.title)