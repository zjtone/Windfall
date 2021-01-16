import time
import random
from django import forms
from rest_framework import status
from rest_framework.response import Response
from assistant.api.apiviews import MyAPIView


class UploadFileForm(forms.Form):
    file = forms.FileField()


def gen_name(name):
    return "./upload/" + str(random.randint(1000, 1000000)) + "_" + str(time.time()) + "_" + name


def handle_uploaded_file(name, f):
    filename = gen_name(name)
    print("filename = {}".format(filename))
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename


class FileApi(MyAPIView):

    def get(self, request):
        pass

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = handle_uploaded_file(str(request.FILES['file']), request.FILES['file'])
            return Response(filename, status=status.HTTP_200_OK)
        return Response("error", status=status.HTTP_400_BAD_REQUEST)
