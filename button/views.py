from django.shortcuts import render,redirect
from .models import Subscriber
from django.contrib import messages


# Create your views here.

def subscription(request):
    if request.method == 'POST':
        useremail = request.POST.get('email')
        action = request.POST.get('action')

        if useremail:
            subscriber, created = Subscriber.objects.get_or_create(useremail=useremail)
            
            if action == 'subscribe':
                if not subscriber.subscribed:
                    subscriber.subscribed = True
                    subscriber.save()
                    messages.success(request, 'You have successfully subscribed!')
                else:
                    messages.info(request, 'You are already subscribed!')

            elif action == 'unsubscribe':
                if subscriber.subscribed:
                    subscriber.subscribed = False
                    subscriber.save()
                    messages.success(request, 'You have successfully unsubscribed!')
                else:
                    messages.info(request, 'You are not subscribed!')

        else:
            messages.error(request, 'Please enter a valid email address!')

        return redirect('subscription')  # Correct the URL name if needed

    return render(request, 'index.html')         
              


        

