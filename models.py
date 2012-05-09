# -*- coding: utf-8 -*-
"""
Models for default project
"""
import datetime

from mongoengine import (connect, Document, StringField, DateTimeField,
    URLField, BooleanField, IntField, ListField)

connect('pravda')


class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    url = URLField()
    tags = ListField()

    published_date_str = StringField()
    grabbed_date = DateTimeField(default=datetime.datetime.now)

    title_red = BooleanField()
    title_bold = BooleanField()
    title_uppercased = BooleanField()
    has_photo = BooleanField()
    has_video = BooleanField()
    comments_number = IntField()
