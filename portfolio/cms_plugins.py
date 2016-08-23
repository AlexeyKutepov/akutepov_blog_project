from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PortfolioItem
from django.utils.translation import ugettext_lazy as _


class PortfolioPlugin(CMSPluginBase):
    model = PortfolioItem
    name = _("Portfolio Plugin")
    render_template = "portfolio_item.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(PortfolioPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(PortfolioPlugin)