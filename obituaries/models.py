from django.db import models
from django.utils import timezone

class Obituary(models.Model):
    title = models.CharField(max_length=255, default='Default Title')
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now)
    custom_id = models.CharField(max_length=20, unique=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.custom_id:  # Check if custom_id is None or empty
            last_obituary = Obituary.objects.order_by('-submission_date').first()
            if last_obituary and last_obituary.custom_id:
                last_number = int(last_obituary.custom_id.split('-')[-1])
            else:
                last_number = 0  # Default to 0 if no previous records
            new_number = last_number + 1
            self.custom_id = f"OB-{new_number:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
