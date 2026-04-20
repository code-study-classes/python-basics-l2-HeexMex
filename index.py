def update_profile(user_id, **updated_fields):
    return {"id": user_id, "updated_fields": updated_fields}


def get_domains(emails):
    return map(lambda email: email.split("@")[1], emails)


def filter_target_audience(users):
    return filter(lambda user: user["age"] >= 18 and user["is_premium"], users)


def build_response(status_code, *errors, **payload):
    return {"status": status_code, "errors": errors, "data": payload}


def calculate_total_spent(transactions):
    return sum(map(lambda transaction: transaction["amount"], transactions))
