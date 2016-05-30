from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

@login_required
def photo(request):
    response = TemplateResponse(request, 'index.html', {})

    return response