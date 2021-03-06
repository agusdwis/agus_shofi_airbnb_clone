# Generated by Django 3.0.5 on 2020-04-12 05:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0025_auto_20200412_0323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['created_at']},
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='review_by_user_id',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='status',
        ),
        migrations.AddField(
            model_name='reviews',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reviews',
            name='name',
            field=models.CharField(default=datetime.datetime(2020, 4, 12, 5, 19, 51, 496539, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='property_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_reviews', to='container.Dwelling'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 4, 12, 5, 20, 30, 182103, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
