from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from feedbacker.forms import FeedbackForm
from feedbacker.models import Feedback


def default(request):
    return render(request, 'default.html')


@login_required
def home(request):
    feedbacks = Feedback.objects.filter(user=request.user)
    social_account = SocialAccount.objects.filter(provider='vk', user=request.user).first()
    first_name = social_account.extra_data.get('first_name')
    last_name = social_account.extra_data.get('last_name')
    photo = social_account.extra_data.get('photo')
    return render(
        request,
        'home.html',
        {'feedbacks': feedbacks, 'first_name': first_name, 'last_name': last_name, 'photo': photo}
    )


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
