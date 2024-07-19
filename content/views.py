from django.shortcuts import render, redirect
from .models import Progress, News
from .forms import ProgressForm, NewsForm


def main(request):
    return render(request, 'main.html')


def o_nas(request):
    return render(request, 'onas.html')


def progress_list(request):
    progresses = Progress.objects.all()
    return render(request, 'progress_list.html', {'progresses': progresses})


def progress_create(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('progress_list')
    else:
        form = ProgressForm()
    return render(request, 'progress_form.html', {'form': form})


def progress_update(request, pk):
    progress = Progress.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('progress_list')
    else:
        form = ProgressForm(instance=progress)
    return render(request, 'progress_form.html', {'form': form})


def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'news': news})


def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})


def news_update(request, pk):
    news_item = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'news_form.html', {'form': form})