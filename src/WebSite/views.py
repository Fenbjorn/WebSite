from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'WebSite/index.html')


def pages(request, other_pages):
    return render(request, f'WebSite/{other_pages}.html')


def open_file(request, *args, **kwargs):
    path = str(kwargs['p'])

    file_path = 'your path'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404