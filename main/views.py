from django.shortcuts import render


def home(request):
    context = {
        "title": "Головна сторінка",
        "content": "Це головна сторінка. Тут є посилання на всі інші сторінки.",
        "is_home": True,
        "pages": [
            {"name": "Сторінка 1", "url": "/page1/"},
            {"name": "Сторінка 2", "url": "/page2/"},
            {"name": "Сторінка 3", "url": "/page3/"},
        ],
    }

    return render(request, "main/page.html", context)


def page1(request):
    context = {
        "title": "Сторінка 1",
        "content": "Це контент першої сторінки.",
        "is_home": False,
    }

    return render(request, "main/page.html", context)


def page2(request):
    context = {
        "title": "Сторінка 2",
        "content": "Це контент другої сторінки.",
        "is_home": False,
    }

    return render(request, "main/page.html", context)


def page3(request):
    context = {
        "title": "Сторінка 3",
        "content": "Це контент третьої сторінки.",
        "is_home": False,
    }

    return render(request, "main/page.html", context)