from django.shortcuts import render

# Create your views here.
def Post_details(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'base.html',{'posts':post})