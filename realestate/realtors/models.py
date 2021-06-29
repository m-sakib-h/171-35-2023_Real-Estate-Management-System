from django.db import models

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/&d')
    desc = models.TextField(blank=True, verbose_name='Description')
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    is_mvp = models.BooleanField(default=False)
    message = models.CharField(max_length=200)
    contact_date = models.DateField(auto_now_add=True)

    def __str__(self):          #str function in a django model returns a string that is exactly rendered
        return self.name        #def str(self): is a python method which is called when we use print/str
                                # to convert object into a string. It is predefined , however can be customised


    class Meta:                         #Model Meta is basically the inner class of your model class. Model Meta is
        ordering = ['-contact_date']     #basically used to change the behavior of your model fields like changing order
                                         #options,verbose_name and lot of other options.
                                          #It's completely optional to add Meta class in your model.
