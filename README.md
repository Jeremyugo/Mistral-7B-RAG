# Mistral-7B-Ollama RAG App

This repository contains code for building a RAG system and deploying it in streamlit.

## Project Oragnization
This project is organized into the following directories: `app`, `data`, `notebooks`, and `scripts`.

- `app`: holds python file for streamlit app
- `data`: contains the data to be fed into the RAG App 
- `notebooks`: holds notebook for prototyping and building the RAG App
- `scripts`: contains python files for App inference

# Getting Started
**`Note:`**
The following requirements must be met to reproduce this project:
1. Access to an ubuntu machine, because Ollama only works on macOS & Linux. If you have a Windows machine, no worries, you can still run this project by installing Linux on Windows. Check out [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
2. A GPU because the Mistral-7B model will be hosted locally. 

## Setting up the Environment
Conda and Docker is not required for this project. However, it is advisable to set up a python environment. To create a python environment run the following:

```
python3 -m venv <env-name>
source <env-name>/bin/activate
```

replace `<env-name>` with the name of your new environment. Then run the code below to download Ollama

```
curl https://ollama.ai/install.sh | sh
```
To install the packages required for the packages

```
pip install torch llama-index qdrant_client transformers streamlit
```
Once all packages have been installed, run the following to start the ollama service
```
ollama serve
```
If the service doesn't start or you get an error, run
```
sudo systemctl stop ollama
ollama serve
```
Ensure this terminal is kept running. To run the Mistral 7B model, open a new terminal and run
```
ollama run mistral
```
To run the Streamlit app, run the following in a new terminal
```
streamlit run app/app.py
```

# Streamlit Demo

https://github.com/Jeremyugo/Mistral-7B-RAG/assets/36512525/98cf70a6-a99d-4974-8198-7ec03ccdd2f7



