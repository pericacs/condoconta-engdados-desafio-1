<!-- Um profissional de Business intelligence da sua companhia te enviou a seguinte demanda:

"Preciso de uma tabela para acompanhar os dados de commits do repositório https://github.com/openai/openai-python *por dia e por autor* para o mês 5 do ano de 2023. A partir dessa tabela irei construir visualizações de dados".

Foi decidido que essa demanda será realizada em duas etapas:

Extração de dados para um datalake, salvando os mesmos em arquivos .json.
Tratamento dos dados e criação da tabela para uso do profissional de Business intelligence.
Dado esse contexto:

Crie um script em python capaz de ler os dados de commits do repositório https://github.com/openai/openai-python.
Esse script deve usar a API pública do github https://docs.githu
b.com/en/rest?apiVersion=2022-11-28.

Durante a execução do script o usuário deve fazer o input de sua token de acesso ao github no terminal. Utilizar o método input().

O script deve acessar os dados de commit e salvar todos os dados obtidos em formato json no mesmo diretório de execução do script.

Crie um segundo script em python capaz de ler os dados extraídos em formato json e prepará-los para serem utilizados em ferramentas de Business Inteligence. Os dados tratados devem conter a contagem de commits realizados por dia e por autor no mês 05/2023.

Os dados tratados devem estar em uma tabela em csv e também devem ser salvos no mesmo diretório de execução do script.
A tabela dos dados tratados deve apresentar uma surrogate key adequada para identificar de forma única os registros.
openai/openai-python
Website
https://pypi.org/project/openai/ -->


<!-- Token que utilizei para para processar os commits no input: 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 -->