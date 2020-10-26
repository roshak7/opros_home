from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question(models.Model):

	RADIO = 'RADIO'
	CHECKBOX = 'CHECKBOX'
	TYPE_OF_CHOICES = [
		(RADIO, 'Радиокнопка'),
		(CHECKBOX, 'Чекбокс'),
	]
	question_text = models.CharField('Текст вопроса', max_length=200, null=True, blank=True)
	img = models.ImageField('Изображение', blank=True, upload_to='')
	type_of = models.CharField('Выбор варианта', max_length=8, null=True, choices=TYPE_OF_CHOICES, default=RADIO)
	pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
	start_date = models.DateTimeField('Начало теста', auto_now=False, default= timezone.now)

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

	def __str__(self):
		return f'id={self.id} | {self.question_text}'

class Choice(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField('Текст вариантов', max_length=200)
	choice_weight = models.IntegerField('Вес ответа', editable=True, default=0)

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'

	def __str__(self):
		return f'id={self.id} | {self.choice_text}'

class Questionnaire(models.Model):

	questionnaire_text = models.CharField('Название', max_length=200, null=True)
	pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
	start_date = models.DateTimeField('Начало теста', auto_now=False, default= timezone.now)

	class Meta:
		verbose_name = 'Опрос'
		verbose_name_plural = 'Опросы'

	def __str__(self):
		return f'id={self.id} | {self.questionnaire_text}'

class QuestionInQuestionnaire(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question', null=True, verbose_name='Вопрос')
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='questionnaire', verbose_name='Опрос')

	class Meta:
		verbose_name = 'Вопрос в опросе'
		verbose_name_plural = 'Вопросы в опросе'

	def __str__(self):
		return str(f'id={self.id} | {self.questionnaire} / {self.question}')

class UserProfile(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
	raiting = models.IntegerField('Колличество набранных балов', editable=True, default=0)
	
	class Meta:
		verbose_name = 'Статистика пользователя'
		verbose_name_plural = 'Статистика пользователей'

	def __str__(self):
		return str(self.user)