from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    return render(request, 'bankapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'bankapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    profile = request.user.profile
    transactions = Transaction.objects.filter(user=request.user).order_by('-timestamp')[:10]
    return render(request, 'bankapp/dashboard.html', {
        'balance': profile.balance,
        'transactions': transactions
    })

@login_required
def deposit_view(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        profile = request.user.profile
        profile.balance += amount
        profile.save()
        Transaction.objects.create(user=request.user, action='Deposit', amount=amount)
        return redirect('dashboard')
    return render(request, 'bankapp/deposit.html')

@login_required
def withdraw_view(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        profile = request.user.profile
        if amount > profile.balance:
            messages.error(request, "Insufficient funds.")
        else:
            profile.balance -= amount
            profile.save()
            Transaction.objects.create(user=request.user, action='Withdraw', amount=amount)
            return redirect('dashboard')
    return render(request, 'bankapp/withdraw.html')

@login_required
def transfer_view(request):
    if request.method == 'POST':
        recipient_username = request.POST['to_user']
        amount = float(request.POST['amount'])
        try:
            recipient = User.objects.get(username=recipient_username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('transfer')
        sender_profile = request.user.profile
        recipient_profile = recipient.profile
        if amount > sender_profile.balance:
            messages.error(request, "Insufficient funds.")
        else:
            sender_profile.balance -= amount
            recipient_profile.balance += amount
            sender_profile.save()
            recipient_profile.save()
            Transaction.objects.create(user=request.user, action='Transfer Sent', amount=amount, note=f"To {
