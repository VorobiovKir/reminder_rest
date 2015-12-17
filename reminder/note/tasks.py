from celery.registry import tasks
from celery.task import Task


class SingUpTask(Task):

    def run(self):
        print 'Its work!'

tasks.register(SingUpTask)
