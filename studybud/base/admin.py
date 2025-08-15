from django.contrib import admin

# Register your models here.
from .models import Topic, Message, Room 

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)