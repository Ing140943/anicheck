from django.shortcuts import render


def about_us(request):
    return render(request, 'blog/contact.html', )
