from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question, Choice


# Question “index” page – displays the latest few questions.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  # DESC
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# Question “detail” page – displays a question text, with no results but with a form to vote.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


# Question “results” page – displays results for a particular question.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Vote action – handles voting for a particular choice in a particular question.
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
