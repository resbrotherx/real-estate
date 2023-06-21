from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=100)
    overview = models.TextField(default='False')
    description = models.TextField(default='False')
    timestamp = models.DateTimeField(blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    item_created_date = models.DateField(auto_now=True)

    def __str__(self): 
        return f'{self.title} - {self.pk}'

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'pk': self.pk
        })

class value(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    overview = models.TextField(default='False')
    timestamp = models.DateTimeField(blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    item_created_date = models.DateField(auto_now=True)

    def __str__(self): 
        return f'{self.title} - {self.pk}'

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'pk': self.pk
        })



class vlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(default='False')
    timestamp = models.DateTimeField(blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    item_created_date = models.DateField(auto_now=True)

    def __str__(self): 
        return f'{self.title} - {self.pk}'
    


class BlogArticle(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	image = models.ImageField(default=False)
	little_discription = models.TextField(default=False)
	discription = models.TextField()
	futured = models.BooleanField(default=False)
	popular = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)
	# dislikes=models.ManyToManyField(User, related_name="q_disliked", blank=True)
	date_updated = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('news_detail', kwargs={
	# 		'id': self.id
	# 	})
	def get_absolute_url(self):
		return reverse('new:news_detail', args=[self.id])

class vlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    item_created_date = models.DateField(auto_now=True)

    def __str__(self): 
        return f'{self.title} - {self.pk}'