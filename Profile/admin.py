from django.contrib import admin
from .models.profile import Profile
from .models.social_acc_model import Social

admin.site.register(Profile)
admin.site.register(Social)
# Register your models here.
