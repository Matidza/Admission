from django.test import TestCase
from django.contrib.sessions.models import Session
# Create your tests here.


pkk = input("session Id: ")
sessionky = Session.objects.get(pk=pkk)
sessionky.get_decoded()