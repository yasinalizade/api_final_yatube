from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, FollowSerializer
from .serializers import GroupSerializer, PostSerializer


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.all()
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        return queryset.filter(post=post)

    def perform_create(self, serializer, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        return serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
