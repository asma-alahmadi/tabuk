from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from datetime import timedelta
from .models import *


# Create your views here.


def index(request):
    packages = Package.objects.all()
    return render (request, "tabuk/index.html",
   { "packages": packages})

def package(request):
    empty = False
    packages = Package.objects.all()
    if len(packages) == 0:
        empty = True
    return render(request, "tabuk/packages.html",{
        "packages": packages,
        "empty": empty,
    })




''' Book Package '''
def booking(request, package_slug):
    package= Package.objects.get(slug=package_slug) 
    if request.method == "POST":
        book = Booking()
        book.package = package
        book.name = request.POST.get("name")
        book.email = request.POST.get("email")
        book.adults = request.POST.get("adults")
        book.children = request.POST.get("children")
        book.start_date = request.POST.get("start_date") 
        book.save()
        request.session['total_price'] = (float(book.adults) * package.cost) + (float(book.children) * package.cost)
        return redirect('checkout', book_id=book.id)
    else:
        return render(request, "tabuk/book.html",{
            "package": package,   
    })

def checkout(request, book_id):
    book = get_object_or_404(Booking, id=book_id)
    user = book.name  
    email = book.email
    start_date = book.start_date
    package = book.package
    duration = package.duration
    checkout = Checkout()
    checkout.user = user
    checkout.email = email
    checkout.package = package
    checkout.total_price = request.session['total_price']
    checkout.save()
    end_date = start_date +  timedelta(duration)
    return render(request, "tabuk/checkout.html", {"total_price": request.session['total_price'],
    "checkout": checkout,
    "book": book,
    "end_date": end_date
    })