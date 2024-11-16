from django.shortcuts import render

def get_landing_page(request):
        return render(request, 'Landing_Page/index.html')