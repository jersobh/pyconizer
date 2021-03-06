#!/usr/bin/env python
# encoding: utf-8
"""
controller.py
"""
from views import render
from models import gen
from models import models
import face_recognition

def index(request):
    img1 = "views/static/img/1.jpg"
    img2 = "views/static/img/2.jpg"
    img3 = "views/static/img/3.jpg"
    known_image = face_recognition.load_image_file(img1)
    unknown_image1 = face_recognition.load_image_file(img2)
    unknown_image2 = face_recognition.load_image_file(img3)

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image1)[0]
    unknown_encoding2 = face_recognition.face_encodings(unknown_image2)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    results2 = face_recognition.compare_faces([biden_encoding], unknown_encoding2)

    context = {'compare': results, 'compare2': results2, 'img1': img1, 'img2': img2}
    template = 'index.jinja2'

    #models.Users.create(username='Charlie') #my example has USERS table with username field)
    return render.view(request, template, context)

def jsonExample(request):
    data = {}
    data['name'] = 'Jhonny'
    data['surname'] = 'test'
    status = 200
    return render.json(data, status)
