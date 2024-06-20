from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    

class Product(models.Model):
    from adminDashboard.models import Branches
    
    class ProductStatus(models.TextChoices):
        ON_SALE = "В наличии", "On Sale"
        IN_STOCK = "На складе", "In Stock"
        NOT_AVAILABLE = "Нет в наличии", "Not Available"

    class RatingChoices(models.IntegerChoices):
        ZERO_STAR = 0, 'Zero Star'
        ONE_STAR = 1, 'One Star'
        TWO_STAR = 2, 'Two Star'
        THREE_STAR = 3, 'Three Star'
        FOUR_STAR = 4, 'Four Star'
        FIVE_STAR = 5, 'Five Star'

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    branches = models.ManyToManyField(Branches, related_name="branches")
    badge = models.CharField(max_length=200, choices=ProductStatus.choices, default=ProductStatus.IN_STOCK)
    sizes = models.ManyToManyField(Size, related_name='sizes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.ZERO_STAR)

    def __str__(self):
        return f"{self.title} - {self.badge}"


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} - {self.photo.url}"    
