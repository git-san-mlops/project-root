import azure.functions as func
import requests
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        app_url = os.environ.get("APP_URL")

        response = requests.get(f"{app_url}/random-fruit")

        return func.HttpResponse(
            response.text,
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)