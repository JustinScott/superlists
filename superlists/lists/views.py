from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        t = request.POST.get('item_text', '')
        if t != '':
            Item.objects.create(text=t)
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
