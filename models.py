from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey('self', null=True, blank=True, related_name='sub_categories')

    def __unicode__(self):
        return self.title

class Item(models.Model):
    """ Any item at all that can be touched """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='stock_images', null=True, blank=True)
    number_in_stock = models.SmallIntegerField(default=1)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return str(self.number_in_stock) + ' x ' + self.title

    def delete(self):
        # This will delete the image flat file when Item is deleted.
        # Without a lot of work, there doesn't seem to be a way to delete
        # the flat file if a new one is being uploaded in it's place.
        self.image.delete()
        super(Item, self).delete()

