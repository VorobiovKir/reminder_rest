# from celery.task import Task

from celery.registry import tasks
from celery.decorators import task
from PIL import Image


@task()
def to_thumbnail(name_img):
    img = Image.open('media/origin/' + name_img)
    size = (36, 36)
    img.thumbnail(size)
    img.save('media/thumbnail/' + name_img)

tasks.register(to_thumbnail)

# class SingUpTask(Task):

#     def run(self, serializer):
#         print serializer

# tasks.register(SingUpTask)
