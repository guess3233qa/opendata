from django.db import models

# Create your models here.

class Poll(models.Model):

	def _unicode_(self):
		return self.question

	def was_published_today(self):
		return self.pub_data.data() == datetime.date.today()

	question = models.CharField(max_length=200)
#        pub_date = models.DateTimeField('date published')

class Choice(models.Model):

	def _unicode_(self):
                return self.choice

	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
