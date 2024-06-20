from django.db import models
from datetime import datetime

from products.models import Product


class PaymentChoice(models.TextChoices):
    WITH_CARD = "Оплата картой", "card"
    CLICK = "Click", "click"
    PAYME = "Payme", "payme"
    CASH = "Наличными", "by_cash"


class OrderStatusChoice(models.TextChoices):
    PAYMENT_SUCCESS = "Оплата прошла успешно!", "success"
    ON_ORDER = "Заказ подготавливается", "on_order"
    DELIVERED = "Доставлен", "delivered"
    DELIVERING = "Доставляется", "delivering"


class Order(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    payment = models.CharField(max_length=200, choices=PaymentChoice.choices, default=PaymentChoice.CASH)
    status = models.CharField(max_length=200, choices=OrderStatusChoice.choices, default=OrderStatusChoice.ON_ORDER)
    total_price = models.IntegerField()

    payment_pending = models.BooleanField(default=False)
    payment_success = models.DateTimeField(null=True, blank=True)
    on_order = models.DateTimeField(null=True, blank=True)
    delivering = models.DateTimeField(null=True, blank=True)
    order_delivered = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == OrderStatusChoice.PAYMENT_SUCCESS and not self.payment_success:
            self.payment_success = datetime.now()
        if self.status == OrderStatusChoice.ON_ORDER and not self.on_order:
            self.on_order = datetime.now()
        if self.status == OrderStatusChoice.DELIVERING and not self.Delivering:
            self.Delivering = datetime.now()
        if self.status == OrderStatusChoice.DELIVERED and not self.order_delivered:
            self.order_delivered = datetime.now()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.email}"


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Заказ №{self.order.id}"
