# Generated by Django 5.1.1 on 2024-09-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_alter_post_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="color",
            field=models.CharField(
                choices=[
                    ("#FBD1A2", "Sunset"),
                    ("#7DCFB6", "Tiffany Blue"),
                    ("#C2AFF0", "Mauve"),
                    ("#E8F7EE", "Honey Dew"),
                    ("#EFCA08", "Jonquil"),
                    ("#00A6A6", "Light Sea Green"),
                    ("#FF4B3E", "Tomatoe"),
                ],
                default="Sunset",
                max_length=20,
            ),
        ),
    ]
