from django.shortcuts import get_object_or_404, render


from pulseletter.models import Blog, Category 


def posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all()
    posts = Blog.objects.filter(
        status='Published',
        category=category,
    ).order_by('-created_at')

    context = {
        'posts': posts,
        'category': category,
        'selected_category': category,
        'categories': categories,
    }
    return render(request, 'posts_by_category.html', context)






