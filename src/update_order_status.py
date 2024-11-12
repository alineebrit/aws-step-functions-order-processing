import json

def lambda_handler(event, context):
    order_id = event.get("order_id")
    new_status = "Confirmed"
    # Simula atualização de status do pedido

    return {
        "statusCode": 200,
        "body": json.dumps({"order_id": order_id, "status": new_status})
    }
