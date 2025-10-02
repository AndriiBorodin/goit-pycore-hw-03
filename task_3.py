import re

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number: str) -> str:
    digits = "".join(re.findall(r"\d+", phone_number))
    has_plus = bool(re.match(r"^\s*\+", phone_number))
    if has_plus or digits.startswith("380"):
        return "+" + digits
    else:
        return "+38" + digits


print([normalize_phone(i) for i in raw_numbers])
# ['+380671234567', '+380952345678', '+380441234567', '+380501234567',
#  '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
