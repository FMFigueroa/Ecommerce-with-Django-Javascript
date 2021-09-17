from django.shortcuts import render
from .models import Products
from .models import Order
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Products.objects.all()
    
    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects,8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html', {'product_object':product_object})
    
def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items',"")
        firstname = request.POST.get('Fname',"")
        lastname = request.POST.get('Lname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        country = request.POST.get('country',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,firstname=firstname,lastname=lastname,email=email,phone=phone,address=address,city=city,country=country,zipcode=zipcode,total=total)
        order.save()

    return render(request,'shop/checkout.html')