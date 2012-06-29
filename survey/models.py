from django.db import models

class Survey(models.Model):
    """A class for collecting an entire survey response
    in one object, which will be added to the database."""
    
    drink = models.CharField(max_length=100)
    rating = models.IntegerField()
    drink_comment = models.TextField()
    music = models.TextField()
    change = models.TextField()
    comment = models.TextField()
    
    def __unicode__(self):
        return "Drink %s, rating %s, drink comment %s, music %s, change %s, comment %s" % (self.drink, self.rating, self.drink_comment, self.music, self.change, self.comment)

class HitCount(models.Model):
    """Keeps track of page counts."""
    
    count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return str(self.count)
