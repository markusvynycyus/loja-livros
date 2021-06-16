from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('empresa:ecv_list_by_category',
                       args=[self.slug])

class Ecv(models.Model):
    category = models.ForeignKey(Category,
                                  related_name='categorias',
                                  on_delete=models.CASCADE)



    slug = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    endereco = models.CharField(max_length=300, db_index=True)
    email = models.CharField(max_length=200, db_index=True)
    link =models.CharField(max_length=300, db_index=True)
    telefone = models.CharField(max_length=200, db_index=True)


    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together =(('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('empresa:ecv_detail',
                       args=[self.id, self.slug])
