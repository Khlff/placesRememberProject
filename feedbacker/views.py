from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def home(request):
    feedbacks = Feedback.objects.filter(user=request.user)
    return render(request, 'home.html', {'feedbacks': feedbacks})

@login_required
def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_adding.html', {'form': form})


