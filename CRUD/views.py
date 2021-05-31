"""Views fot the bnew app."""
import json
from rest_framework import status

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
import requests
from urllib.parse import urlencode
from django.http import HttpResponse, HttpResponseRedirect, QueryDict

from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import View
from django.shortcuts import render
import logging


from ejemplos.models import *


class TestAPI(View):
    def __init__(self):
        pass

    def get(self, request, *args, **kwargs):
        print("get")
        if request.GET.get('flag'):
            gente = Profile.objects.all()
            data = []
            for value in gente:
                data.append({"id":value.id,"phone":value.phone,"direccion":value.direction})

            return HttpResponse(json.dumps({'code':200,'message':data}, cls=DjangoJSONEncoder), content_type='application/json')

        return render(request, 'alfonso.html', {})

    def post(self, request, *args, **kwargs):
        try:
            print("post",request.POST)
            gente = Profile.objects.all()
            for value in gente:
                print("Email",value.email)

            data = {
                "phone":request.POST.get('phone'),
                "direction":request.POST.get('direction'),
                "localphone":request.POST.get('localphone'),
            }
            new_user = Profile(**data)
            new_user.save()
            return HttpResponse(json.dumps({'code':400,'message':'se guardo bien'}, cls=DjangoJSONEncoder), content_type='application/json')
            # return render(request, 'alfonso.html', {})
        except Exception as e:
            print('error',e)
            return HttpResponse({"message": "Error", "code":500},cls=DjangoJSONEncoder,content_type='application/json')


    def put(self, request, *args, **kwargs):
        request.POST=QueryDict(request.read())
        print("put",request.POST)
        gente = Profile.objects.get(id=int(request.POST.get('id')))
        gente.phone = request.POST.get('phone')
        gente.save()
        return HttpResponse(json.dumps({'code':200,'message':'se guardo bien'}, cls=DjangoJSONEncoder), content_type='application/json')
