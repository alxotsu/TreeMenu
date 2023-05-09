from django.db import models
from django.core.exceptions import ValidationError


class MenuItem(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", null=True, blank=True)

    class Meta:
        unique_together = ('name', 'menu')

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.parent_id is not None and self.menu_id != self.parent.menu_id:
            raise ValidationError(f"Menu items cannot have parent from another menu")
        return super(MenuItem, self).save(force_insert, force_update, using, update_fields)
