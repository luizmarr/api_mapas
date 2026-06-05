from fastapi import FastAPI, Form, Request
from services.mapas import Mapas
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="API de Geocodificação",
    description="Uma API para geocodificação de endereços usando a biblioteca geopy.",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
mapas = Mapas()

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/geocode")
def geocode(request: Request, endereco: str = Form(...)):
    resultado = mapas.geocode(endereco)
    if resultado:
        return templates.TemplateResponse(
    request=request,
    name="resultado.html",
    context={"resultado": resultado}
)
    else:
        return {"error": "Endereço não encontrado"}

def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":    
    main()