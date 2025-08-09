from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    При наличии параметров limit/offset в запросе работает как
    LimitOffsetPoagination, при их отсутствии возвращает просто список.
    """
    def paginate_queryset(self, queryset, request, view=None):
        query_params = request.query_params
        if 'limit' not in query_params and 'offset' not in query_params:
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)
