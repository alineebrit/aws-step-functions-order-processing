import json

def lambda_handler(event, context):
    customer_email = event.get("customer_email")
    # Simula envio de notificação

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Order confirmation sent to {customer_email}"})
    }
