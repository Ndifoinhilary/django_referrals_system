from django.db import models

from django.contrib.auth.models import User

from referrals.utils import generate_ref_code

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(
        User, related_name="ref_by", on_delete=models.CASCADE, blank=True, null=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}---{self.code}"

    def get_recommened_profiles(self):
        qs = Profile.objects.all()
        my_recs = [p for p in qs if p.recommended_by == self.user]
        return my_recs

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code

        super().save(*args, **kwargs)
