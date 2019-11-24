from django.contrib import admin
from .models import Store
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

admin.site.register(Store)
