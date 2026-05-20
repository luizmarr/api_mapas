from fastapi import FastAPI
from services.mapas import Mapas

app = FastAPI(
    title="API de Geocodificação",
    description="Uma API para geocodificação de endereços usando a biblioteca geopy.",
)

mapas = Mapas()

@app.get("/geocode")
def geocode(endereco: str):

    resultado = mapas.geocode(endereco)

    if not resultado:
        return {"erro": "Endereço não encontrado"}

    return resultado

def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":    
    main()