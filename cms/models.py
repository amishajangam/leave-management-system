from django.db import models

class Notice(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    file = models.FileField(
        upload_to='notices/',
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='notice_images/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title