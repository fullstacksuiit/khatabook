from udhaar.models import Party, Transaction
from django.shortcuts import render,HttpResponse
from .services import parse_request
# Create your views here.


def render_index(request):
    all_party = Party.objects.all()
    context = {'all_party': all_party}
    return render(request, 'index.html', context)


def add_credit(request):
    if request.method == "POST":
        parse_request(request, credit=True)
    return render_index(request)

def add_debit(request):
    if request.method == "POST":
        parse_request(request, credit=False)
    return render_index(request)


def render_transactions(request):
    transactions = Transaction.objects.all().order_by('-date')
    total_credit = 0
    total_debit = 0
    for t in transactions:
        if t.amount < 0:
            total_debit = total_debit+t.amount
        else:
            total_credit = total_credit+t.amount
    context = {'total_credit':total_credit, 'total_debit':total_debit}
    return render(request, 'udhaar.html', context)
