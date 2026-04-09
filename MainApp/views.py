from django.shortcuts import render

# Create your views here.
def index(request):
    # This view is to display the homepage.
    return render(request, 'MainApp/index.html')

