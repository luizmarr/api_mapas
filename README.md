# 🌎 GeoMap Explorer

Aplicação web desenvolvida em **Python** utilizando **FastAPI** para realizar geocodificação de endereços e apresentar a localização encontrada em um mapa.

O projeto foi desenvolvido como forma de prática em desenvolvimento web, criação de APIs e integração com serviços de geolocalização.

## 🚀 Tecnologias

* 🐍 Python
* ⚡ FastAPI
* 🗺️ Geopy
* 🌐 HTML5
* 🎨 CSS3
* 📄 Jinja2
* 🖥️ Uvicorn

## 📌 Funcionalidades

* 🔎 Pesquisa de endereços
* 📍 Geocodificação de endereços
* 🌎 Conversão de endereços em coordenadas geográficas
* 🗺️ Exibição da localização em um mapa
* 📌 Marcador para a localização encontrada
* ⚠️ Tratamento de endereço não encontrado
* 📚 Documentação automática da API com FastAPI

## 🖥️ Funcionamento

O usuário informa um endereço através da interface da aplicação.

A aplicação envia o endereço para o sistema de geocodificação, que realiza a busca e retorna as informações da localização.

Quando o endereço é encontrado, a aplicação apresenta os dados e sua localização no mapa.

### Exemplo

```text
Endereço informado:
Avenida Paulista, São Paulo

Resultado:
Latitude: -23.561684
Longitude: -46.655981
```

## 📂 Estrutura do projeto

```text
api_mapas/
│
├── services/
│
├── static/
│
├── templates/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### 📁 Principais diretórios

**`services/`**

Contém os serviços utilizados pela aplicação.

**`static/`**

Contém os arquivos estáticos utilizados pela interface, como arquivos CSS.

**`templates/`**

Contém os templates HTML utilizados pela aplicação.

**`main.py`**

Arquivo principal responsável pela inicialização da aplicação FastAPI e definição das rotas.

**`requirements.txt`**

Contém as dependências necessárias para executar o projeto.

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### 2. Entre na pasta do projeto

```bash
cd api_mapas
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

## ▶️ Executando o projeto

Com o ambiente virtual ativado, execute:

```bash
uvicorn main:app --reload
```

Depois, acesse:

```text
http://127.0.0.1:8000
```

## 📚 Documentação da API

O FastAPI disponibiliza uma documentação interativa automaticamente.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## 🚀 Próximas melhorias

* [ ] Implementar busca por localização diretamente no mapa
* [ ] Adicionar histórico de pesquisas
* [ ] Melhorar a experiência em dispositivos móveis
* [ ] Adicionar mais validações para endereços
* [ ] Implementar testes automatizados
* [ ] Melhorar o tratamento de erros
* [ ] Adicionar novos recursos de geolocalização
* [ ] Melhorar a organização e arquitetura do projeto

## 🎯 Objetivo

O **GeoMap Explorer** foi desenvolvido com o objetivo de colocar em prática conhecimentos de **Python, FastAPI, desenvolvimento web, APIs e geolocalização**.

O projeto também representa parte da minha evolução prática no desenvolvimento de software.

## 👨‍💻 Autor

**Luiz Henrique**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS)**.

---

⭐ Se você gostou do projeto, considere deixar uma estrela no repositório.
