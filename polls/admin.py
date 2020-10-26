from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Questionnaire, QuestionInQuestionnaire,UserProfile

admin.site.site_header = "HR project"
admin.site.site_title = "HR project Administation area"
admin.site.index_title = "Welcome to the HR project Administation area"

class UserProfileAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['user']}),
	(None, {'fields': ['raiting']})]

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_text']}),
	(None, {'fields': ['img']}),(None, {'fields': ['type_of']}),
	(None, {'fields': ['pub_date']}),
	(None, {'fields': ['start_date']})]
	inlines = [ChoiceInline]

class QuestionInQuestionnaireInline(admin.TabularInline):
	model = QuestionInQuestionnaire
	extra = 0

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['questionnaire_text']}), (None, {'fields': ['pub_date']}),
	(None, {'fields': ['start_date']})]
	inlines = [QuestionInQuestionnaireInline]
# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile)
