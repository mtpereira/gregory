# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from django.db import models
class Categories(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.TextField(blank=True, null=True)

	# article = models.ManyToManyField('Articles', through='RelArticlesCategories',related_name='article',related_query_name='rel_articles_categories.article_id')

	def __str__(self):
		return self.category_name

	class Meta:
		managed = True
		verbose_name_plural = 'categories'
		db_table = 'categories'


class Articles(models.Model):
	article_id = models.AutoField(primary_key=True)
	title = models.TextField(blank=True, null=True)
	summary = models.TextField(blank=True, null=True)
	link = models.TextField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	source = models.ForeignKey('Sources', models.DO_NOTHING, db_column='source', blank=True, null=True)
	relevant = models.BooleanField(blank=True, null=True)
	ml_prediction_gnb = models.BooleanField(blank=True, null=True)
	ml_prediction_lr = models.BooleanField(blank=True, null=True)
	discovery_date = models.DateTimeField()
	noun_phrases = models.JSONField(blank=True, null=True)
	# category = models.ManyToManyField(Categories, ,related_query_name='rel_articles_categories.category_id')
	sent_to_admin = models.BooleanField(blank=True, null=True)
	sent_to_subscribers = models.BooleanField(blank=True, null=True)
	sent_to_twitter = models.BooleanField(blank=True, null=True)
	categories = models.ManyToManyField(Categories, 
		# through='RelArticlesCategories',
		# through_fields=('article_id', 'category_id'),
		# related_query_name='rel_articles_categories.category_id',
		# related_name='+',
		)
	entities = models.ManyToManyField('Entities')


	def __str__(self):
		return str(self.article_id)

	class Meta:
		managed = True
		unique_together = (('title', 'link'),)
		verbose_name_plural = 'articles'
		db_table = 'articles'


class Entities(models.Model):
	entity = models.TextField()
	label = models.TextField()


	class Meta:
		managed = True
		verbose_name_plural = 'entities'
		db_table = 'entities'



class Sources(models.Model):
	source_id = models.AutoField(primary_key=True)
	name = models.TextField(blank=True, null=True)
	link = models.TextField(blank=True, null=True)
	language = models.TextField()
	subject = models.TextField()
	method = models.TextField()
	

	def __str__(self):
		return self.name

	class Meta:
		managed = True
		verbose_name_plural = 'sources'
		db_table = 'sources'

class Trials(models.Model):
	trial_id = models.AutoField(primary_key=True)
	discovery_date = models.DateTimeField(blank=True, null=True)
	title = models.TextField()
	summary = models.TextField(blank=True, null=True)
	link = models.TextField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	source = models.TextField(blank=True, null=True)
	relevant = models.BooleanField(blank=True, null=True)
	sent = models.BooleanField(blank=True, null=True)
	sent_to_twitter = models.BooleanField(blank=True, null=True)
	sent_to_subscribers = models.BooleanField(blank=True, null=True)

	def __str__(self):
		return str(self.trial_id) 

	class Meta:
		managed = True
		unique_together = (('title', 'link'),)
		verbose_name_plural = 'trials'
		db_table = 'trials'
