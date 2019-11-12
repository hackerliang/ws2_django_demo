from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def index1(request):
    context = dict()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data['search']
            print(post_data)
        context['content'] = "I love UIC"
    else:
        context['content'] = "I love DS!"
        form = SearchForm()
    context['form'] = form
    return render(request, 'index.html', context)