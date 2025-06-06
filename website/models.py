from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    staff_status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

