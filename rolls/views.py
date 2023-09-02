from django.shortcuts import render
from .models import Roll

# Create your views here.
def rolls(request):
    rolls = Roll.objects.all # save all the model objecets (db records)
    return render(request, 'rolls/sushi-rolls.html', {'rolls': rolls}) #third parameter: rolls variable is the dictionary of the rolls records

def contacts(request):
    return render(request, 'rolls/contacts.html')

def order(request):
    rolls = Roll.objects.all
    return render(request, 'rolls/order-now.html', {'rolls': rolls})