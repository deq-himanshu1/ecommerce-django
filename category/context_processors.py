from .models import Category

# Context_processor takes request as an argument and return the dictionary of data 
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)