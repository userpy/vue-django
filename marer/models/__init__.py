from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt import models as mptt_models
from mptt.fields import TreeForeignKey

from marer.models.base import *
from marer.models.issue import *
from marer.models.issuer import *
from marer.models.user import *


class FinanceOrganization(models.Model):
    name = models.CharField(max_length=512, blank=False, null=False)
    interest_rate = models.FloatField(blank=False, null=False, default=0)
    review_term_days = models.PositiveIntegerField(blank=False, null=False, default=1)


class OKVED2(mptt_models.MPTTModel):
    name = models.CharField(max_length=512, blank=False, null=False)
    code = models.CharField(max_length=32, blank=False, null=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='childrens')


class Region(mptt_models.MPTTModel):
    name = models.CharField(max_length=512, blank=False, null=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='childrens')


class FinanceProductPage(mptt_models.MPTTModel):

    class Meta:
        verbose_name = _('finance product')
        verbose_name_plural = _('finance products')

    name = models.CharField(verbose_name=_('finance product name'), max_length=512, blank=False, null=False)
    parent = TreeForeignKey('self', verbose_name=_('parent product'), null=True, blank=True, related_name='childrens')
    _seo_h1 = models.CharField(verbose_name=_('name on page'), max_length=512, blank=True, null=False, default='')
    _seo_title = models.CharField(verbose_name=_('browser title'), max_length=512, blank=True, null=False, default='')
    _seo_description = models.CharField(
        verbose_name=_('page desctiption'),
        max_length=512,
        blank=True,
        null=False,
        default=''
    )
    _seo_keywords = models.CharField(
        verbose_name=_('page keywords'),
        max_length=512,
        blank=True,
        null=False,
        default=''
    )
    page_content = RichTextField(verbose_name=_('page content'), blank=True, null=False, default='')

    def __str__(self):
        return self.name

    def get_seo_h1(self):
        return self._seo_h1 if self._seo_h1 != '' else self.name

    def get_seo_title(self):
        return self._seo_title if self._seo_title != '' else self.name

