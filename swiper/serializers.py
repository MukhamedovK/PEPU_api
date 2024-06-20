from rest_framework import serializers

from environs import Env

from .models import *

env = Env()
env.read_env()


class ShowcaseSwiperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowcaseSwiper
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['image'] = env.str("DOMEN") + instance.image.url
    

class ClothesSwiperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesSwiper
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['image'] = env.str("DOMEN") + instance.image.url


class ShowcaseSubSwiperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowcaseSubSwiper
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['image'] = env.str("DOMEN") + instance.image.url


