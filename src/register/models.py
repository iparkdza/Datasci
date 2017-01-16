from django.db import models

# Create your models here.
class register(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	username = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)
	firstName = models.CharField(max_length=100, blank=True, null=True)
	lastName = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	birthdate = models.DateField(blank = True, null = True)
	gender  = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True )	
	score = models.IntegerField(default=0, null=True)
	
	def __unicode__(self):
		return str(self.username)