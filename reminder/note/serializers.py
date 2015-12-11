from rest_framework import serializers
from .models import Notes, Tags, Categories, Colors, Images
# from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')


class TagsSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tags
        fields = ('id', 'name', 'author')


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('id', 'name')


class CategoriesSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Categories
        fields = ('id', 'name', 'author')


class ImagesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Images
        fields = ('id', 'title', 'img_dir', 'author')


class NotesSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    # tag = TagsSerializer(many=True, read_only=True)
    # category = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Notes
        fields = ('id', 'title', 'context', 'pub_date',
                  'color', 'tag', 'category', 'author', 'tag', 'image')
