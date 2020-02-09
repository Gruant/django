from .models import Category


def menu(request):
    category_tree = Category.objects.filter(parent=None)
    categories = category_tree.get_descendants(include_self=True)
    context = {
            "category": categories
        }
    return context
