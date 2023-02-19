from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#add slots to write the choices of the question
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] mettre dans l'ordre des questions voulues
    
    #créer des parties dans notre form
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]

    inlines = [ChoiceInLine] #implement choices

    #Pour sélectionner les valeurs qu'on donne dans la liste des questions
    list_display = ("question_text", 'pub_date', "was_published_recently")

    #Add a filter for the date attribute
    list_filter = ['pub_date']

    #Add a search bar for the question_text attribute
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

