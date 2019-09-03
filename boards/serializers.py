from rest_framework import serializers
from .models import BillBoard
from app.models import contact_tble

class BoardSerializer(serializers.ModelSerializer):
     class Meta:
        model = BillBoard        
        fields = ('boardId','imglink','facingDirection','height','width','latitude','longitude','city','sqfeetSize','backLight','available')

class citySerializer(serializers.ModelSerializer):
     class Meta:
        model = BillBoard        
        fields = ('city','backLight','available')

class contactSerializer(serializers.ModelSerializer):
     class Meta:
        model = contact_tble        
        fields = ('boardId','Name','number')

          #  fields = ('boardId',)