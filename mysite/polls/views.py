from typing import Any
from django.db.models import F
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"  # default : "polls/question_list.html"
    context_object_name = "latest_question_list"  # default : question_lista

    def get_queryset(self):
        """Return the last five published questions(pub_date가 미래 시점인 question 제외)."""
        # __lte : less than or equal to
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    # pub_date가 미래 시점인 question 제외
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST : 넘어온 데이터에 key로 접근한다.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # 데이터가 두 번 POST 되는 것을 방지하기 위해 HttpResponse가 아닌 HttpResponseRedirect를 return
        # reverse() : urls.py에 정의한 name으로 url을 넘긴다. -> 유지/보수 용이
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
