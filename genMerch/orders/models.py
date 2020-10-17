from django.db import models
from django.utils.functional import cached_property

from customers import models as customers_models
from products import models as products_models
from main import models as main_models


class Order(main_models.SoftDeletionModel):
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    customer = models.ForeignKey(
        to=customers_models.Customer, on_delete=models.CASCADE, blank=True, null=True
    )
    payment_received = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer if self.customer else self.id}"  # pylint: disable=no-member

    @cached_property
    def total(self) -> float:
        total = 0

        for order_item in self.order_items:  # pylint: disable=no-member
            total += order_item.product.price * order_item.quantity

        return total

    @cached_property
    def is_paid(self) -> bool:
        return self.payment_received == None


class OrderItem(main_models.SoftDeletionModel):
    product = models.ForeignKey(to=products_models.Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)

    class Meta:
        default_related_name = "order_items"


class OrderProduct(main_models.SoftDeletionModel):
    product_id = models.ForeignKey(to=products_models.Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "OrderProduct"


class Cart(main_models.SoftDeletionModel):
    product_id = models.ForeignKey(to=products_models.Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "Cart"
