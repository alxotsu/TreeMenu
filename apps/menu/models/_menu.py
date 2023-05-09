from django.urls import reverse
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=64, unique=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    is_named = models.BooleanField(default=False)
    named_url_kwargs = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.url is None:
            self.url = "menu_view"
            self.is_named = True
            self.named_url_kwargs = {"menu_name": self.name}
        return super(Menu, self).save(force_insert, force_update, using, update_fields)

    def get_url(self):
        if self.is_named:
            return reverse(self.url, kwargs=self.named_url_kwargs)
        return self.url
