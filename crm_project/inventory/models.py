from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator


class CompanyProduct(models.Model):

    name = models.CharField(
        verbose_name=_('نام محصول'),
        max_length=50,
        unique=True)
    
    has_taxation = models.BooleanField(
        verbose_name=_('آیا مشمول مالیات است؟'), 
        default=True)
    
    image_catalog = models.ImageField(
        verbose_name=_('عکس کاتالوگ'), 
        upload_to="media/catalogs/pictures",
        blank=True)

    pdf_catalog = models.FileField(
        verbose_name=_('پی دی اف کاتالوگ'),
        upload_to='media/catalogs/pdfs',
        blank=True,
        validators=[FileExtensionValidator(['pdf'])])

    price = models.PositiveIntegerField(
        verbose_name=_('قیمت'),
        default=0)

    technical_features = models.TextField(
        verbose_name=_('ویژگی های فنی'), 
        max_length=300)

    related_with_manufacturedـproducts = models.ManyToManyField(
        "organization.OrganizationProduct",
        verbose_name=_('قابل استفاده برای تولید محصولات تولیدی')
    )

    def __str__(self) -> str:
        return self.name
