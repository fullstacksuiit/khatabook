from .models import *


def parse_request(request, credit=True):
    phone_number = request.POST.get('party')
    party, _ = Party.objects.get_or_create(number=phone_number)
    date = request.POST.get('date')
    amount = float(request.POST.get('amount'))
    if credit is False:
        amount = amount * -1
    description = request.POST.get('description')
    transaction = Transaction(party=party, date=date, amount=amount, description=description)
    transaction.save()
    party.balance = party.balance + float(amount)
    party.save()
   