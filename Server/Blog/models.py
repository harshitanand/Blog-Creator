from mongoengine import *

connect('test')

class MetaData(EmbeddedDocument):
    body = StringField()
    author = StringField()

class Post(Document):
    title = StringField()
    body = ListField(StringField())
    author = StringField()
    comments = EmbeddedDocumentListField(MetaData)
    likes = LongField()

