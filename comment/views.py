from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from .form import CommentForm
from .models import Comment
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def comments(request):
    user_comments = Comment.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('comment')
    else:
        form = CommentForm()
    template = loader.get_template('comment/comments.html')
    context = {
        'form': form,
        'comments': user_comments
    }
    return HttpResponse(template.render(context, request))
