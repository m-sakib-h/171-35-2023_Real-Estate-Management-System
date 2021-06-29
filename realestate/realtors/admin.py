from django.contrib import admin
from realtors.models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    class Meta:                              #Model Meta is basically the inner class of your model class. Model Meta is
        model = Realtor                     #basically used to change the behavior of your model fields like changing order
                                            #options,verbose_name and lot of other options.
                                             #It's completely optional to add Meta class in your model.

    list_display = ['id', 'name', 'email', 'phone', 'is_mvp', ]
    list_display_links = ['id', 'name', ]
    list_filter = ('name',)
    list_editable = ('phone', 'is_mvp',)
    search_fields = ('name', 'email',)
    list_per_page = 3


# Register your models here.
admin.site.register(Realtor, RealtorAdmin)