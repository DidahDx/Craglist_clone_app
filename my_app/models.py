from django.db import models


# Create your models here.
# Models are for databases
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        # used to return the string of the actual search object
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural= 'Searches'