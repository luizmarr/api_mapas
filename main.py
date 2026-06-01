from fastapi import FastAPI, Form, Request
from services.mapas import Mapas
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="API de Geocodificação",
    description="Uma API para geocodificação de endereços usando a biblioteca geopy.",
)
templates = Jinja2Templates(directory="templates")
mapas = Mapas()

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/geocode")
def geocode(endereco: str = Form(...)):
    resultado = mapas.geocode(endereco)
    if resultado:
        return resultado
    else:
        return {"error": "Endereço não encontrado"}

def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":    
    main()