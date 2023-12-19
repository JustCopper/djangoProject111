from django.shortcuts import render, redirect


def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'test.html')

def custom_404(request, exception):
  return render(request, 'er404.html')


def err404(request):
    return render(request, 'er404.html')

def soups_view(request):
     return render(request, 'soups.html')

def hot_view(request):
    if request.method == 'POST':
        recipe_title = request.POST['recipe_title']
        image_path = request.POST['image_path']
        context = {
            'title' : recipe_title,
            'image_path' : image_path
        }
        # ... обработка данных ...
        return render(request, 'foodcard.html',context)
    else:
        return render(request, 'hot.html')

def salati_view(request):
     return render(request, 'salati.html')


def foodcard_view(request):
    context = {
        'title': 'Recipe Page',
        'image_path': '/path/to/image',
        'recipe_title': 'Recipe Title',
        'recipe_description': 'Recipe Description...'
    }
    return render(request, 'FoodCard.html',context)

def zakuski_view(request):
     return render(request, 'zakuski.html')