data = {
    'visa': '',
    'mastercard': '',
    'maestro': '',
    'mir': '',
    'jcb': '',
    'discover': '',
}


def make_payment_gateway(name_card: str):
    def payment_gateway(card_number: str):
        print(f"Processing payment with {name_card} card: {card_number}")
        return True
    return payment_gateway

caskade = []
for card_name in data.keys():
    caskade.append(make_payment_gateway(card_name))

for el in caskade:
    if el('1234-5678-9012-3456'):
        print(f"Payment successful with {el.__name__} card")
        break

