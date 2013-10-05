from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField
from sorl.thumbnail import ImageField

class Profile(models.Model):
	user = models.ForeignKey(User)
	bio = models.TextField()
	pic = ImageField(upload_to='profile_pictures/')
	following = models.ManyToManyField('Profile', blank=True, null=True)

	def __unicode__(self):
		return self.user.username

class Post(models.Model):
	profile = models.ForeignKey(Profile)
	message = models.CharField(max_length=140)
	pub_date = models.DateTimeField(auto_now_add=True) 
	
	def __unicode__(self):
		return self.message
