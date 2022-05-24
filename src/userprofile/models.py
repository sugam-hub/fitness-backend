from pickle import TRUE
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
# Create your models here.
User = get_user_model()


class Profile(models.Model):

    firstname = models.CharField(
        _("First Name"), max_length=50, null=True, blank=True)
    lastname = models.CharField(
        _("Last Name"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=50, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=50, null=True, blank=True)
    country = models.CharField(
        _("Country"), max_length=50, null=True, blank=True)
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    bmi = models.CharField(_("BMI"), max_length=50, null=True, blank=True)
    calories = models.CharField(
        _("Calories"), max_length=50, null=True, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=True)
    # photo = models.ImageField(upload_to='media/food-images')

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profile")

    def __str__(self):
        return str(self.id)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)
