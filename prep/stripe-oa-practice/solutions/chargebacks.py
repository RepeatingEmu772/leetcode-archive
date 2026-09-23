"""Your solution for chargebacks. See the corresponding file in problems/."""
import csv
import re


def validate(fields: list[str]) -> str | None:
    if len(fields) != 5:
        return None

    t_id, m_id, amount, currency, reason = [
        field.strip() for field in fields
    ]

    # Nonempty IDs containing only ASCII letters, digits, _ or -
    for identifier in (t_id, m_id):
        if re.fullmatch(r"[A-Za-z0-9_-]+", identifier) is None:
            return None

    # Positive integer written using ASCII digits only
    if re.fullmatch(r"[0-9]+", amount) is None:
        return None

    amount_value = int(amount)
    if amount_value <= 0:
        return None

    if currency not in {"USD", "EUR", "JPY"}:
        return None

    if reason not in {"fraud", "duplicate", "withdrawn"}:
        return None

    return f"{t_id},{m_id},{amount_value},{currency},{reason}"

def processFile(network, content):
    transactions = {}

    for line in content.splitlines()[1:]:
        if not line.strip():
            continue

        try:
            fields = next(csv.reader([line], strict=True))
        except csv.Error:
            continue

        validated = validate(fields)
        if validated is None:
            continue

        t_id = validated.split(",", 1)[0]
        transactions[(network, t_id)] = f"{network},{validated}"

    return transactions


def solve(data: dict, part: int = 3) -> list[str]:
    files = sorted(data["files"], key=lambda file: file["date"])
    transactions = {}

    for file in files:
        network = file["network"]
        content = file["contents"]

        file_transactions = processFile(network, content)
        transactions.update(file_transactions)

    result = [
        transactions[key]
        for key in sorted(transactions)
        if transactions[key].split(",")[-1] != "withdrawn"
    ]

    return result


if __name__ == "__main__":
    test_input = {
        "files": [{
            "network": "visa",
            "date": "2026-01-01",
            "contents": (
                "transaction_id,merchant_id,amount,currency,reason\n\n"
                '"t", m1 , 001 , USD , fraud\n\n'
            ),
        }]
    }


    result = solve(test_input)  # Replace with your function name
    print(result)


