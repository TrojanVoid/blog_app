from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(default = 'default_user_profile.png', upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username 
    
    def save(self, *args, **kwargs):
        super().save()
        
        img = Image.open(self.profile_pic.path)
        
        if img.height > 100 or img.width > 100:
            new_img = (100,100)
            img.thumbnail(new_img)
            img.save(self.profile_pic.path)
            
            
