from django.db import models

# Create your models here.
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Medicine(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    #date_added = models.DateTimeField(auto_now_add=True, null=True)
    #updated = models.DateTimeField(auto_now=True, null=True)
    
    



    def __str__(self):
        return self.name


class MedicineGiven(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity_given = models.IntegerField()
    #date_added = models.DateTimeField(auto_now_add=True, null=True)
    #updated = models.DateTimeField(auto_now=True, null=True)
    
   

    class Meta:
        verbose_name_plural = 'Medicines Given'

    def save(self, *args, **kwargs):
        quantity = int(self.medicine.quantity) - self.quantity_given 

        self.medicine.quantity = quantity
        self.medicine.save()

        super().save(*args, **kwargs)

       
        

    def __str__(self):
        return self.medicine.name