from django.contrib import admin

# Register your models here.
from .models import * #import all models from current directory
# Register your models here.
#Solution1
class MemberAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publication_date', 'is_available')
admin.site.register(Member, MemberAdmin)

