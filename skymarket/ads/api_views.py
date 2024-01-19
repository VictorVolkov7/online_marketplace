from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .filters import AdTitleFilter
from .models import Ad, Comment
from .pagination import AdPagination
from .permissions import IsOwner, IsAdmin
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer, CommonDetailSerializer, \
    CommonDetailAndStatusSerializer


@extend_schema(tags=["Ad"])
@extend_schema(
    summary="API endpoint for viewing the Ad list.",
    responses={
        status.HTTP_200_OK: AdSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
    }
    )
class AdListAPIView(generics.ListAPIView):
    """
    API endpoint for viewing the Ad list.
    """
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdTitleFilter
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


@extend_schema(tags=["Ad"])
@extend_schema(
    summary="API endpoint for viewing the Ad detail.",
    responses={
        status.HTTP_200_OK: AdDetailSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
    }
    )
class AdDetailAPIView(generics.RetrieveAPIView):
    """
    API endpoint for viewing the Ad detail.
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Ad"])
@extend_schema(
    summary="API endpoint for creating the Ad.",
    responses={
        status.HTTP_201_CREATED: AdSerializer,
        status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
    }
    )
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


@extend_schema(tags=["Ad"])
@extend_schema(
    summary="API endpoint for updating the Ad.",
    responses={
        status.HTTP_200_OK: AdDetailSerializer,
        status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
    }
    )
class AdUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint for updating the Ad.
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


@extend_schema(tags=["Ad"])
@extend_schema(
    summary="API endpoint for deleting the Ad.",
    responses={
        status.HTTP_204_NO_CONTENT: '',
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
    }
    )
class AdDeleteAPIView(generics.DestroyAPIView):
    """
    API endpoint for deleting the Ad.
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


# Comments generics
@extend_schema(tags=["Comment"])
@extend_schema(
    summary="API endpoint for viewing the Comment list.",
    responses={
        status.HTTP_200_OK: CommentSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
    }
    )
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


@extend_schema(tags=["Comment"])
@extend_schema(
    summary="API endpoint for viewing the Comment detail.",
    responses={
        status.HTTP_200_OK: CommentSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
        status.HTTP_405_METHOD_NOT_ALLOWED: CommonDetailSerializer,
    }
    )
class CommentDetailAPIView(generics.RetrieveAPIView):
    """
    API endpoint for viewing the Comment detail.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'commentId'
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Comment"])
@extend_schema(
    summary="API endpoint for creating the Comment.",
    responses={
        status.HTTP_201_CREATED: CommentSerializer,
        status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
    }
    )
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


@extend_schema(tags=["Comment"])
@extend_schema(
    summary="API endpoint for updating the Comment.",
    responses={
        status.HTTP_200_OK: CommentSerializer,
        status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
    }
    )
class CommentUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint for updating the Comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'commentId'
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


@extend_schema(tags=["Comment"])
@extend_schema(
    summary="API endpoint for deleting the Comment.",
    responses={
        status.HTTP_201_CREATED: AdDetailSerializer,
        status.HTTP_400_BAD_REQUEST: CommonDetailSerializer,
        status.HTTP_401_UNAUTHORIZED: CommonDetailSerializer,
        status.HTTP_403_FORBIDDEN: CommonDetailAndStatusSerializer,
        status.HTTP_404_NOT_FOUND: CommonDetailSerializer,
    }
    )
class CommentDeleteAPIView(generics.DestroyAPIView):
    """
    API endpoint for deleting the Comment.
    """
    queryset = Comment.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'commentId'
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
