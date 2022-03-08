from django.contrib import admin

# Register your models here.
from .models import Articles, Categories, Trials, Sources, Entities

# this class define which department columns will be shown in the department admin web site.
class ArticleAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['article_id', 'title']

class TrialAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['trial_id', 'title']

class SourceAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name','subject']

admin.site.register(Articles,ArticleAdmin)
admin.site.register(Trials, TrialAdmin)
admin.site.register(Sources,SourceAdmin)
admin.site.register(Categories)
admin.site.register(Entities)