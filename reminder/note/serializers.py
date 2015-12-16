from rest_framework import serializers
from .models import Notes, Tags, Categories, Colors, Images


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name', 'author')


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('id', 'name')


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', 'author')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'title', 'img_dir', 'author')


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id', 'title', 'context', 'pub_date',
                  'color', 'tag', 'category', 'author', 'tag', 'image')
