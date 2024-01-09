from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(_("Bio goes here"))
    code = name = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, related_name='ref_by', on_delete=models.CASCADE, blank=True)
    updated_at = models.DateTimeField( auto_now=True)
    created_at = models.DateTimeField( auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.username}---{self.code}"
    
    def get_recommened_profiles(self):
        pass
    


    def save(self, *args, **kwargs):
        if self.code == "":
            pass
        
        super().save(*args, **kwargs)