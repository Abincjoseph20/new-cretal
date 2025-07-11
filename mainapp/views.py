from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from .models import CATEGORY_CHOICE  # Import the tuple directly



def base(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request,'mainapp/index.html',context)

#locals() is a built in function to call all the local functions
class Category(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'mainapp/category.html',locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,'mainapp/category.html',locals())
    
class ProductDetails(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'mainapp/productdetais.html', locals())


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(description__icontains=keyword)
            # product_count = product.count()
        else:
            return redirect('home')
    contxt = {
        'products' : products,
        # 'product_count' : product_count,
    }
    return render(request,'mainapp/store.html',contxt)


def store(request):
    products = Product.objects.all()
    contxt ={
        'products':products
    }
    return render(request,'mainapp/store.html',contxt)



def demo(request):
    return render(request,'mainapp/demo.html')


def erro_handiling(request):
    return render(request,'mainapp/error_message.html')


def admin_list(request):
    products = Product.objects.all().order_by('-created_date')  # Changed variable name to plural
    context = {
        'products': products,  # Changed key to plural to match template
        'category_choices': dict(CATEGORY_CHOICE)  # Use the tuple directly
    }
    return render(request, 'admin/admin_list.html', context)  # Added context parameter



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect('product_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm()
    
    return render(request, 'admin/add_product.html', {'form': form})



def admin_home(request):
    return render(request,'admin/admin_home1.html')




def product_update(request,pk):
    product = get_object_or_404(Product,pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            updated_product = form.save()
            
            messages.success(request, f"Product '{updated_product.title}' updated successfully.")            
            return redirect('product_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'product': product,
        'is_update': True  # Flag to indicate update mode in template
    }
    
    return render(request, 'admin/product_update.html', context)

def admin_delete(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'admin/delete.html',{'product':product})