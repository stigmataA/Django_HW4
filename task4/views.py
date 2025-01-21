from django.shortcuts import render


# Create your views here.
def platform(request):
    title = 'Главная страница'
    menu_choice = {'main': 'Главная', 'shop': 'Магазин', 'cart': 'Корзина'}
    context = {
        'title': title,
        'menu_choice': menu_choice,
    }
    return render(request, 'fourth_task/platform.html', context)


def games(request):
    title = 'Магазин'
    text = 'Игры'
    buy = 'Купить'
    back = 'Вернуться обратно'
    games_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "Pay Day 2"]}
    menu_choice = {'main': 'Главная', 'shop': 'Магазин', 'cart': 'Корзина'}
    context = {
        'title': title,
        'text': text,
        'buy': buy,
        'back': back,
        'games_dict': games_dict,
        'menu_choice': menu_choice,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    title = 'Корзина'
    message = "Извините, Ваша корзина пуста"
    back = 'Вернуться на главную'
    menu_choice = {'main': 'Главная', 'shop': 'Магазин', 'cart': 'Корзина'}
    context = {
        'title': title,
        'message': message,
        'back': back,
        'menu_choice': menu_choice,
    }
    return render(request, 'fourth_task/cart.html', context)




