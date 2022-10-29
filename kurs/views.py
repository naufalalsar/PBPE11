from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from kurs.models import Currency, Exchange
import requests
from datetime import date
from dateutil.relativedelta import relativedelta
from decimal import Decimal

def get_data(target_currency):
    currencies = Currency.objects.all()
    exchanges = Exchange.objects.filter(target_currency=target_currency)
    last_updated = exchanges[0].last_updated if len(exchanges) > 0 else None
    today = date.today()
    if last_updated != today:
        try:

            sess = requests.Session()
            yesterday = today - relativedelta(days=1)
            one_week_ago = today - relativedelta(weeks=1)
            one_month_ago = today - relativedelta(months=1)
            one_year_ago = today - relativedelta(years=1)
            response = sess.get(
                f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/{target_currency.code.lower()}.json"
            )
            data_today = response.json()
            response = sess.get(
                f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/{target_currency.code.lower()}.json"
            )
            data_yesterday = response.json()
            response = sess.get(
                f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{one_week_ago}/currencies/{target_currency.code.lower()}.json"
            )
            data_one_week = response.json()
            response = sess.get(
                f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{one_month_ago}/currencies/{target_currency.code.lower()}.json"
            )
            data_one_month = response.json()
            response = sess.get(
                f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{one_year_ago}/currencies/{target_currency.code.lower()}.json"
            )
            data_one_year = response.json()
            for source_currency in currencies:
                amount = round(
                    1
                    / float(
                        data_today[target_currency.code.lower()][
                            source_currency.code.lower()
                        ]
                    ),
                    6,
                )
                change_1d = round(
                    (
                        float(
                            data_yesterday[target_currency.code.lower()][
                                source_currency.code.lower()
                            ]
                            / float(
                                data_today[target_currency.code.lower()][
                                    source_currency.code.lower()
                                ]
                            )
                        )
                        - 1
                    )
                    * 100,
                    6,
                )

                change_1w = round(
                    (
                        float(
                            data_one_week[target_currency.code.lower()][
                                source_currency.code.lower()
                            ]
                            / float(
                                data_today[target_currency.code.lower()][
                                    source_currency.code.lower()
                                ]
                            )
                        )
                        - 1
                    )
                    * 100,
                    6,
                )

                change_1m = round(
                    (
                        float(
                            data_one_month[target_currency.code.lower()][
                                source_currency.code.lower()
                            ]
                            / float(
                                data_today[target_currency.code.lower()][
                                    source_currency.code.lower()
                                ]
                            )
                        )
                        - 1
                    )
                    * 100,
                    6,
                )

                change_1y = round(
                    (
                        float(
                            data_one_year[target_currency.code.lower()][
                                source_currency.code.lower()
                            ]
                            / float(
                                data_today[target_currency.code.lower()][
                                    source_currency.code.lower()
                                ]
                            )
                        )
                        - 1
                    )
                    * 100,
                    6,
                )
                change_1d_color = "green-400" if change_1d >= 0 else "red-600"
                change_1w_color = "green-400" if change_1w >= 0 else "red-600"
                change_1m_color = "green-400" if change_1m >= 0 else "red-600"
                change_1y_color = "green-400" if change_1y >= 0 else "red-600"

                exchange = exchanges.filter(source_currency=source_currency)
                # if object has been created and need to be updated
                if exchange:
                    exchange = exchange[0]
                    exchange.amount = amount
                    exchange.change_1d = change_1d
                    exchange.change_1w = change_1w
                    exchange.change_1m = change_1m
                    exchange.change_1y = change_1y
                    exchange.change_1d_color = change_1d_color
                    exchange.change_1w_color = change_1w_color
                    exchange.change_1m_color = change_1m_color
                    exchange.change_1y_color = change_1y_color
                    exchange.last_updated = today
                    exchange.save()
                # if object has not been created
                else:
                    exchange = Exchange(
                        source_currency=source_currency,
                        target_currency=target_currency,
                        amount=amount,
                        change_1d=change_1d,
                        change_1w=change_1w,
                        change_1m=change_1m,
                        change_1y=change_1y,
                        change_1d_color=change_1d_color,
                        change_1w_color=change_1w_color,
                        change_1m_color=change_1m_color,
                        change_1y_color=change_1y_color,
                        last_updated=today,
                    )
                    exchange.save()
        except Exception as e:
            pass

    if len(exchanges) == 0:
        exchanges = Exchange.objects.filter(target_currency=target_currency)

    return exchanges


# Create your views here.
def kurs(request):
    target_currency = Currency.objects.get(code="IDR")
    exchanges = get_data(target_currency)
    for exchange in exchanges:
        exchange.amount = "{:,}".format(exchange.amount)
    context = {"exchanges": exchanges}
    return render(request, "kurs.html", context)


def kurs_json(request, currency):
    target_currency = Currency.objects.get(code=currency)
    exchanges = get_data(target_currency)
    for exchange in exchanges:
        exchange.amount = "{:,}".format(exchange.amount)
    return HttpResponse(serializers.serialize("json", exchanges, use_natural_foreign_keys=True), content_type="application/json")


def calculate(request, source_currency, target_currency):
    source_currency = Currency.objects.get(code=source_currency)
    target_currency = Currency.objects.get(code=target_currency)
    exchange = Exchange.objects.get(source_currency=source_currency, target_currency=target_currency)
    source_amount = Decimal(request.GET.get("source_amount"))
    result = round(exchange.amount * source_amount,6)
    return JsonResponse({"result": result})

def chart(request, source_currency, target_currency):
    source_currency = Currency.objects.get(code=source_currency)
    target_currency = Currency.objects.get(code=target_currency)
    context = {"source_currency": source_currency, "target_currency": target_currency}
    return render(request, "chart.html", context)