from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Notes, Colors, Tags, Categories, Images
from .serializers import NotesSerializer, ColorsSerializer
from .serializers import TagsSerializer, CategoriesSerializer, ImagesSerializer
from .tasks import SingUpTask

from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import redirect


@permission_classes((IsAuthenticated, ))
class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)


@permission_classes((IsAuthenticated, ))
class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


@permission_classes((IsAuthenticated, ))
class ColorsList(generics.ListCreateAPIView):
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


@permission_classes((IsAuthenticated, ))
class ColorsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


@permission_classes((IsAuthenticated, ))
class TagsList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

    def get_queryset(self):
        return Tags.objects.filter(author=self.request.user)


@permission_classes((IsAuthenticated, ))
class TagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


@permission_classes((IsAuthenticated, ))
class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        return Categories.objects.filter(author=self.request.user)


@permission_classes((IsAuthenticated, ))
class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


# For redirect if not Auth
class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/auth/login/')


class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'note/note.html'


@permission_classes((IsAuthenticated, ))
class ImagesList(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

    def post(self, request, format=None):
        print request.FILES['select_file']
        serializer = ImagesSerializer(
            data={
                'img_dir': request.FILES['select_file'],
                'title': request.POST['title'],
                'author': request.user.id
            })
        # serializer = ImagesSerializer(data=request.data, files=request.FILES)
        if serializer.is_valid():
            SingUpTask.delay()
            serializer.save()
            print 'SUCCESS'
        else:
            print serializer.errors

        # return Response(status=status.HTTP_201_CREATED).render()
        return redirect('/')

    def get_queryset(self):
        return Images.objects.filter(author=self.request.user)


@permission_classes((IsAuthenticated, ))
class ImagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

    def get_object(self, pk, author):
        try:
            return Images.objects.get(pk=pk, author=author)
        except Images.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk, request.user)
        serializer = ImagesSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        image = self.get_object(pk, request.user)
        serializer = ImagesSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = self.get_object(pk, request.user)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
