from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class Item(Document):
    name = StringField(required=True)
    description = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
