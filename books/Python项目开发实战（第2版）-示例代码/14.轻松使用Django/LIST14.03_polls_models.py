# -*- coding: utf-8 -*-
from django.db import models

class Poll(models.Model):
    question_text = models.CharField(max_length=200)
