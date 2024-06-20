from rest_framework import serializers

from .models import *


class OrderSerializer(serializers.ModelSerializer):
    payment = serializers.ChoiceField(choices=PaymentChoice.choices)
    status = serializers.ChoiceField(choices=OrderStatusChoice.choices)
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["on_order"] = datetime.strftime(instance.on_order, "%a, %d %b %Y, %I:%M %p")
        if instance.delivering:
            redata["delivering"] = datetime.strftime(instance.delivering, "%a, %d %b %Y, %I:%M %p")
        if instance.order_delivered:
            redata["order_delivered"] = datetime.strftime(instance.order_delivered, "%a, %d %b %Y, %I:%M %p")
        if instance.payment_success:
            redata["payment_success"] = datetime.strftime(instance.payment_success, "%a, %d %b %Y, %I:%M %p")

        return redata
    

class OrderProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    class Meta:
        model = OrderProduct
        fields = '__all__'


