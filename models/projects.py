from django.db import models

def upload_profile_location(self,filename):
    
    return 'Profile/static/%s/%s' % ('picture', filename)

class Projects(models.Model):
    project_image = models.ImageField(null = True,upload_to=upload_profile_location)
    project_name = models.CharField(null = True,max_length=50)
    project_link = models.URLField(null = True,max_length=255)

    def __str__(self):
        return str(self.project_name)
