from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CustomerConfig(AppConfig):
    label = 'customer'
    name = 'oscar.apps.customer'
    verbose_name = _('Customer')