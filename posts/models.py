from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

from PIL import Image

class Post(models.Model):
    post = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def slug(self):
        return slugify(self.title)
    
    def save(self, *args, **kwargs):
        super().save()
        
        if self.image:
        
            img = Image.open(self.image.path)
        
            if img.height > 500 or img.width > 500 or img.height < 500 or img.width < 500:
                new_img = (500,500)
                img.thumbnail(new_img)
                img.save(self.image.path)
                
    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
    
class PostView(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    time_stamp = models.PositiveIntegerField()
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('post_id','user_id'),)
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    
    class Meta:
        unique_together = (('user_id'),('post_id'),)
        
