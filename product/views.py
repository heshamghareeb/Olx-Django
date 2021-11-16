from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count, Q

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('search_q')
    if search_query:
        productlist = productlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(status__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query) 
            
        )

    paginator = Paginator(productlist, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    template = "Product/product_list.html"
    context = {'product_list':productlist,'category_list':categorylist,'category':category}
    return render(request, template, context)

def index(request, category_slug=None):
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('search_q')
    if search_query:
        productlist = productlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(status__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query) 
            
        )


    template = "Product/index.html"
    context = {'product_list':productlist,'category_list':categorylist,'category':category}
    return render(request, template, context)




def product_detail(request, product_slug):
    print(product_slug,'product_slug')
    productdetail = get_object_or_404(Product, slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    context = {'product_detail':productdetail, 'product_images': productimages}
    return render(request, 'Product/product_detail.html', context)