from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406406710',
        'name': 'Farrel Arrayyan Adrianshah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)