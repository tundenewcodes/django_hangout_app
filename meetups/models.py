from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}  ({self.address})'

class Participants(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length = 200)
    organizer_email = models.EmailField()
    date = models.DateTimeField()
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True) # not compulsorily to be filled
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #onetomany
    participant = models.ManyToManyField(Participants, blank=True, null=True) #if you dont get a value , null will be stored
    #this functions redefines meetup list names in admin
    def __str__(self):
        return f'{self.title} - {self.slug}'