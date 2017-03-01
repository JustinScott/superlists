from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        t = request.POST.get('item_text', '')
        if t != '':
            Item.objects.create(text=t)
        return redirect('/lists/the-one/')
    return render(request, 'home.html')


def view_list(request):
    if request.method == 'POST':
        t = request.POST.get('item_text', '')
        if t != '':
            Item.objects.create(text=t)
        return redirect('/lists/the-one/')

    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
