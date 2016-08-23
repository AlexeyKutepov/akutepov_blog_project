from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ServiceItem
from django.utils.translation import ugettext_lazy as _


class ServicePlugin(CMSPluginBase):
    model = ServiceItem
    name = _("Service Plugin")
    render_template = "service_item.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ServicePlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ServicePlugin)