from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


# Question “index” page – displays the latest few questions.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  # DESC
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# Question “detail” page – displays a question text, with no results but with a form to vote.
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


# Question “results” page – displays results for a particular question.
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


# Vote action – handles voting for a particular choice in a particular question.
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
