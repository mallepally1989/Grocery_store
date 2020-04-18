from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

STATUS_CHOICES = (
    ("Fruits", "Fruits"),
    ("Foods", "Foods"), 
    ("Drinks","Drinks" ),
    ("Others", "Others"), 
)

class Product(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.0)
    salePrice = models.DecimalField( decimal_places=2, max_digits=100, default=0.0)
    slug = models.SlugField()
    category = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Others")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # to make the title is unique if not, should choose another title to name because it will make slug unique
    class Meta:
        unique_together = ('title', 'slug')

    def get_price(self):
        return self.price
    # to get the link of a unique product
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='')
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title

class Contact(models.Model):
    first_name= models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    message =models.TextField()

    def __str__(self):
        return f'{self.first_name}{self.last_name}'

