contact = {
    "contact1": {
        "name": "Анна Иванова",
        "phone": "+79001234567",
        "email": "anna.ivanova@example.com"
    },
    "contact2": {
        "name": "Петр Сидоров",
        "phone": "+79119876543",
        "email": "petr.sidorov@example.com"
}
}

print(contact["contact1"])
contact["contact2"]["phone"] = "+79225551122"
contact["contact1"]["address"] = "г. Москва, ул. Пушкина, д. 10"
del contact["contact2"]["email"]

print(contact)
