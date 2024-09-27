from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from myblog.models import Myblog


class MyblogCreateView(CreateView):
    model = Myblog
    fields = ('title', 'slug', 'body', 'preview', 'created_at', 'public', 'views_counter')
    success_url = reverse_lazy('myblog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MyblogListView(ListView):
    model = Myblog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(public=True)
        return queryset


class MyblogUpdateView(UpdateView):
    model = Myblog
    fields = ('title', 'slug', 'body', 'preview', 'created_at', 'public', 'views_counter')
    success_url = reverse_lazy('myblog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('myblog:view', args=[self.kwargs.get('pk')])


class MyblogDetailView(DetailView):
    model = Myblog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class MyblogDeleteView(DeleteView):
    model = Myblog
    success_url = reverse_lazy('myblog:list')
