from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.response import TemplateResponse
import os

@login_required
def camera(request):
    image_ready = os.path.exists('/tmp/photo.jpg')
    response = TemplateResponse(request, 'camera/index.html', {
        'image_ready': image_ready
    })

    return response

@login_required
def image(request):
    if os.path.exists('/tmp/photo.jpg'):
        image_data = open('/tmp/photo.jpg', 'rb').read()
        return HttpResponse(image_data, mimetype='image/jpeg')