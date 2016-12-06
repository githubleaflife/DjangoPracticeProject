from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import ArticleColumn
from django.contrib.auth.models import User

from .forms import ArticleColumnForm

@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
	if request.method == "GET":
	    columns = ArticleColumn.objects.all()
	    column_form = ArticleColumnForm()
	    return render(request, "ArticleManage/column/article_column.html", {"columns":columns, 'column_form':column_form})

	if request.method == "POST":
		column_name = request.POST['column']
		has_column = ArticleColumn.objects.filter(column=column_name)
		if has_column:
			return HttpResponse('2')
		else:
		    user = User.objects.get(username=request.user.username)
		    ArticleColumn.objects.create(user=user, column=column_name)
		    return HttpResponse("1")
