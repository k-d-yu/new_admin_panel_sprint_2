from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView

from movies.models import Filmwork


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Filmwork.objects.prefetch_related('genres', 'persons').values('id', 'title', 'description',
                                                                                 'creation_date', 'rating', 'type')

        genres_list = ArrayAgg('genres__name', distinct=True)
        actors_list = ArrayAgg('persons__full_name', distinct=True, filter=Q(personfilmwork__role='actor'))
        directors_list = ArrayAgg('persons__full_name', distinct=True,
                                  filter=Q(personfilmwork__role='director'))
        writers_list = ArrayAgg('persons__full_name', distinct=True, filter=Q(personfilmwork__role='writer'))

        return queryset.annotate(genres=genres_list, actors=actors_list, directors=directors_list, writers=writers_list)

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()

        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.paginate_by)
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        return self.object