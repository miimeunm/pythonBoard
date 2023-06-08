from django.http import HttpResponse
from django.shortcuts import render
from .models import Board

def index(request) :
    return render(request, 'board/index.html')

def list(request) :
    board_list = Board.objects.all()
    context = {
        'board_list' : board_list,
    }
    
    return render(request, 'board/list.html', context)

def detail(request, id) :
    list = Board.objects.get(id=id)
    
    context = {
        'list' : list,
    }
    
    return render(request, 'board/detail.html', context)