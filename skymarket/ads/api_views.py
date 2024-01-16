from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Ad, Comment
from .pagination import AdPagination
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdListAPIView(generics.ListAPIView):
    """
    API endpoint for viewing the Ad list.
    """
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Returns the queryset with filter if 'me' in url path.
        Otherwise returns all Ads.
        """
        if 'me' in self.request.path:
            return Ad.objects.filter(author=self.request.user)
        else:
            return Ad.objects.all()


class AdDetailAPIView(generics.RetrieveAPIView):
    """
    API endpoint for viewing the Ad detail.
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class AdCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for creating the Ad.
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Creating an ad with the author assigned to the current user.
        """
        ad = serializer.save()
        ad.author = self.request.user
        ad.save()


class AdUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint for updating the Ad.
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class AdDeleteAPIView(generics.DestroyAPIView):
    """
    API endpoint for deleting the Ad.
    """
    queryset = Ad.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


# Comments generics
class CommentListAPIView(generics.ListAPIView):
    """
    API endpoint for viewing the Comment list.
    """
    serializer_class = CommentSerializer
    lookup_field = 'ad_pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retrieve the Comment with filtering by id.
        """
        return Comment.objects.filter(ad=self.kwargs.get('id'))


class CommentDetailAPIView(generics.RetrieveAPIView):
    """
    API endpoint for viewing the Comment detail.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'commentId'
    permission_classes = [IsAuthenticated]


class CommentCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for creating the Comment.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Creating an ad with the author assigned to the current user and current ads.
        """
        comment = serializer.save()
        comment.author = self.request.user
        comment.ad = Ad.objects.get(id=self.kwargs.get('id'))
        comment.save()


class CommentUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint for updating the Comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'commentId'
    permission_classes = [IsAuthenticated]


class CommentDeleteAPIView(generics.DestroyAPIView):
    """
    API endpoint for deleting the Comment.
    """
    queryset = Comment.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'commentId'
    permission_classes = [IsAuthenticated]
