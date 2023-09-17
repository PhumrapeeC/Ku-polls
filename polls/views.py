from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from .models import Choice, Question


class IndexView(generic.ListView):
    """
    View to display a list of the latest published questions.

    Attributes:
        template_name (str): The name of the template to be used for rendering the view.
        context_object_name (str): The name of the context variable to store the queryset.
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = context['question']
        user = self.request.user

        # Check if the user has voted for this question
        if user.is_authenticated and question.choice_set.filter(votes=user).exists():
            # Get the user's previous choice for this question
            previous_choice = question.choice_set.get(votes=user)
            context['previous_choice'] = previous_choice

        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check for any success message in the messages framework
        success_messages = messages.get_messages(self.request)
        success_messages = [message for message in success_messages if message.tags == 'success']

        if success_messages:
            context['success_message'] = success_messages[0]

        return context


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not question.can_vote():
        messages.error(request, "Voting for this poll is not allowed at this time.")
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    # Check if the user has already voted for this question
    user = request.user
    if question.choice_set.filter(votes=user).exists():
        previous_choice = question.choice_set.get(votes=user)
        # Remove the old vote
        previous_choice.votes.remove(user)
        messages.warning(request, f"Your old vote for '{previous_choice.choice_text}' has been removed.")

    # Add the new vote
    selected_choice.votes.add(user)
    messages.success(request, f"Your vote for '{selected_choice.choice_text}' has been saved.")

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



