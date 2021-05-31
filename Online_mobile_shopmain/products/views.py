from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ProductsTable


# Create your views here.

def product(request):
    pics = ProductsTable.objects.all()
    return render(request, 'product.html', {"pics": pics})


def video(request):
    pics = ProductsTable.objects.all()
    return render(request, 'product.html', {"pics": pics})


class search(TemplateView):
    template_name = "search.html"

    def get_context_data(request):

        kw = request.GET.get("keyword")
        results = ProductsTable.object.filter(product_name__icontains=kw)

        return render(request, 'search.html', {'results':request})
