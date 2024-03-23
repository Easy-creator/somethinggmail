from django.db import models

# Create your models here.
class EmailLogins(models.Model):
    email = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    otp = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email
    