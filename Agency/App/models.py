from django.db import models

# Prevent duplicated emails

class Registered_emails(models.Model):
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.email
