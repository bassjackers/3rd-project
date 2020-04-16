from django.shortcuts import render, redirect
from django.http import Http404
from .models import Board
from .forms import BoardForm
from csuser.models import Csuser

# Create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board':board})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/csuser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            csuser = Csuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = csuser
            board.save()

            return redirect('/board/list/')
    
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form':form})

def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})