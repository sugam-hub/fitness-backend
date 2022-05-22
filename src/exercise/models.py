from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Exercise(models.Model):

    name = models.CharField(_("Exercise Name"), max_length=50)
    time = models.CharField(_("Duation"), max_length=50)
    kcal = models.CharField(_("K CAL"), max_length=50)
    bmi_affection_rate = models.FloatField(
        _("BMI Affection Rate"), max_length=10, default=0)
    photo = models.ImageField(upload_to='media/exercise-images')

    # class Meta:
    #     verbose_name = _("Exercise")
    #     verbose_name_plural = _("Exercise")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Exercise_detail", kwargs={"pk": self.pk})
