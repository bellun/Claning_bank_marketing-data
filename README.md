# Claning_bank_marketing-data
Projeto para limpeza de dados

Os empréstimos pessoais representam uma das fontes de receita mais estratégicas para o setor bancário. No Reino Unido, por exemplo, uma taxa média de 10%([referência](https://www.experian.com/blogs/ask-experian/whats-a-good-interest-rate-for-a-personal-loan/)) ao ano em empréstimos de 24 meses pode gerar retornos expressivos – especialmente quando consideramos que apenas em setembro de 2022, o volume captado pelos consumidores ultrapassou £1.5([artigo uk finance](https://www.ukfinance.org.uk/system/files/2022-12/Household%20Finance%20Review%202022%20Q3-%20Final.pdf)) bilhão, potencialmente gerando £300 milhões em juros ao final do período.

Neste projeto, trabalhei com dados de marketing de um banco, preparando as informações para análise e armazenamento em banco de dados. O trabalho envolveu:

Organização dos dados:

Dividi o arquivo original em três conjuntos lógicos: informações de clientes, dados da campanha e indicadores econômicos

Garanti que cada tabela contivesse apenas as colunas necessárias

Padronizei os nomes das colunas para facilitar a integração

Limpeza e padronização:

Corrigi valores inconsistentes nas colunas de educação e profissão

Converti respostas como "sim/não" para valores booleanos (True/False)

Tratei adequadamente os valores faltantes

Criei uma coluna de data formatada corretamente a partir dos campos separados de mês e dia

Preparação para análise:

Assegurei que cada campo tivesse o tipo de dado correto

Exportei os dados limpos em arquivos CSV prontos para uso

Mantive a estrutura necessária para fácil integração com PostgreSQL

O resultado foi um conjunto de dados organizado e padronizado, pronto para alimentar análises e campanhas futuras. Essa preparação permite que a equipe de marketing trabalhe com informações confiáveis e consistentes, além de facilitar a incorporação de novos dados à medida que novas campanhas forem realizadas.
