from django.shortcuts import render, get_object_or_404
from .models import Category, Livro


def livro_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    livros = Livro.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        livros = livros.filter(category=category)
    return render(request,
                  'estoque/livro/list.html',
                  {'category': category,
                   'categories': categories,
                   'livros': livros})


def livro_detail(request, id, slug):
    livro = get_object_or_404(Livro,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'estoque/livro/detail.html',
                  {'livro': livro})