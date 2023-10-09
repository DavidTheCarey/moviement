from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Take


class TakeForm(ModelForm):
    class Meta:
        model = Take
        style_classes = "form-control my-2"
        fields = ["title","themes","rating","description"]
        widgets = {
            'title':  TextInput(attrs={
                'class': style_classes,
            }),
            'themes':  TextInput(attrs={
                'class': style_classes,
            }),
            'themes':  TextInput(attrs={
                'class': style_classes,
            }),
            'rating':  NumberInput(attrs={
                'class': style_classes,
                'max': 10,
                'min': 0
            }),
            'description':  Textarea(attrs={
                'class': style_classes,
            }),
        }
