from django.db import models

def upload_profile_location(self,filename):
    
    return 'Profile/static/%s/%s' % ('picture', filename)

class Profile(models.Model):
    picture = models.ImageField(null = True,upload_to=upload_profile_location)
    full_name = models.CharField(max_length=50)
    age= models.IntegerField(null = True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender= models.CharField(max_length=5, choices=GENDER_CHOICES)
    birthday= models.DateField(null = True)
    address=models.CharField(max_length=50)
    school= models.CharField(max_length=50)
    graduate_yr= models.DateField(null=True)
    course= models.CharField(max_length=50)
    
    def __str__(self):
        return self.full_name