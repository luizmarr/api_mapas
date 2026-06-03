# 🌍 GeoMap Explorer

Uma aplicação web desenvolvida com **Python** e **FastAPI** que converte endereços em coordenadas geográficas (latitude e longitude) utilizando o serviço **Nominatim (OpenStreetMap)** através da biblioteca **Geopy**.

O projeto conta com uma interface web intuitiva, permitindo que o usuário realize pesquisas de endereços diretamente pelo navegador e visualize os resultados de forma organizada.

---

## 🚀 Funcionalidades

* 🔍 Pesquisa de endereços
* 📍 Conversão de endereços em coordenadas geográficas
* 🌎 Exibição do país encontrado
* 📄 Página de resultado renderizada com Jinja2
* 🎨 Interface estilizada com HTML e CSS
* ⚠️ Tratamento de erros para endereços inválidos
* 🏗️ Estrutura organizada seguindo boas práticas

---

## 📸 Demonstração

### Página Inicial
![Página Inicial](imagens/pagina_inicial.png)

### Página de Resultado

![Resultado da Busca](imagens/resultado_busca.png)
---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python 3
* FastAPI
* Uvicorn

### Geocodificação

* Geopy
* Nominatim (OpenStreetMap)

### Frontend

* HTML5
* CSS3
* Bootstrap
* Jinja2 Templates

### Controle de Versão

* Git
* GitHub

---

## 📂 Estrutura do Projeto

```text
api_mapas/
│
├── app/
│   └── services/
│       └── mapas.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── resultado.html
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/luizmarr/estudos.git
```

### 2. Entrar na pasta do projeto

```bash
cd api_mapas
```

### 3. Criar ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar ambiente virtual

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar aplicação

```bash
python main.py
```

ou

```bash
uvicorn main:app --reload
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos importantes de desenvolvimento web:

* Criação de APIs com FastAPI
* Rotas GET e POST
* Manipulação de formulários HTML
* Templates com Jinja2
* Estilização com CSS
* Organização de projetos Python
* Integração com serviços de geolocalização
* Controle de versão com Git e GitHub

---

## 🔮 Melhorias Futuras

* 🗺️ Exibir mapa interativo com a localização encontrada
* 📱 Melhorar a responsividade para dispositivos móveis
* 🌙 Implementar tema escuro

---

## 👨‍💻 Autor

Desenvolvido por **Luiz Henrique Marreira de Souza** como projeto de estudos em Python, FastAPI e desenvolvimento web.
