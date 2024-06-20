from rest_framework import serializers
from environs import Env

from .models import *

env = Env()
env.read_env()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    sizes = serializers.PrimaryKeyRelatedField(many=True, queryset=Size.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    badge = serializers.ChoiceField(choices=Product.ProductStatus.choices)
    rating = serializers.ChoiceField(choices=Product.RatingChoices.choices)

    class Meta:
        model = Product
        fields = '__all__'


class ProductPhotoSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = ProductPhoto
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['image'] = env.str("DOMEN") + instance.image.url

