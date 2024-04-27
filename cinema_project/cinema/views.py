from django.shortcuts import render, redirect, get_object_or_404
from .models import cinema
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

@login_required
def create_cinema(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.userid = request.user
            note.save()
            return redirect('cinemas_list')
    else:
        form = NoteForm()
    return render(request, 'cinema/create_cinema.html', {'form': form})

@login_required
def cinemas_list(request):
    cinemas = cinema.objects.filter(userid=request.user)
    return render(request, 'cinema/cinemas_list.html', {'cinemas': cinemas})

@login_required
def view_cinema(request, cinema_id):
    mov = get_object_or_404(cinema, id=cinema_id)
    return render(request, 'cinema/view_cinema.html', {'cinema': mov})

@login_required
def update_cinema(request, cinema_id):
    note = get_object_or_404(cinema, id=cinema_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('cinemas_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'cinema/update_cinema.html', {'form': form})

@login_required
def delete_cinema(request, cinema_id):
    note = get_object_or_404(cinema, id=cinema_id)
    if request.method == 'POST':
        note.delete()
        return redirect('cinemas_list')
    return render(request, 'cinema/delete_cinema.html', {'cinema': note})
