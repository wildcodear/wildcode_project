from django.db import models
from django.utils.translation import ugettext_lazy as _


class Proform(models.Model):
    CASH = 'cash'
    CREDIT_CARD = 'credit_card'
    NEGOTIABLE = 'negotiable'
    TRANSFER = 'transfer'

    PAYMENT_CONDITIONS = (
        (CASH, _('Cash')),
        (CREDIT_CARD, _('Credit card')),
        (NEGOTIABLE, _('Negotiable')),
        (TRANSFER, _('Transfer')),
    )

    company = models.ForeignKey('works.Company',
                                related_name='proforms_company')
    client = models.ForeignKey('works.Client',
                               related_name='proforms_client')
    created = models.DateTimeField(auto_now_add=True)
    expire_on = models.DateTimeField()
    payment_conditions = models.CharField(max_length=100,
                                          choices=PAYMENT_CONDITIONS)
    total_to_pay = models.FloatField(default=0)

    def __unicode__(self):
        return "%s" % self.id


class Report(models.Model):
    datetime_in = models.DateTimeField()
    machine_data = models.TextField()
    problem = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    observations = models.TextField(blank=True, null=True)
    suggestions = models.TextField(blank=True, null=True)
    datetime_out = models.DateTimeField()
    technical = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.id
