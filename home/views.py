from django.views.generic import TemplateView

from .models import Post


class Index(TemplateView):
    template_name = "home/index.html"
