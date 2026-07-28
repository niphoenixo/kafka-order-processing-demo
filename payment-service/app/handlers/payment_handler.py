def process_payment(order):
    print("=" * 60)
    print(f"Received Order : {order['order_id']}")
    print(f"Customer       : {order['customer']}")
    print(f"Amount         : {order['amount']}")
    print("Processing Payment...")

    if order["amount"] > 1000:
        raise Exception("Payment Gateway Unavailable")

    print("✅ Payment Successful")
    print("=" * 60)