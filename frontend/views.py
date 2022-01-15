from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'frontend/index.html')

def detail(request):
    return render(request, 'frontend/detail.html')

def pesan(request):
    return render(request, 'frontend/pesan.html')

def konfirmasi(request):
    return render(request, 'frontend/history-invoice.html')