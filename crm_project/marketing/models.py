from django.db import models
from django.core import validators
from django.db.models.expressions import F
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels
from django.contrib.auth import get_user_model


min_length_validator = validators.MinValueValidator(
    limit_value=0, 
    message=("discount can't be negative"))


max_length_validator = validators.MaxValueValidator(
    limit_value=100, 
    message=("discount can't be more than 100"))


class Quote(models.Model):

    owner = models.ForeignKey(
        "organization.Organization",
        on_delete=models.PROTECT,
        verbose_name=_("سازمان"))
    
    creator = models.ForeignKey(
        get_user_model(),
        verbose_name=_("کارشناس ایجاد کننده"),
        on_delete=models.PROTECT,
        default=None
    )

    created_time = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name=_("تاریخ ایجاد پیش فاکتور"))

    def __str__(self):
        return self.owner.organization_name
    
    def sum_all_base_cost(self):
        return self.quoteitem_set.aggregate(
            models.Sum('base_cost')).get('base_cost__sum', 0)
    
    def sum_final_cost(self):
        return self.quoteitem_set.aggregate(
            models.Sum('final_cost_with_discount')).get('final_cost_with_discount__sum', 0)


class QuoteItem(models.Model):

    quote = models.ForeignKey(
        "Quote",
        on_delete=models.CASCADE)

    product = models.ForeignKey(
        'inventory.CompanyProduct',
        on_delete=models.PROTECT
    )

    # product price of item in quote has to be fixed because maybe later we need to change /
    # product price in our company model and we don't want it to change in our item in quote /
    # in otherwords out items in quote that are our quote has to be fixed
    product_price = models.PositiveIntegerField(
        verbose_name=_("قیمت خام محصول"),
        default=0,
    )

    discount = models.FloatField(
        default=0.0,
        verbose_name=_("درصد تخفیف"),
        validators=[
            min_length_validator, 
            max_length_validator
            ]
    )

    quantity = models.PositiveBigIntegerField(
        default=1,
        verbose_name=_("تعداد خرید")
    )

    base_cost = models.PositiveBigIntegerField(
        default=0,
        verbose_name=_("قیمت خام")
    )

    cost_with_taxation = models.PositiveBigIntegerField(
        default=0,
        verbose_name=_("قیمت با مالیات")
    )

    final_cost_with_discount = models.PositiveBigIntegerField(
        default=0,
        verbose_name=_("قیمت نهایی با تخفیف")
    )

    def set_fixed_product_price(self):
        self.product_price = self.product.price

    def calculating_base_cost(self):
        return self.product_price * self.quantity
    
    def calculating_cost_with_taxation(self, base_cost):
        return ((base_cost * 9) / 100) + base_cost
    
    def calculating_discount_amount(self, cost_with_taxation):
        return (cost_with_taxation * self.discount) / 100
    
    def calculating_final_cost_with_discount(self, cost_with_taxation, discount_amount):
        return cost_with_taxation - discount_amount


class QuoteFollowUp(models.Model):

    organization = models.ForeignKey(
        'organization.Organization',
        verbose_name=_("سازمان"),
        on_delete=models.CASCADE
    )

    expert_creator = models.ForeignKey(
        get_user_model(),
        verbose_name=_("کارشناس ایجاد کننده"),
        on_delete=models.PROTECT
    )

    created_time = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name=_("تاریخ ایجاد پیش فاکتور")
    )

    content = models.TextField(
        verbose_name=_('متن پیگیری'),
        max_length=400,
        default=None
    )

    def __str__(self):
        return self.organization.organization_name


class QuoteEmailHistory(models.Model):

    receiver_email_address = models.EmailField(
        verbose_name=_("ایمیل گیرنده")
    )

    was_successfull = models.BooleanField(
        default=False,
        verbose_name=_("ایمیل ارسال شد؟")
    )

    created_time = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name=_("تاریخ ارسال شده")
    )

    user_sender = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name=_("کاربر ارسال کننده")
    )

    def __str__(self):
        return self.receiver_email_address
