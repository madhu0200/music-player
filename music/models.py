from django.db import models

# Create your models here.


class songs(models.Model):
    title=models.CharField(max_length=25)
    template=models.FileField(upload_to='templates/')
    song=models.FileField(upload_to='songs/')
    #image=models.FileField(upload_to='songs/',null=True)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'song'
