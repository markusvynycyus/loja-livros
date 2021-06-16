from django.shortcuts import render, get_object_or_404
from .models import Category, Ecv


def ecv_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    ecvs = Ecv.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        ecvs = ecvs.filter(category=category)
    return render(request,
                  'empresa/ecv/list.html',
                  {'category': category,
                   'categories': categories,
                   'ecvs': ecvs})


def ecv_detail(request, id, slug):
    ecv = get_object_or_404(Livro,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'empresa/ecv/detail.html',
                  {'ecv': ecv})