from django.shortcuts import render

# HTTP Request
def home_view(request):
    # return HTTP Response
    return render(request, 'recipes/home.html', context={
        'name': 'Lucas'
    })
