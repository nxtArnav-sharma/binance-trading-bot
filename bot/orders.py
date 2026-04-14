from .client import get_client


def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            if price is None:
                raise ValueError("LIMIT orders require a price.")

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        return order

    except Exception as e:
        print("Error placing order:", str(e))
        raise