from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def o_nas(request):
    return render(request, 'onas.html')


def serif(request):
    return render(request, 'serif.html')
