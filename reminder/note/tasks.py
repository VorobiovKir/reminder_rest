from celery.registry import tasks
from celery.task import Task
from celery.decorators import task


@task()
def saveImage(serializer):
    print serializer

# class SingUpTask(Task):

#     def run(self, serializer):
#         print serializer

# tasks.register(SingUpTask)
tasks.register(saveImage)
