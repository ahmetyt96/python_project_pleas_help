from datetime import datetime, timedelta, date
from itertools import product
import json

json_data = {
    "data": [{
        "name": "ABC",
        "date": "2022-10",
        "in": 10,
        "out": 5,
        "lock": 2
    },
        {
            "name": "ABC",
            "date": "2022-11",
            "in": 14,
            "out": 6,
            "lock": 3
        },
        {
            "name": "ABC",
            "date": "2022-12",
            "in": 23,
            "out": 8,
            "lock": 7
        },
        {
            "name": "ABF",
            "date": "2022-10",
            "in": 26,
            "out": 12,
            "lock": 1
        },
        {
            "name": "ABF",
            "date": "2023-11",
            "in": 34,
            "out": 15,
            "lock": 4
        },
        {
            "name": "DAC",
            "date": "2023-05",
            "in": 45,
            "out": 20,
            "lock": 5
        },
        {
            "name": "DFK",
            "date": "2023-08",
            "in": 56,
            "out": 2,
            "lock": 11
        }
    ]
}


def date_range():
    dataArr = []

    product_dict = {"product": []}

    dates = ["2022-09-13", "2023-04-05"]
    start_date = datetime.strptime(dates[0], "%Y-%m-%d")
    end_date = datetime.strptime(dates[1], "%Y-%m-%d")
    start_year = start_date.year
    start_month = start_date.month
    end_year = end_date.year
    end_month = end_date.month
    dataArr.append(str(start_year) + "-" + str(start_month).zfill(2))
    while start_month <= 12:
        start_month += 1
        if start_month == 12:
            dataArr.append(str(start_year) + "-" + str(start_month).zfill(2))
            start_month = 1
            start_year += 1
        if start_year == end_year and start_month == end_month:
            break

        dataArr.append(str(start_year) + "-" + str(start_month).zfill(2))
    dataArr.append(str(end_year) + "-" + str(end_month).zfill(2))

    for jsData in json_data["data"]:
        if jsData["name"]+"_IN" or jsData["name"]+"_OUT" or jsData["name"]+"_LOCK" not in product_dict["product"]:
            product_dict["product"].append({"model_name": jsData["name"]+"_IN", "data": []})
            product_dict["product"].append({"model_name": jsData["name"]+"_OUT", "data": []})
            product_dict["product"].append({"model_name": jsData["name"]+"_LOCK", "data": []})
        elif jsData["name"]+"_IN" or jsData["name"]+"_OUT" or jsData["name"]+"_LOCK" in product_dict["product"]:
            pass
        else:
            print("else")

    print(json.dumps(product_dict))


date_range()

# def get_date_range(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# def get_month_range(start_date, end_date):
#     for n in range(int((end_date.year - start_date.year) * 12 + end_date.month - start_date.month)):
#         yield start_date + timedelta(n*365/12)