from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.


class TODO (models.Model):

    name = models.CharField(max_length= 50 , unique=True , )
    
    description = models.TextField(null = True , blank=True)

    Deadline = models.DateField ()

    def __str__(self):
        return self.name





class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING' , 'PENDING'),
        ('IN PROGRESS' , 'IN PROGRESS'),
        ('COMPLETED' , 'COMPLETED'),
    ]
    
    title=models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length = 12 , choices = STATUS_CHOICES , default = 'PENDING')
    due_date = models.DateField(null= True , blank=True)
    priority = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(10)] ,null= True , blank= True) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    TODO = models.ForeignKey(TODO, on_delete=models.CASCADE )
    def __str__(self):
        return self.title




 
class comment(models.Model):
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)


    task = models.ForeignKey(Task , on_delete = models.CASCADE)

    
    def __str__(self):
        return self.content