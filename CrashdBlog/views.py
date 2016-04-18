from django.shortcuts import render

def post_list(request):
    return render(request, 'CrashdBlog/post_list.html', {})
