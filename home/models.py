from django.db import models

from django_resized import ResizedImageField


class Post(models.Model):
    """
    Creates card posts for board
    """

    author_name = models.CharField(max_length=80)
    body = models.TextField(null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="laura_board_posts/",
        force_format="WEBP",
        default="",
    )
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.author_name)
