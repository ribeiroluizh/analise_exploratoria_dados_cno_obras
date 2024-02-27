# Análise Exploratória de Dados do Cadastro Nacional de Obras - CNO
Fontes: [Site Oficial Dados Gov.Br](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-de-obras-cno)

### Resumo
O Cadastro Nacional de Obras (CNO) é o banco de dados, administrado pela Secretaria Especial da Receita Federal do Brasil (RFB), que armazena informações cadastrais de obras de construção civil e de seus responsáveis. Este cadastro é necessário para que o contribuinte possa cumprir as suas obrigações tributárias (entregar declarações e realizar pagamentos) e, ao final da obra, obter a certidão de regularidade fiscal relativa à obra.

#### Descrição
O Cadastro Nacional de Obras (CNO) é o banco de dados, administrado pela Secretaria Especial da Receita Federal do Brasil (RFB), que armazena informações cadastrais de obras de construção civil e de seus responsáveis. Este cadastro é necessário para que o contribuinte possa cumprir as suas obrigações tributárias (entregar declarações e realizar pagamentos) e, ao final da obra, obter a certidão de regularidade fiscal relativa à obra.

#### Recursos de Dados
##### Dicionário de Dados do Cadastro Nacional de Obras - CNO
O arquivo relaciona as informações que possibilitam organizar, classificar, relacionar e inferir novos dados sobre o conjunto de dados do Cadastro Nacional de Obras. <br>
Arquivo.PDF | [Acesse](https://www.gov.br/receitafederal/dados/cno-metadados.pdf)

Arquivo de Trabalho CSV | [Acesse]()

***

Licença: Creative Commons Atribuição
 Formatos: PDF; zip+csv;
 Atualização: -
 Última alteração: 24/11/2022 14:43:55

 ***

#### Sobre o arquivo de dados.
O arquivo de dados é muito extenso e contém mais de 2 milhões de dados, para isso, antes de iniciar minha análise, eu 
optei por converter o arquivo .csv para .parquet, de forma simples. E esta manipulação não se encontra no código-fonte.

### Legendas:
#### Qualificação do responsável
Qualificação do responsável pela obra <br>
0070 - Proprietário do Imóvel <br>
0057 - Dono da Obra <br>
0064 - Incorporador de Construção Civil <br>
0053 - Pessoa Jurídica Construtora <br>
0111 - Sociedade Líder de Consórcio <br>
0109 - Consórcio <br>
0110 - Construção em nome coletivo <br>
#### Situação
Situação da obra
01 - NULA <br>
02 - ATIVA <br>
03 – SUSPENSA <br>
14 - PARALISADA <br>
15 - ENCERRADA <br>
