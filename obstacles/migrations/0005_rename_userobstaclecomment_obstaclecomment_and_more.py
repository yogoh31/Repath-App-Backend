# Generated by Django 4.0.2 on 2022-02-25 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obstacles', '0004_alter_obstacle_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserObstacleComment',
            new_name='ObstacleComment',
        ),
        migrations.RenameModel(
            old_name='UserObstacleCommentPhoto',
            new_name='ObstacleCommentPhoto',
        ),
        migrations.AlterField(
            model_name='obstaclephoto',
            name='obstacle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='obstacles.obstacle'),
        ),
    ]
