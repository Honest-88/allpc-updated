# Core Django imports.
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView
)

# Blog application imports.
from blog.models.article_models import Article, Category


class CategoryArticlesListView(ListView):
    model = Article
    paginate_by = 6
    context_object_name = 'articles'
    template_name = 'blog/category/category_articles.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Article.objects.filter(category=category, status=Article.PUBLISHED, deleted=False)

    def get_context_data(self, **kwargs):
        context = super(CategoryArticlesListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context['category'] = category
        return context

class CategoriesListView(ListView):
    model = Category
    paginate_by = 12
    context_object_name = 'categories'
    template_name = 'blog/category/categories_list.html'

    def get_queryset(self):
        return Category.objects.order_by('-date_created')


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name", "image"]
    template_name = 'blog/category/category_form.html'

    def form_valid(self, form):
        form.instance.save()
        messages.success(self.request, f"'{form.instance.name}' "
                                       f"submitted successfully. You will be "
                                       f"notified when it is approved."
                                       f"Thank you !!!")
        return redirect('/')


class CategoryUpdateCreateView(LoginRequiredMixin, SuccessMessageMixin,
                               UpdateView):
    model = Category
    fields = ["name", "image"]
    template_name = 'blog/category/category_form.html'
    success_url = reverse_lazy("blog:categories_list")
    success_message = "Category Updated Successfully"




class TagArticlesListView(ListView):
    """
        List articles related to a tag.
    """
    model = Article
    paginate_by = 12
    context_object_name = 'tag_articles_list'
    template_name = 'blog/article/tag_articles_list.html'

    def get_queryset(self):
        """
            Filter Articles by tag_name
        """

        tag_name = self.kwargs.get('tag_name', '')

        if tag_name:
            tag_articles_list = Article.objects.filter(tags__name__in=[tag_name],
                                                       status=Article.PUBLISHED,
                                                       deleted=False
                                                       )

            if not tag_articles_list:
                messages.info(self.request, f"No Results for '{tag_name}' tag")
                return tag_articles_list
            else:
                messages.success(self.request, f"Results for '{tag_name}' tag")
                return tag_articles_list
        else:
            messages.error(self.request, "Invalid tag")
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(approved=True)
        return context

