# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request, 'upload/form.html')

def upload(request):
    for count, x in enumerate(request.FILES.getlist('files')):
        def handle_uploaded_file(f):
            with open('/' + str(count), 'wb') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        handle_uploaded_file(x)
    return HttpResponse('File(s) uploaded!')
