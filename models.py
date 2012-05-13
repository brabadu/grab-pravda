# -*- coding: utf-8 -*-
"""
Models for default project
"""
import datetime

from mongoengine import (connect, DynamicDocument, StringField, DateTimeField,
    URLField, BooleanField, IntField, ListField)

connect('pravda')


class Post(DynamicDocument):
    source = StringField(required=True)

    title = StringField(required=True)
    content = StringField(required=True)
    url = URLField()
    tags = ListField()

    images = ListField()
    links = ListField()

    published_date_str = StringField()
    published_date = DateTimeField()
    grabbed_date = DateTimeField(default=datetime.datetime.now)

    processed = ListField()

    title_red = BooleanField()
    title_bold = BooleanField()
    title_uppercased = BooleanField()
    has_photo = BooleanField()
    has_video = BooleanField()
    updated = BooleanField()
    comments_number = IntField()
