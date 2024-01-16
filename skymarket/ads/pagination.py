from rest_framework import pagination


class AdPagination(pagination.PageNumberPagination):
    """
    Custom class for pagination for ads.
    """

    page_size = 10  # Number of elements per page
    page_size_query_param = 'page_size'  # Query parameter to specify the number of elements on the page
    max_page_size = 50  # Maximum number of elements per page
