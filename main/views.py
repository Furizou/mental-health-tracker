from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306228390',
        'name': 'Kukuh CU',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)