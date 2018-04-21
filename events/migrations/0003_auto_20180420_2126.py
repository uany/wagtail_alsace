# Generated by Django 2.0.4 on 2018-04-20 21:26

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('events', '0002_auto_20180420_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, help_text='Name of the event')),
                ('body', wagtail.core.fields.RichTextField(blank=True, verbose_name='Page body')),
                ('date', models.DateTimeField()),
                ('location_name', models.TextField(blank=True, help_text='Name of the location')),
                ('location_address', models.TextField(blank=True, help_text='Address of the location')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.RenameField(
            model_name='eventpage',
            old_name='introduction',
            new_name='seo_description',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='location_address',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='location_name',
        ),
        migrations.AddField(
            model_name='eventpage',
            name='seo_keywords',
            field=models.TextField(blank=True, help_text='Text to describe the page'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='events.Event'),
        ),
    ]