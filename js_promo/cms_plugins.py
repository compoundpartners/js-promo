# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import Promo


@plugin_pool.register_plugin
class PromoPlugin(CMSPluginBase):
    model = Promo
    name = _('Promo')
    admin_preview = False
    render_template = 'js-promo/promo.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context
