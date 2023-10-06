from django.forms import ModelForm
from .models import Take

class TakeForm(ModelForm):
    class Meta:
        model = Take
        fields = ["title","themes","rating","description"]
