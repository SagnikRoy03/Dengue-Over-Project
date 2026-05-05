from rest_framework import serializers
from DENGUE_APP.models import Doctor


class DoctorSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"