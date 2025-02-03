from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from .models import Items, Review
from .searchItems import SearchItems

def index_view(request):
    return render(request, 'index.html')

def search_view(request):
    if request.method == 'GET':
        title = request.GET.get('title', None)
        start = request.GET.get('start', 1)
        site = request.GET.get('site', "all")
        instance = SearchItems()
        results = instance.search(title, start, site)
        hit_count = len(results)
        context = {'results': results, 'hit_count': hit_count}
        return render(request, 'test.html', context)

def detail_view(request, item_id):
    try:
        # item_idに対応するアイテムを取得する
        item = get_object_or_404(Items, pk=item_id)
    except Items.DoesNotExist:
        item = Items.objects.create(
            id=item_id
        )  # 必要に応じて初期値を設定
        return redirect('item_detail', item_id=item.id)

    context = {'item': item}
    return render(request, 'detail.html', context)

class DetailView(DetailView):
    model = Items
    template_name = 'detail.html'

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_form.html'
    fields = ('item','text')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Items.objects.get(pk=self.kwargs['item_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.item.id})