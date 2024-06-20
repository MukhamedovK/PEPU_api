from rest_framework import serializers
from environs import Env

from .models import *

env = Env()
env.read_env()

class ProfileSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Profile.ProfileStatus.choices)

    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = env.str('DOMEN') + instance.image.url

        return redata
    

class BranchSerializer(serializers.ModelSerializer):
    branch_manager = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = Branches
        fields = '__all__'


