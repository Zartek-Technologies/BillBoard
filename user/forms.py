from django import forms
from boards.models import BillBoard
from boards.choices import *

class BillBoardForm(forms.ModelForm):
    facingDirection = forms.ChoiceField(label='facingDirection',widget=forms.Select, choices=DIRECTION_CHOICES)
    
    class Meta:
        model = BillBoard
        fields = ['boardId','imglink','facingDirection','height','width','latitude','longitude','city','sqfeetSize','backLight','available']

class BillBoardUpdateForm(forms.ModelForm):
    facingDirection = forms.ChoiceField(label='facingDirection',widget=forms.Select, choices=DIRECTION_CHOICES)
    class Meta:
        model = BillBoard             
        fields = ['imglink','boardId','facingDirection','height','width','latitude','longitude','city','sqfeetSize','backLight','available']
        