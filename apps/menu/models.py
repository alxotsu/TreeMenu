from django.db import models


class MenuItem(models.Model):
    menu_name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", null=True, blank=True)

    class Meta:
        unique_together = ('name', 'menu_name')

    def __str__(self):
        return self.name
