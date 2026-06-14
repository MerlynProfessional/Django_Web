from django.contrib import admin
from .models import Member_class

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  prepopulated_fields = {"slug": ("firstname", "lastname")}
  
admin.site.register(Member_class, MemberAdmin)