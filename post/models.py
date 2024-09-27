from django.db import models

from cloudinary.models import CloudinaryField

from django.db import models


class Post(models.Model):
    """
    Creates card posts for board
    """
    COLOR_CHOICES = [
        
        ('#FBD1A2', 'Sunset'),  
        ('#7DCFB6', 'Tiffany Blue'),
        ('#C2AFF0', 'Mauve'),
        ('#E8F7EE', 'Honey Dew'),
        ('#EFCA08', 'Jonquil'),
        ('#00A6A6', 'Light Sea Green'),
        ('#FF4B3E', 'Tomatoe'),
    ]


    author_name = models.CharField(max_length=80)
    body = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default="placeholder")
    posted_date = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='Sunset')

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.author_name)
