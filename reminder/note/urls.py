from django.conf.urls import url, include

from note import views

urlpatterns = [
    url(r'^notes/$', views.NotesList.as_view(), name='notes'),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.NotesDetail.as_view(), name='note'),
    url(r'^colors/$', views.ColorsList.as_view(), name='colors'),
    url(r'^colors/(?P<pk>[0-9]+)/$',
        views.ColorsDetail.as_view(), name='color'),
    url(r'^tags/$', views.TagsList.as_view(), name='tags'),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagsDetail.as_view(), name='tag'),
    url(r'^categories/$', views.CategoriesList.as_view(), name='categories'),
    url(r'^categories/(?P<pk>[0-9]+)/$',
        views.CategoriesDetail.as_view(), name='category'),
    url(r'^images/(?P<pk>[0-9]+)/$',
        views.ImagesDetail.as_view(), name='images'),
    url(r'^images/', views.ImagesList.as_view(), name='image'),
    url(r'^$', views.MainPage.as_view(), name='home'),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]
