from django.shortcuts import render


def header_page(request):
    print(request)
    return render(request,'home.html')