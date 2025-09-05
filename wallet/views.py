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



