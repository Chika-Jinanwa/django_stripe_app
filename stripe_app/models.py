import datetime
from datetime import date
from django.db import models
from django.urls import reverse
import uuid


class User(models.Model):
    paid_until = models.DateField(
        null=True,
        blank=True
    )

    def set_paid_until(self, date_or_timestamp):
        if isinstance(date_or_timestamp, int):
            # input date as timestamp integer
            paid_until = date.fromtimestamp(date_or_timestamp)
        elif isinstance(date_or_timestamp, str):
            # input date as timestamp string
            paid_until = date.fromtimestamp(int(date_or_timestamp))
        else:
            paid_until = date_or_timestamp

        self.paid_until = paid_until
        self.save()

    def has_paid(
        self,
        current_date=datetime.date.today()
    ):
        if self.paid_until is None:
            return False

        return current_date < self.paid_until


class Product(models.Model):

    title = models.CharField(max_length=30)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )

    class Meta:
        verbose_name = "Premium Product"
        verbose_name_plural = "Premium Products"

    def __str__(self):
        return f"{self.title}"


