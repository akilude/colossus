# Generated by Django 2.0.6 on 2018-06-07 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0011_email_content_text'),
        ('subscribers', '0007_auto_20180607_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='campaigns.Campaign'),
        ),
    ]