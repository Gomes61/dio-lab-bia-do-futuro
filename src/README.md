# Passo a Passo de Execução 

## Setup do Ollama 

```bash
#1. Instalar Ollama (ollama.com)
#2. Baixar o modelo leve
ollama pull gpt-oss

#3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo código-fonte está no arquivo 'app.py'. 

## Como Rodar 

```bash
#1Instalar dependências
pip install -r requirements.txt

#2 Garantir que o Ollama está rodando
Ollama serve

#3 Rodar a aplicação
 python -m streamlit run src/app.py
```

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
