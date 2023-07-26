from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = market_image
        fields = ['name', 'Mfg','market_sample_img','receivedate']

class TestsampleImageForm(forms.ModelForm):
    class Meta:
        model = test_image
        fields = ['receivedno','samplename', 'receivedfrom','Mfg','test_sample_img','receivedate']