from django.contrib import admin
from home.models import Contact

# Register your models here.
@admin.register(Contact)
# @admin.register(User)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')  # Optional: customize admin list view
