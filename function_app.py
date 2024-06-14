import azure.functions as func
import logging
from vision_oai import images_prompt

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="ImagePrompt")
def ImagePrompt(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    api_key = req_body.get('api_key')
    prompt = req_body.get('prompt')
    urls = req_body.get('urls')
    if not (api_key and prompt):
        return func.HttpResponse(
             f"This HTTP triggered function executed successfully. Provide prompt and key, {req_body}",
             status_code=200
        )
        
    try:
        result = images_prompt(
            api_key,
            prompt,
            *urls
        )
    except Exception as e:
        return func.HttpResponse(
             f"{req_body} \n\n"+str(e),
             status_code=500
        )
            
    return func.HttpResponse(result)
    