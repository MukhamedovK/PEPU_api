from django.db import models

# from products.models import Product



class Profile(models.Model):

    class ProfileStatus(models.TextChoices):
        OFFLINE = "Оффлайн", "offline"
        ONLINE = "Онлайн", "online"

    image = models.ImageField(upload_to='profile/', default='media/default-img/profile.png')
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    password = models.CharField(max_length=30)
    job = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=ProfileStatus.choices, default=ProfileStatus.OFFLINE)
    salary = models.PositiveIntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname} - {self.status}"


class Branches(models.Model):
    title = models.CharField(max_length=200, default="Aptamat ko't")
    description = models.TextField()
    branch_manager = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    open_at = models.TimeField()
    close_at = models.TimeField()


    def __str__(self):
        return f"{self.title} - {self.branch_manager}"



    
