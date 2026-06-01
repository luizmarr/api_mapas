# 🌍 GeoMap Explorer (API de Geocodificação)

O **GeoMap Explorer** é uma aplicação web simples e eficiente que converte endereços de texto em coordenadas geográficas (latitude e longitude). O projeto conta com um backend robusto construído em Python com **FastAPI** e uma interface web amigável (frontend) integrada via Jinja2 Templates.

A lógica de localização utiliza a biblioteca **Geopy** integrada ao serviço Nominatim (OpenStreetMap) para buscar os dados de geocodificação de forma gratuita.

---

## 📸 Demonstração da Interface

![Frontend do GeoMap Explorer](app_mapas_frontend.png)
*(Dica: salve o print da sua tela na raiz do projeto com o nome `app_mapas_frontend.png` para que ele apareça aqui!)*

---

## 🚀 Funcionalidades

- **Geocodificação Direta:** Transforma qualquer endereço textual em coordenadas precisas.
- **Interface Web Integrada:** Formulário limpo e intuitivo para inserção de dados pelo usuário.
- **Tratamento de Erros:** Retorna mensagens claras caso o endereço fornecido não seja localizado.
- **Resposta em JSON:** API estruturada pronta para ser consumida por outros serviços ou aplicações.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** [Python 3](https://www.python.org/) & [FastAPI](https://fastapi.tiangolo.com/)
- **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
- **Geocodificação:** [Geopy](https://geopy.readthedocs.io/) (Nominatim / OpenStreetMap)
- **Frontend:** HTML5 & CSS3 (Renderizados através do `FastAPI Templates`)

---

## 📁 Estrutura do Projeto

Conforme a organização atual do diretório de desenvolvimento:

```text
api_mapas/
├── .venv-1/                 # Ambiente virtual contendo as dependências
├── app/
│   └── services/
│       └── mapas.py         # Lógica de integração com o serviço de mapas (Geopy)
├── static/
│   └── style.css            # Estilização visual da interface web
├── templates/
│   └── index.html           # Frontend (Interface do GeoMap Explorer)
├── .gitignore               # Arquivo para ignorar arquivos desnecessários no Git
├── main.py                  # Arquivo principal (Configuração do FastAPI e Rotas)
├── requirements.txt         # Arquivo com as dependências do projeto
└── README.md                # Documentação do projeto