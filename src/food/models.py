from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Food(models.Model):

    name = models.CharField(_("Food Name"), max_length=50)
    time = models.DurationField(_("Duation"))
    kcal = models.IntegerField(_("K CAL"))
    description = models.TextField(_("Food Description"))
    photo = models.ImageField(upload_to='media/food-images')

    class Meta:
        verbose_name = _("Food")
        verbose_name_plural = _("Foods")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Food_detail", kwargs={"pk": self.pk})
