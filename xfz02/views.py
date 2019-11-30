from django.shortcuts import render

def test(request):
    return render(request,'news/index.html')
