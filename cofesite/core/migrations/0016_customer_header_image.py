# Generated by Django 4.0 on 2022-01-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_blog_body_alter_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
