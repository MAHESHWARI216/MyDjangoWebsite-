

# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .models import Contact, BlogPost

# Home Page
def home_page(request):
    current_time = timezone.now()
    return render(request, 'index.html', {'current_time': current_time})   # ✅ Change 'home.html' to 'index.html'

# About Page
def about_page(request):
    return render(request, 'about.html')

# Contact Page
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save into database
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            return render(request, 'thankyou.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Blog List Page
def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})

# Blog Detail Page
def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # <-- important!
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog_form.html', {'form': form})
