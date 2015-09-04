# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import userena.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(upload_to=userena.models.upload_to_mugshot, help_text='A personal image displayed in your profile.', verbose_name='mugshot', blank=True)),
                ('privacy', models.CharField(verbose_name='privacy', help_text='Designates who can view your profile.', default='registered', choices=[('open', 'Open'), ('registered', 'Registered'), ('closed', 'Closed')], max_length=15)),
                ('nickname', models.CharField(verbose_name='暱稱', default='', max_length=30)),
                ('sex', models.SmallIntegerField(verbose_name='性別', choices=[(0, ''), (1, 'Male'), (2, 'Female')], default=0)),
                ('blood', models.SmallIntegerField(verbose_name='血型', choices=[(0, ''), (1, 'O'), (2, 'A'), (3, 'B'), (4, 'AB')], default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('enable', models.BooleanField(verbose_name='啟用', default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='user_profile')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '會員基本資料',
            },
        ),
    ]
