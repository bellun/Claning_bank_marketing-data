# Cleaning_bank_marketing-data
Projeto para limpeza de dados

<img width="773" height="505" alt="image" src="https://github.com/user-attachments/assets/9b9990ca-02ed-49be-89a3-a14675a02d53" />

Os empréstimos pessoais representam uma das fontes de receita mais estratégicas para o setor bancário. No Reino Unido, por exemplo, uma taxa média de 10%([referência](https://www.experian.com/blogs/ask-experian/whats-a-good-interest-rate-for-a-personal-loan/)) ao ano em empréstimos de 24 meses pode gerar retornos expressivos – especialmente quando consideramos que apenas em setembro de 2022, o volume captado pelos consumidores ultrapassou £1.5([artigo uk finance](https://www.ukfinance.org.uk/system/files/2022-12/Household%20Finance%20Review%202022%20Q3-%20Final.pdf)) bilhão, potencialmente gerando £300 milhões em juros ao final do período.

# 📊 Projeto de Preparação de Dados de Marketing Bancário

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Compatible-blue?logo=postgresql)
![Status](https://img.shields.io/badge/status-finalizado-brightgreen)

Neste projeto, trabalhei com dados de marketing de um banco, preparando as informações para análise e armazenamento em banco de dados.



## 🧱 Organização dos Dados

- Dividi o arquivo original em três conjuntos lógicos:
  - Informações de **clientes**
  - Dados da **campanha**
  - **Indicadores econômicos**
- Garanti que cada tabela contivesse apenas as colunas necessárias.
- Padronizei os nomes das colunas para facilitar a integração.



## 🧹 Limpeza e Padronização

- Corrigi valores inconsistentes nas colunas de **educação** e **profissão**.
- Padronizei respostas booleanas (`sim/não` → `True/False`).
- Tratei adequadamente os **valores faltantes**.
- Criei uma coluna de **data formatada corretamente** a partir dos campos separados de mês e dia.



## 🧪 Preparação para Análise

- Ajustei os **tipos de dados** para garantir consistência.
- Exportei os dados limpos em arquivos `.CSV` prontos para uso.
- Mantive a estrutura compatível com **PostgreSQL**, facilitando a integração com banco de dados.



## ✅ Resultado

O resultado foi um conjunto de dados **organizado e padronizado**, pronto para alimentar análises e campanhas futuras.

Essa preparação permite que a equipe de marketing trabalhe com **informações confiáveis e consistentes**, além de facilitar a incorporação de novos dados conforme novas campanhas forem realizadas.


## ⚙️ Tecnologias Utilizadas

- Python (pandas, numpy)
- PostgreSQL
- Jupyter Notebook




