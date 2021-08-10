from django.contrib import admin
from polls.models import *

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceTable(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    search_fields = ['question_text']
    list_filter = ['pub_date']
    fieldsets = [
        ('Question Info', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceTable]
    
admin.site.register(Question, QuestionAdmin)