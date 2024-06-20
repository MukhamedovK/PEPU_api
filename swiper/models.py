from django.db import models


class ShowcaseSwiper(models.Model):
    image = models.ImageField(upload_to='swiper/showcase/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class ShowcaseSubSwiper(models.Model):
    image = models.ImageField(upload_to='swiper/showcase-sub/')
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.price}"
    

class ClothesSwiper(models.Model):
    image = models.ImageField(upload_to="swiper/clothes/")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    


