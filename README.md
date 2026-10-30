# Projeto-Avaliativo-Final---M-dulo-2
Projeto Avaliativo Final - Módulo 2

# Projeto: Classificação de Niveis de Obesidade para Mulheres 40+
Este notebook guiará o desenvolvimento, modularização e documentação de uma API Web completa utilizando FastAPI para disponibilizar um modelo preditivo treinado.

## Escolha do Modelo e Dataset
Para garantir que a validação via Pydantic e os endpoints da API funcionem de forma clara, e de acordo com interesses pessoais, escolhi o dataset "Estimation of Obesity Levels Based on Eating Habits and Physical Condition".

### Dataset: 
"Estimation of Obesity Levels Based on Eating Habits and Physical Condition". Utilizando uma estratégia de filtragem para o público feminino 40+

### Objetivo: 
Classificar o nível de obesidade de um indivíduo (peso insuficiente, peso normal, sobrepeso, obesidade I, II ou III).

### Variáveis de Entrada: 
Hábitos alimentares (consumo de vegetais, número de refeições, ingestão de água) e condição física (atividade física, tempo de uso de telas, idade, histórico familiar).

### Vantagem para a API: 
Excelente para criar uma API de recomendação de saúde ou estilo de vida, exigindo uma validação bem rica com Pydantic para strings, números e enums (como frequências de hábitos).

## Tecnologias Utilizadas: 
Version: 1.144.0 (user setup)
Commit: 2c33b50b16c472efe58357d1d2a8a5414bc23fbf
Date: 2026-10-27T20:18:03Z
Electron: 43.8.3
ElectronBuildId: 15784459
Chromium: 150.0.7871.250
Node.js: 24.22.1
V8: 15.0.245.31-electron.0
@github/copilot: 1.0.103.r40031404408.gba6c003
@github/copilot-sdk: 1.0.27.40031404408.gba6c003
OS: Windows_NT x64 10.0.19045

Python 3.14.7

Clone github https://github.com/giselemachado1978-ai/Projeto-Avaliativo-Final---M-dulo-2

Venv criado pela barra " quick access" no vscode

Bibliotecas do arquivo "requirements.txt" instaladas via Terminal com comando pip install

# Pipeline construído por etapas conforme sequência abaixo:

## Fase 1: Preparação e Serialização do Modelo (Pipeline Offline)

-Download via urllib do dataset no repositório UCI e descompactação para uso.
-Treino do modelo preditivo escolhido, garantindo a divisão entre dados de treino, validação e teste e os devidos tratamentos de pré-processamento (imputação de nulos, codificação categórica e escalonamento).
-Serialização do Artefato: pipeline salvo em um arquivo binário dedicado (joblib) dentro de uma pasta apropriada do projeto 
- Relatório de Métricas

## Fase 2: Estrutura Modular da API FastAPI
Criação dos arquivos Python que compõem a arquitetura em camadas da aplicação Web

A aplicação segue uma arquitetura em camadas:
-schemas/ ou schemas.py: Definição de modelos Pydantic (BaseModel, Field) para validação estrita do JSON recebido no corpo da requisição e do JSON retornado.
    -Esquemas de Entrada e Saída: Classes herdadas de BaseModel em módulo separado (schemas.py), definindo explicitamente o contrato de dados que a API aceita e o contrato que ela devolve.
    -Uso de Tipagem e Restrições (Field): tipos estáticos adequados e regras mínimas de negócio nos atributos.
-services/ ou services.py: Módulo responsável por carregar o modelo serializado e executar a inferência matemática, desacoplando regras de negócio do protocolo HTTP.
-routers/ ou routers.py: Módulos de rota usando APIRouter agrupando os endpoints de negócio.
-main.py: Ponto de entrada da aplicação, inclusão dos roteadores e gerenciamento do ciclo de vida.


## Fase 3: Ciclo de Vida e Inicialização Otimizada (Lifespan)
Atualização dos arquivos `main.py` e `routers.py` para implementar o padrão `@asynccontextmanager` para que o modelo seja carregado somente na inicialização e compartilhado por meio de `request.app.state.model`.
OBS.: É terminantemente proibido ler o disco ou recarregar o arquivo .joblib/.pkl dentro da função da rota de predição a cada requisição HTTP recebida.

## Fase 4: Modelagem e Validação Estrita de Dados (Pydantic)

-Prevenção de Dados Inválidos: Garantir que o envio de tipos incorretos (ex.: texto em campos numéricos ou valores fora dos limites) seja interceptado automaticamente pelo Pydantic, gerando respostas com status HTTP 422 Unprocessable Entity antes de repassar os dados para o modelo preditivo.

## Fase 5: Implementação de Endpoints e Tratamento de Erros (FastAPI & HTTP)
Endpoint de Monitoramento (GET /health): Rota de checagem de integridade operacional que deve responder com status HTTP 200 OK, informando se o serviço está ativo e se o modelo de Machine Learning reside corretamente na memória RAM.
Endpoint de Inferência (POST /predict ou /v1/predict): Rota que consome o esquema de entrada validado, invoca a camada de serviço/inferência e retorna a predição no formato do esquema de saída configurado com status HTTP 200 OK.
Semântica e Tratamento de Exceções HTTP: Mapear e retornar status codes apropriados (200 OK, 400 Bad Request, 422 Unprocessable Entity ou 500 Internal Server Error), evitando que a API caia (crash) ou retorne erros sem tratamento ao usuário.
 
inicialização do servidor com Uvicorn.
Documentação da API: Exemplos de payloads JSON para chamada do endpoint /predict e link da documentação Swagger (/docs).
Links das Evidências: Link do vídeo no Google Drive.**