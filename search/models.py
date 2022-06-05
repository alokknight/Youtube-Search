from django.db import models
# from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class SearchdataModel(models.Model):
    index       =models.IntegerField(default=0,unique=True)
    title       =models.CharField(max_length=1000,primary_key=True)
    channelTitle=models.CharField(max_length=1000,default='#')
    desc        =models.TextField()
    duration    =models.CharField(max_length=12,  default='#')
    videoURL    =models.CharField(max_length=1000,default='#')
    thumbURL    =models.CharField(max_length=1000,default='#')
    publishTime =models.DateTimeField(default=now, blank=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = SearchdataModel.objects.all().aggregate(largest=models.Max('index'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.index = last_id + 1

        super(SearchdataModel, self).save(*args, **kwargs)