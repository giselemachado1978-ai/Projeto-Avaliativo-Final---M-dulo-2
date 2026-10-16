# Projeto-Avaliativo-Final---M-dulo-2
Projeto Avaliativo Final - Módulo 2

**Nome e Resumo do Projeto: 
Qual problema de negócio o modelo preditivo resolve.
Origem do Modelo: Indicar qual dos 3 projetos anteriores foi aproveitado ou descrever a base utilizada para o projeto próprio.
Tecnologias Utilizadas: Listar bibliotecas e versões (FastAPI, Pydantic, Scikit-Learn, Uvicorn, etc.).
Instruções de Instalação e Execução: Comandos para criação de ambiente virtual (venv), instalação do requirements.txt e inicialização do servidor com Uvicorn.
Documentação da API: Exemplos de payloads JSON para chamada do endpoint /predict e link da documentação Swagger (/docs).
Links das Evidências: Link do vídeo no Google Drive.**

Objetivo: Projeto Avaliativo Final - Módulo 2
Disponibilizar um modelo preditivo treinado como uma API REST pronta para consumo por aplicações externas.

Modelo escolhido (Kaggle):
 Construir, modularizar e documentar uma API Web completa com FastAPI, implementando endpoints padronizados de monitoramento de saúde (/health) e de inferência sob demanda (/predict ou /v1/predict), com esquemas de entrada e saída validados via Pydantic e ciclo de vida otimizado.

 O trabalho se apresenta conforme as etapas abaixo:

 Fase 1: Preparação e Serialização do Modelo (Pipeline Offline)
Treinar (ou refinar) o modelo preditivo escolhido, garantindo a divisão entre dados de treino, validação e teste e os devidos tratamentos de pré-processamento (imputação de nulos, codificação categórica e escalonamento).
Serialização do Artefato: Salvar o pipeline ou modelo treinado em um arquivo binário dedicado (ex.: .joblib ou .pkl) dentro de uma pasta apropriada do projeto (ex.: models/) ou usar um banco de dados sqlite, como explorado em aula ou ainda uma ferramenta mais apropriada e robusta como o MLflow.
Relatório de Métricas: Apresentar em documentação ou script auxiliar as métricas alcançadas pelo modelo selecionado (Acurácia, F1-Score, ROC-AUC, MSE/R² dependendo do tipo de problema).

Fase 2: Estrutura Modular da API FastAPI
A aplicação não pode ser um arquivo único com todo o código misturado. Deve seguir uma arquitetura em camadas:
schemas/ ou schemas.py: Definição de modelos Pydantic (BaseModel, Field) para validação estrita do JSON recebido no corpo da requisição e do JSON retornado.
services/ ou services.py: Módulo responsável por carregar o modelo serializado e executar a inferência matemática, desacoplando regras de negócio do protocolo HTTP.
routers/ ou routers.py: Módulos de rota usando APIRouter agrupando os endpoints de negócio.
main.py: Ponto de entrada da aplicação, inclusão dos roteadores e gerenciamento do ciclo de vida.

Fase 3: Ciclo de Vida e Inicialização Otimizada (Lifespan)
O arquivo serializado do modelo deve ser carregado na memória RAM uma única vez na inicialização da aplicação (utilizando @asynccontextmanager com lifespan do FastAPI).
Proibição Técnica: É terminantemente proibido ler o disco ou recarregar o arquivo .joblib/.pkl dentro da função da rota de predição a cada requisição HTTP recebida.

Fase 4: Modelagem e Validação Estrita de Dados (Pydantic)
Esquemas de Entrada e Saída: Criar classes herdadas de BaseModel em módulo separado (schemas.py), definindo explicitamente o contrato de dados que a API aceita e o contrato que ela devolve.
Uso de Tipagem e Restrições (Field): Configurar tipos estáticos adequados e regras mínimas de negócio nos atributos (ex.: faixas de valores com ge, le, gt, limites de tamanho de texto e descrições).
Prevenção de Dados Inválidos: Garantir que o envio de tipos incorretos (ex.: texto em campos numéricos ou valores fora dos limites) seja interceptado automaticamente pelo Pydantic, gerando respostas com status HTTP 422 Unprocessable Entity antes de repassar os dados para o modelo preditivo.

Fase 5: Implementação de Endpoints e Tratamento de Erros (FastAPI & HTTP)
Endpoint de Monitoramento (GET /health): Rota de checagem de integridade operacional que deve responder com status HTTP 200 OK, informando se o serviço está ativo e se o modelo de Machine Learning reside corretamente na memória RAM.
Endpoint de Inferência (POST /predict ou /v1/predict): Rota que consome o esquema de entrada validado, invoca a camada de serviço/inferência e retorna a predição no formato do esquema de saída configurado com status HTTP 200 OK.
Semântica e Tratamento de Exceções HTTP: Mapear e retornar status codes apropriados (200 OK, 400 Bad Request, 422 Unprocessable Entity ou 500 Internal Server Error), evitando que a API caia (crash) ou retorne erros sem tratamento ao usuário.
 
