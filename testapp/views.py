from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'index.html')
def test2(request):
    return render(request, 'test.html')

def test3(request):
    return render(request, 'test3.html')