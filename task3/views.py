from django.shortcuts import render

# Create your views here.
def platform(request):
    title = "Главная страница"
    main = "Главная"
    shop = "Магазин"
    basket = "Корзина"
    context = {
        "title": title,
        "main": main,
        "shop": shop,
        "basket": basket,
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    return render(request, 'third_task/games.html')

def cart(request):
    return render(request, 'third_task/cart.html')