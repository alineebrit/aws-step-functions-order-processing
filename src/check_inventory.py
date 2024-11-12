import json

def lambda_handler(event, context):
    item_id = event.get("item_id")
    # Simula verificação de estoque
    stock_available = True  # Simula estoque disponível

    return {
        "statusCode": 200,
        "body": json.dumps({"item_id": item_id, "stock_available": stock_available})
    }
