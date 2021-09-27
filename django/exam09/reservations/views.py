from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe

# Create your views here.
def index(request):
    reservaions = Reservation.objects.all()
    context = {
        'reservations': reservaions
    }
    return render(request, 'reservations/index.html', context)

@login_required  # 데코레이터
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':  # POST
        form = ReservationForm(data=request.POST)
        if form.is_valid():  # 유효성 검사
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
    else:  # GET
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context)

@require_safe
def detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)  # 404 error
    context = {
        'reservation': reservation,
    }
    return render(request, 'reservations/detail.html', context)
