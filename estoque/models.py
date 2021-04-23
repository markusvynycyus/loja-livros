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
        return reverse('estoque:livro_list_by_category',
                       args=[self.slug])


class Autor(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name ='autor'
        verbose_name_plural ='autores'

    def __str__(self):
        return self.name



class Editora(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering =('name',)
        verbose_name ='editora'
        verbose_name_plural = 'editoras'

    def __str__(self):
        return self.name



class Livro(models.Model):
    category = models.ForeignKey(Category,
                                  related_name='categorias',
                                  on_delete=models.CASCADE)

    autor = models.ManyToManyField(Autor,
                                   related_name='autor') # Um livro posseu vários Autores.

    editora = models.ForeignKey(Editora,
                                related_name='editoras',
                                on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, unique=True)
    paginas = models.PositiveIntegerField()
    image = models.ImageField(upload_to='livros/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=12,
                        validators=[MinValueValidator(1)])



    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together =(('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('estoque:livro_detail',
                       args=[self.id, self.slug])
