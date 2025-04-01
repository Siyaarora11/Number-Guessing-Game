import random
from django.shortcuts import render

# Create your views here.

random_number = random.randint(1,100)
def guess_number(request):
    global random_number
    message = ''

    if request.method=="POST":
        try:
         user_guess = int(request.POST.get('guess'))
         if user_guess < random_number:
               message = "To Low Please Provide High Number"
         elif user_guess > random_number:
               message = "To High Please Provide Low Number"
         else:
               message = f"Confratulation You Won The Game Correct Number {random_number}"
               random_number = random.randint(1,100)
        except ValueError:
           message = "plese provide valid number"
    return render(request,'guess_number.html',{'message':message})
