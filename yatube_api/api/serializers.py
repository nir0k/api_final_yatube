from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.shortcuts import get_object_or_404
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.pagination import LimitOffsetPagination


from posts.models import Comment, Post, Group, Follow, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(many=True, required=False)
    pagination_class = LimitOffsetPagination

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author',)

    def create(self, validated_data):
        if 'comments' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post
        comments = validated_data.pop('comments')
        post = Post.objects.create(**validated_data)
        for comment in comments:
            current_comments, status = Comment.objects.get_or_create(
                **comment, post=post)
        return post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='This following already exists.'
            )
        ]

    def validate_following(self, value):
        following = get_object_or_404(User, username=value)
        user = self.context['request'].user
        print(f'user={user}, following={following}')
        if following == self.context['request'].user:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        return following
