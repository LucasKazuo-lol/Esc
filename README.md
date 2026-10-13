# Estudos de Python e PL/SQL

Repositório de exercícios para praticar lógica de programação, listas, classes em Python e estruturas de repetição em PL/SQL.

## Conteúdo

| Arquivo | Objetivo |
| --- | --- |
| [notas.py](notas.py) | Ler notas e calcular média, maior e menor valor, contagens e classificação de desempenho. |
| [Python/classe.py](Python/classe.py) | Criar objetos com nome e idade e praticar métodos de instância. |
| [Python/hello.py](Python/hello.py) | Trabalhar com listas, inserção de elementos e laços de repetição. |
| [PL.sql](PL.sql) | Praticar `LOOP`, `FOR`, `WHILE`, condições e geração de números aleatórios. |

## Como executar os exemplos Python

Requisito: Python 3. Não há dependências externas.

```bash
git clone https://github.com/LucasKazuo-lol/Esc.git
cd Esc
python notas.py
```

Informe uma quantidade de notas maior que zero e depois digite os valores solicitados. Use ponto como separador decimal, por exemplo `7.5`.

Os outros exemplos são independentes:

```bash
python Python/classe.py
python Python/hello.py
```

No Windows, também é possível usar `py` no lugar de `python`.

## Como executar os exemplos PL/SQL

O arquivo `PL.sql` contém três blocos anônimos para um ambiente compatível com Oracle PL/SQL.

Execute um bloco por vez e habilite a exibição de `DBMS_OUTPUT` na ferramenta utilizada. No SQL*Plus ou no modo de script do SQL Developer, use `SET SERVEROUTPUT ON` e adicione uma linha com `/` após cada bloco.

## Sobre o repositório

Os arquivos são exercícios de aprendizagem e podem evoluir conforme os estudos. O programa de notas pressupõe entradas numéricas válidas e uma quantidade de notas positiva.

## Autor

[Lucas Kazuo](https://github.com/LucasKazuo-lol)
