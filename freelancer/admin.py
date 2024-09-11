from django.contrib import admin
from . import models
# Register your models here.
class SkillsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('skill_name',),}
admin.site.register(models.Skills, SkillsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',),}
admin.site.register(models.Category, CategoryAdmin)

admin.site.register(models.Freelancer)
admin.site.register(models.Portfolio)