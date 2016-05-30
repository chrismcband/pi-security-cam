
from __future__ import absolute_import
import os
from picamera import PiCamera
from time import sleep
from celery import Celery
from django.apps import AppConfig
from django.conf import settings
from PIL import Image as PilImage


if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover


app = Celery('pi_security_cam')


class CeleryConfig(AppConfig):
    name = 'pi_security_cam.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings')
        app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # pragma: no cover


@app.task(bind=True)
def take_photo(self, photo_path=None):
    if not photo_path:
        photo_path = '/tmp/photo.jpg'

    with PiCamera() as camera:
        try:
            camera.start_preview()
            sleep(2)
            camera.capture(photo_path)
            camera.stop_preview()
        finally:
            camera.close()

    im = PilImage.open(photo_path)
    rotated_image = im.rotate(180)
    rotated_image.save(photo_path)
    sleep(2)