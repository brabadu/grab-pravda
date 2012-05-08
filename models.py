# -*- coding: utf-8 -*-
"""
Models for default project
"""
import datetime

from mongoengine import (connect, Document, StringField, DateTimeField,
    URLField, BooleanField)

connect('pravda')


class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    url = URLField()
    published_date = DateTimeField()
    grabbed_date = DateTimeField(default=datetime.datetime.now)

    title_red = BooleanField()
    title_cappitalized = BooleanField()
    title_bold = BooleanField()
    has_photo = BooleanField()
    has_video = BooleanField()
