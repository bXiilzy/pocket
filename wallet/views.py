from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from .models import Transaction
from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request: HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name") or ""
        amount_raw = request.POST.get("amount") or "0"
        description = request.POST.get("description") or ""
        transaction_type = request.POST.get("transaction_type") or "expense"

        # แปลงเป็น Decimal ให้ตรงกับ DecimalField (กันบั๊กสตริง)
        from decimal import Decimal, InvalidOperation

        try:
            amount = Decimal(amount_raw)
        except InvalidOperation:
            amount = Decimal("0")

        Transaction.objects.create(
            user=request.user,
            name=name.strip(),
            amount=amount,
            description=description.strip(),
            transaction_type=transaction_type,
        )
        return redirect("home")

    # ✅ ดึงข้อมูลแล้วแปลงเป็น list ของ dict (พร้อมฟิลด์ที่อยากใช้ใน JS)
    transactions_qs = (
        Transaction.objects.filter(user=request.user)
        .order_by("-created_at")
        .values("id", "name", "amount", "description", "transaction_type", "created_at")
    )
    transactions_list = list(transactions_qs)

    # ✅ DjangoJSONEncoder จะช่วย serialize Decimal/Datetime ให้เป็น JSON ได้
    transactions_json = json.dumps(transactions_list, cls=DjangoJSONEncoder)

    return render(
        request,
        "home.html",
        context={
            "transactions_json": transactions_json,
            "transactions": transactions_list,
        },
    )

@login_required
def logout_view(request: HttpRequest):
    logout(request)
    return redirect("login")


@login_required
def delete_transaction(request: HttpRequest, transaction_id: int):
    if request.method == "POST":
        try:
            transaction = Transaction.objects.get(
                id=transaction_id, user=request.user)
            transaction.delete()
            return redirect("home")
        except Transaction.DoesNotExist:
            return redirect("home")  # หรือแสดงข้อความ error ก็ได้
    else:
        return redirect("home")  # หรือแสดงข้อความ error ก็ได้


def login_view(request: HttpRequest):
    if request.user.is_authenticated:  # ถ้า login แล้ว ห้ามเข้า
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    else:
        if request.user.is_authenticated:  # ถ้า login แล้ว ห้ามเข้า
            return redirect("home")
        return render(request, "login.html")


def register_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("confirm")

        if not username or not password:
            return render(
                request, "register.html", {
                    "error": "Please fill in all fields"}
            )
        if password != password2:
            return render(request, "register.html", {"error": "Passwords do not match"})
        if User.objects.filter(username=username).exists():
            return render(
                request, "register.html", {"error": "Username already exists"}
            )

        # สร้าง user ใหม่
        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # login อัตโนมัติหลังสมัครเสร็จ
        return redirect("home")

    return render(request, "register.html")

    

