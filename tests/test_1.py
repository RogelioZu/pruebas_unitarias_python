
def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total


def test_calculate_total_with_empty_list():
    print("prueba")
    assert calculate_total([]) == 0

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "audifonos", "price": 50
        },
        {
            "name": "lirbo", "price": 30
        },
        {
            "name": "ipad", "price": 1000
        }

    ]

    assert calculate_total(products) == 1080
    print("otra prueba")

if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_multiple_product()