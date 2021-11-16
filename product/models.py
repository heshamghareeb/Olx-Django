from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    Status_Type =(
    ('New','New'),
    ('Used','Used'),
    )
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=100, choices=Status_Type)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='main_product/', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now,verbose_name=_("Created At"))
    slug = models.SlugField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})


class ProductImages (models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    class Meta:
        verbose_name = _("Produc Image")
        verbose_name_plural = _("Produc Images")

    def __str__(self):
        return self.product.name



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='Categories/', blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)


    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.brand_name