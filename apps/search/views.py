from django.shortcuts import render

def search_index(request):
    return render(request,'search/search.html')