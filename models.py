from peewee import Model, PostgresqlDatabase, AutoField, CharField
import os

db = PostgresqlDatabase(None)

class ImageMetadata(Model):
    id = AutoField()
    filename = CharField(unique=True)
    filepath = CharField(unique=True)

    class Meta:
        database = db