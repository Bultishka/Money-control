from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Expense
from datetime import datetime
from django.db.models import Sum, Avg, Max
from django.core.paginator import Paginator


@login_required(login_url='login')
def expenses(request):

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = int(data.get('price', 0))
        date = data.get('date')
        record_type = data.get('record_type', 'expense')

        Expense.objects.create(
            user=request.user,
            name=name,
            price=price,
            date=date,
            record_type=record_type,
        )
        return redirect('expenses')

    queryset = Expense.objects.filter(user=request.user)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date:
        queryset = queryset.filter(date__gte=start_date)
    if end_date:
        queryset = queryset.filter(date__lte=end_date)

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'expenses': page_obj,
        'start_date': request.GET.get('start_date', ''),
        'end_date': request.GET.get('end_date', ''),
    }
    return render(request, 'expenses.html', context)


@login_required(login_url='/login/')
def update_expense(request, id=None):
    expense = get_object_or_404(Expense, id=id, user=request.user) if id else None

    if request.method == 'POST':
        name = request.POST.get('name')
        price = int(request.POST.get('price', 0))
        date = request.POST.get('date')
        record_type = request.POST.get('record_type', 'expense')

        expense.name = name
        expense.price = price
        expense.date = datetime.strptime(date, '%Y-%m-%d') if date else datetime.today()
        expense.record_type = record_type
        expense.save()
        messages.success(request, "Запись успешно обновлена!")

        return redirect('expenses')

    context = {'expense': expense}
    return render(request, 'update_expense.html', context)


@login_required(login_url='/login/')
def delete_expense(request, id):
    queryset = Expense.objects.filter(id=id, user=request.user).first()
    if not queryset:
        messages.error(request, "Вы не можете удалить эту трату")
        return redirect('/')

    queryset.delete()
    return redirect('/')


def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if not user_obj:
                messages.error(request, "Пользователь не найден")
                return redirect('/login/')
            user_auth = authenticate(username=username, password=password)
            if user_auth:
                login(request, user_auth)
                return redirect('expenses')
            messages.error(request, "Неверный пароль")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Что-то пошло не так")
            return redirect('/register/')
    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Ник занят")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Аккаунт создан")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Что-то пошло не так")
            return redirect('/register')
    return render(request, "register.html")


def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def analyze(request):

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    expenses_queryset = Expense.objects.filter(user=request.user, record_type='expense')
    income_queryset = Expense.objects.filter(user=request.user, record_type='income')

    if start_date:
        expenses_queryset = expenses_queryset.filter(date__gte=start_date)
        income_queryset = income_queryset.filter(date__gte=start_date)
    if end_date:
        expenses_queryset = expenses_queryset.filter(date__lte=end_date)
        income_queryset = income_queryset.filter(date__lte=end_date)

    expenses_total = expenses_queryset.aggregate(Sum('price'), Max('price'), Avg('price'))
    expenses_sum = expenses_total['price__sum'] or 0
    expenses_max = expenses_total['price__max'] or 0
    expenses_avg = round(expenses_total['price__avg'] or 0, 2)

    income_total = income_queryset.aggregate(Sum('price'), Max('price'), Avg('price'))
    income_sum = income_total['price__sum'] or 0
    income_max = income_total['price__max'] or 0
    income_avg = round(income_total['price__avg'] or 0, 2)

    context = {
        'expenses': expenses_queryset,
        'income': income_queryset,
        'total_expenses': expenses_sum,
        'max_expense': expenses_max,
        'avg_expense': expenses_avg,
        'total_income': income_sum,
        'max_income': income_max,
        'avg_income': income_avg,
        'username': request.user.username,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'analyze.html', context)