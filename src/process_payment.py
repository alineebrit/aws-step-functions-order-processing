import json

def lambda_handler(event, context):
    order_id = event.get("order_id")
    # Simula processamento de pagamento
    payment_successful = True  # Simula pagamento bem-sucedido

    return {
        "statusCode": 200,
        "body": json.dumps({"order_id": order_id, "payment_successful": payment_successful})
    }
