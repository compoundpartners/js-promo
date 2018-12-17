# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Promo(CMSPlugin):
    title = models.CharField(_('title'), max_length=255, blank=True, null=True)
    sub_title = models.CharField(_('sub title'), max_length=255, blank=True, null=True)
    image = FilerImageField(verbose_name=_('image'), null=True, blank=True, related_name="promo_image")
    summary = models.TextField(_('summary'), blank=True, default='')
    link_text = models.CharField(_('link text'), max_length=255, blank=True, null=True)
    link_url = models.CharField(_('link url'), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title or _('Promo')
