from django.contrib import admin
from .models import User,Agent,lead
# Register your models here.
admin.site.register(User)
admin.site.register(lead)
admin.site.register(Agent)