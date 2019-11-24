from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    pass

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='store')

    class Meta:
        default_permissions = ('add',)
        permissions = (('give_refund','Can refund customers'),('can_hire','Can hire employees'),('delete','delete the items'))

    # class Meta:
    #     db_table = 'store'

    def get_absolute_url_detail(self):
        return reverse("stor:detail", kwargs={"pk": self.pk})

    def get_absolute_url_update(self):
        return reverse("stor:update", kwargs={"pk": self.pk})

    def get_absolute_url_delete(self):
        return reverse("stor:delete", kwargs={"pk": self.pk})
