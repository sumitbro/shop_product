from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=50, null=True)
    phone= models.CharField(max_length=50)
    email= models.EmailField()
    date_created= models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name= models.CharField(max_length=50, null=True)
    


    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY=(
        ('InDoor', 'InDoor'),
        ('Out Door', 'Out Door'),
    
    )
    name=models.CharField(max_length=50)
    price= models.FloatField()
    category= models.CharField(max_length=200, choices=CATEGORY)
    description= models.TextField(max_length=200, blank=True)
    date_created= models.DateField(auto_now_add=True)
    tag= models.ManyToManyField(Tag)

    def __str__(self):
        return self.name





class Order(models.Model):
    STATUS=(
        ('pending', 'pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created= models.DateField(auto_now_add=True)
    status= models.CharField(max_length=200, null=True, choices=STATUS)


    def __str__(self):
        return self.product.name
    
