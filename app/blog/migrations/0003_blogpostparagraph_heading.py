# Generated by Django 4.2.5 on 2023-10-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpostsnippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostparagraph',
            name='heading',
            field=models.CharField(blank=True, help_text='The heading of the paragraph.', max_length=50),
        ),
    ]