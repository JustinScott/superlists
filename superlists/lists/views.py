from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    if request.POST.get('item_text', '') != '':
        Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-one/')
