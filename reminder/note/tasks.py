from __future__ import absolute_import
from reminder.celery import app
from celery.registry import tasks

@app.task
def test(param):
    print 'Hello'

tasks.register(test)
