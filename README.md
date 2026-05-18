#  API de Mapas (Geocoding)

API simples em Python que converte endereços em coordenadas geográficas (latitude e longitude) utilizando a biblioteca **Geopy** e o serviço Nominatim (OpenStreetMap).

---

##  Funcionalidades

- Converter endereço em coordenadas (geocoding)
- Retornar endereço formatado
- Retornar latitude e longitude
- Estrutura simples e fácil de expandir para projetos maiores

---

##  Tecnologias utilizadas

- Python
- FastAPI (opcional, se você estiver usando API)
- Geopy
- Uvicorn

---

##  Estrutura do projeto

```text
api_mapa/
│
├── main.py
├── mapas.py
├── requirements.txt
└── README.md