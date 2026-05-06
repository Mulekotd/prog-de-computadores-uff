# Relatório - Las Vegas Casino

## 1. Introdução

Este documento apresenta o sistema de gerenciamento de cassino desenvolvido como projeto da disciplina de Programação 1. O sistema implementa funcionalidades completas de CRUD (Create, Read, Update, Delete) para gerenciamento de apostas, clientes, jogos e movimentações financeiras, utilizando arquivos de texto como mecanismo de persistência de dados.

## 2. Decisões de Projeto

### 2.1 Estrutura de Diretórios

A arquitetura do projeto adota uma organização hierárquica que prioriza a separação lógica entre os componentes do sistema. Esta estrutura estabelece uma clara distinção entre o código-fonte da aplicação, os conjuntos de dados de entrada e os arquivos de saída gerados durante a execução do programa. Tal abordagem visa promover a manutenibilidade do código e facilitar a compreensão da organização dos artefatos do sistema.

### 2.2 Estratégia de Geração de Dados

A fim de otimizar o processo de recuperação de informações, implementou-se uma estratégia de indexação durante a fase de criação dos arquivos de dados. Especificamente, foi incorporada uma coluna identificadora única (id) para cada registro das entidades do programa. Esta decisão proporciona um mecanismo eficiente de busca e referenciamento de entidades, eliminando a necessidade de varreduras sequenciais completas e reduzindo a complexidade algorítmica das operações de leitura de dados.

### 2.3 Modelagem Orientada a Objetos

Nesta abordagem, cada classe corresponde de forma biunívoca a um arquivo específico, de modo que os atributos das classes espelham fielmente as colunas presentes nos respectivos arquivos. Este paradigma assegura a consistência estrutural entre a camada de persistência e a camada de domínio da aplicação.

<div style="page-break-after: always;"></div>

### 2.4 Classe Especializada em Manipulação de Arquivos

Para encapsular as operações de entrada e saída em arquivos de texto, foi desenvolvida uma classe especializada denominada `File`. Esta classe implementa métodos específicos para as operações fundamentais de manipulação de arquivos, incluindo leitura, escrita, adição de conteúdo e extração de dados.

### 2.5 Arquitetura do Módulo Principal

O módulo `main.py` foi estruturado seguindo o princípio da responsabilidade única. A implementação adota uma abordagem minimalista, na qual a complexidade lógica e operacional é integralmente delegada à classe auxiliar `Program`. Esta decisão arquitetural promove a clareza do ponto de entrada da aplicação, concentrando as responsabilidades de coordenação do sistema em componentes especializados.

<div style="page-break-after: always;"></div>

## 3. Análise de Desempenho

Com o objetivo de avaliar a eficiência das operações, foram realizadas medições de tempo em cada etapa individual do projeto.

### 3.1 Primeira Etapa - Geração de Dados

A tabela abaixo apresenta os tempos de execução do script `hydration.py`:

| **Arquivo**          | **Tempo de Execução** |
| -------------------- | --------------------- |
| `movimentations.txt` | 325.86 ms             |
| `bets.txt`           | 66.25 ms              |
| `clients.txt`        | 6.98 ms               |
| `games.txt`          | 0.90 ms               |

### 3.2 Segunda Etapa - Carregamento Inicial

A tabela seguinte demonstra os tempos necessários para o carregamento dos arquivos de texto pelo programa principal durante sua inicialização:

| **Arquivo**          | **Tempo de Execução** |
| -------------------- | --------------------- |
| `movimentations.txt` | 32.31 ms              |
| `bets.txt`           | 46.09 ms              |
| `clients.txt`        | 30.44 ms              |
| `games.txt`          | 23.11 ms              |

<div style="page-break-after: always;"></div>

### 3.3 Terceira Etapa - Operações CRUD

As tabelas a seguir apresentam os tempos de execução das operações de manipulação de dados para cada entidade do sistema.

#### 3.3.1 Apostas

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 881.86 ms             |
| Visualizar | 0.51 ms               |
| Adicionar  | 0.08 ms               |
| Editar     | 0.07 ms               |
| Excluir    | 0.32 ms               |

#### 3.3.2 Clientes

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 120.99 ms             |
| Visualizar | 0.48 ms               |
| Adicionar  | 0.06 ms               |
| Editar     | 0.04 ms               |
| Excluir    | 0.37 ms               |

<div style="page-break-after: always;"></div>

#### 3.3.3 Jogos

A entidade jogos apresenta os menores tempos de listagem, resultado da quantidade reduzida de dados comparado às demais entidades.

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 2.61 ms               |
| Visualizar | 0.54 ms               |
| Adicionar  | 0.05 ms               |
| Editar     | 0.05 ms               |
| Excluir    | 0.37 ms               |

#### 3.3.4 Movimentações

As movimentações financeiras exibem o maior tempo de listagem dentre todas as entidades, o que é esperado considerando o alto volume de transações registradas.

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 4018.12 ms            |
| Visualizar | 0.55 ms               |
| Adicionar  | 0.05 ms               |
| Editar     | 0.04 ms               |
| Excluir    | 0.51 ms               |

### 3.4 Persistência de Dados ao Encerramento

Ao finalizar o programa, os dados são persistidos em arquivos de saída localizados no diretório `output/`. O tempo médio necessário para a geração completa desses arquivos é de aproximadamente **6934.90 ms**, garantindo que todas as alterações realizadas durante a execução sejam preservadas.
