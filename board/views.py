from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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
    list.incrementReadCount()
    
    context = {
        'list' : list,
    }
    
    return render(request, 'board/detail.html', context)

def addForm(request) :
    if request.method == 'POST' :
        title = request.POST['title']
        writer = request.POST['writer']
        content = request.POST['content']
        
        Board.objects.create(title=title, writer=writer, content=content)
        
        return HttpResponseRedirect(reverse('board:list'))

    else :
        return render(request, 'board/addForm.html')

def editForm(request, id) :
       list = Board.objects.get(id=id)
       context = {
           'list' : list,
       }
       
       if request.method == 'POST' :
            title = request.POST['title']
            writer = request.POST['writer']
            content = request.POST['content']
            
            Board.objects.filter(id=id).update(title=title, writer=writer, content=content)
            return HttpResponseRedirect(reverse('board:detail', args=(list.id,)))
        
       else :
           return render(request, 'board/editForm.html', context)
       
def deleteForm(request, id) :
    list = Board.objects.get(id=id)
    context = {
        'list' : list,
    }
    
    if request.method == 'POST' :
        Board.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('board:list'))
    
    else :
        return render(request, 'board/deleteForm.html', context)
    
    