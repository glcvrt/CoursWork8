from django.contrib import admin

from users.models import User


@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'is_active',)
    list_filter = ('id',)
