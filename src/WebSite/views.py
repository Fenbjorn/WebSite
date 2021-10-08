from django.shortcuts import render



def index(request):
    return render(request, 'WebSite/index.html')


def pages(request, other_pages):
    return render(request, f'WebSite/{other_pages}.html')


