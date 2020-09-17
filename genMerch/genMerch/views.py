from django.views.generic import TemplateView
from django.db.models.query import QuerySet


class CustomTemplateView(TemplateView):
    template_name = ''
    queryset = None
    default_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {**context, **self.default_context}

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        context['queryset'] = queryset

        return context
