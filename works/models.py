from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='companies_logos')
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    web_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Work(models.Model):
    proform = models.ForeignKey('documents.Proform',
                                related_name='works')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
