# -*- coding: UTF-8 -*-
from vicuna import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    login = db.Column(db.String(100))
    nickname = db.Column(db.String(100))
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return '%s(%s)' % (self.nickname, self.username)
