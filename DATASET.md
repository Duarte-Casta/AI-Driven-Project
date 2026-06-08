# DATASET: students_portugal.csv

## Colunas

### WLE (Weighted Likelihood Estimates)

As variáveis da escala **WLE** são índices com base na **média dos países da OCDE (fixada em 0)** e num **desvio padrão de 1**. [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/pisa-2022-technical-report_599753f0/01820d6d-en.pdf)

* **Valor 0:** Representa a média internacional da OCDE.
* **Valor Positivo ($>0$):** Indica uma presença do atributo superior à média da OCDE.
* **Valor Negativo ($<0$):** Indica uma presença do atributo inferior à média da OCDE.

--- 
### Identificadores

| Coluna | Descrição | Valores |
|--------|-----------|---------|
| `CNTSTUID` | International Student ID | Numérico (ex: 62050001.0 - 62060541.0) |
| `CNTSCHID` | International School ID | Numérico (ex: 62000159.0 - 62000227.0) |
| `STRATUM` | Stratum ID (5 caracteres: código país + ID original da região) | `PRT01` a `PRT25` + `PRT97` (ver abaixo) |

**Região (`STRATUM`) - Valores**

| Código | Região |
|--------|--------|
| PRT01 | Alentejo Central |
| PRT02 | Alentejo Litoral |
| PRT03 | Algarve |
| PRT04 | Alto Alentejo |
| PRT05 | Alto Minho |
| PRT06 | Alto Tâmega |
| PRT07 | Área Metropolitana de Lisboa |
| PRT08 | Área Metropolitana do Porto |
| PRT09 | Ave |
| PRT10 | Baixo Alentejo |
| PRT11 | Beira Baixa |
| PRT12 | Beiras e Serra da Estrela |
| PRT13 | Cávado |
| PRT14 | Douro |
| PRT15 | Lezíria do Tejo |
| PRT16 | Médio Tejo |
| PRT17 | Oeste |
| PRT18 | Região Autónoma da Madeira |
| PRT19 | Região Autónoma dos Açores |
| PRT20 | Região de Aveiro |
| PRT21 | Região de Coimbra |
| PRT22 | Região de Leiria |
| PRT23 | Tâmega e Sousa |
| PRT24 | Terras de Trás-os-Montes |
| PRT25 | Viseu Dão Lafões |
| PRT97 | Estrato não divulgado |
### Demográficos

| Coluna | Descrição | Valores |
|--------|-----------|---------|
| `STU_GENDER` | Género do aluno  | `1` = Feminino, `2` = Masculino |
| `ISCEDP` | Nível do programa de educação que o aluno frequenta (ISCED 2011) | Código de 3 dígitos (ver tabela abaixo) |

**ISCEDP - Níveis de educação (ISCED 2011):**

| Código | Descrição |
|--------|-----------|
| `244` | Ensino Básico - 3º ciclo (ISCED 2), via geral, suficiente para conclusão do nível, com acesso direto ao ensino superior |
| `344` | Ensino Secundário (ISCED 3), via geral, suficiente para conclusão do nível, com acesso direto ao ensino superior |
| `354` | Ensino Secundário (ISCED 3), via profissional, suficiente para conclusão do nível, com acesso direto ao ensino superior |

### Contexto Escolar e Académico

| Coluna | Descrição | Valores | Notas |
|--------|-----------|---------|-------|
| `REPEAT` | Repetição de ano | `0` = Nunca repetiu, `1` = Repetiu pelo menos uma vez | — |
| `EXERPRAC` | Frequência de exercício/desporto antes ou depois da escola (vezes por semana) | `0` = Nenhuma, `1` a `9` = N vezes por semana, `10` = 10 ou mais vezes por semana | — |
| `RELATST` | Qualidade das relações aluno-professor (WLE) | Score WLE (min: -10.09, max: 3.42) | **Valor positivo** relações mais positivas · **Valor negativo:** relações menos positivas |
| `BULLIED` | Índice de sofrer bullying (WLE) | Score WLE (min: -1.23, max: 4.69) | **Valor positivo:** maior índice de sofrer bullying · **Valor negativo:** menor índice de sofrer bullying |
| `FAMSUP` | Suporte familiar (WLE) | Score WLE (min: -3.87, max: 2.41) | **Valor positivo:** maior  suporte familiar · **Valor negativo:**  menor suporte familiar |
| `HISCED` | Nível de educação mais alto dos pais (ISCED) | `1` a `10` (ver tabela abaixo) | — |
| `ICTRES` | Recursos TIC (WLE) | Score WLE (min: -6.09, max: 5.29) | **Valor positivo:** mais recursos · **Valor negativo:** menos recursos |
| `ESCS` | Índice de estatuto económico, social e cultural | Score padronizado (min: -6.84, max: 7.38) | **Valor positivo:** maior nível socioeconómico · **Valor negativo:** menor nível socioeconómico |

**HISCED - Níveis de educação dos pais:**

| Valor | Descrição |
|-------|-----------|
| `1` | Abaixo do ISCED level 1 |
| `2` | ISCED level 1 (Ensino Básico - 1º ciclo) |
| `3` | ISCED level 2 (Ensino Básico - 3º ciclo) |
| `4` | ISCED level 3.3 (Secundário - profissional) |
| `5` | ISCED level 3.4 (Secundário - geral) |
| `6` | ISCED level 4 (Pós-secundário não superior) |
| `7` | ISCED level 5 (Curso superior curto - CET) |
| `8` | ISCED level 6 (Licenciatura) |
| `9` | ISCED level 7 (Mestrado) |
| `10` | ISCED level 8 (Doutoramento) |

### Escola

| Coluna | Descrição | Valores | Notas |
|--------|-----------|---------|-------|
| `SCHLTYPE` | Tipo de escola | `1` = Privada independente, `2` = Privada dependente do Estado, `3` = Pública | — |
| `SCHSIZE` | Dimensão da escola (soma de alunos) | Numérico (min: 1, max: 19201) | — |
| `TOTAT` | Número total de professores na escola  | Numérico (min: 0, max: 1025) | — |
| `PROATCE` | Proporção de professores totalmente certificados | `0.0` a `1.0` | — |
| `STRATIO` | Rácio aluno-professor | Numérico (min: 1, max: 100) | — |
| `STAFFSHORT` | Escassez de pessoal educativo (WLE) | Score WLE (min: -2.39, max: 4.50) | **Valor positivo:** maior escassez de pessoal educativo · **Valor negativo:** menor escassez de pessoal educativo |
| `EDUSHORT` | Escassez de material educativo (WLE) | Score WLE (min: -1.93, max: 3.52) | **Valor positivo:** maior escassez de material educativo · **Valor negativo:** menor escassez de material educativo |
| `SCPREPBP` | Preparação da escola para ensino remoto, antes da pandemia (WLE) | Score WLE (min: -0.83, max: 3.36) | **Valor positivo:** mais preparada · **Valor negativo:** menos preparada |
| `SCPREPAP` | Preparação da escola para ensino remoto, em resposta à pandemia (WLE) | Score WLE (min: -4.17, max: 1.82) | **Valor positivo:** melhor resposta à pandemia · **Valor negativo:** pior resposta à pandemia |
| `PROBSCRI` | Problemas com a capacidade da escola para fornecer ensino remoto (WLE) | Score WLE (min: -3.04, max: 3.73) | **Valor positivo:** mais problemas · **Valor negativo:** menos problemas |
| `CV19_ONLINE_CLASS` | Durante os confinamentos COVID: aulas foram lecionadas remotamente usando dispositivos digitais | `1` = Nenhuma das aulas, `2` = Menos de metade, `3` = Cerca de metade, `4` = Mais de metade, `5` = Todas ou quase todas | — |
| `CV19_CANCELLED_CLASS` | Durante os confinamentos COVID: aulas foram canceladas e não substituídas por ensino remoto | `1` = Nenhuma das aulas, `2` = Menos de metade, `3` = Cerca de metade, `4` = Mais de metade, `5` = Todas ou quase todas | — |

### Professores (agregados por escola)

| Coluna | Descrição | Valores |
|--------|-----------|---------|
| `TC_GENDER_MEAN` | Média do género dos professores por escola | ~`1.0` (maioritariamente feminino) a ~`2.0` (maioritariamente masculino) |
| `TC_AGE_MEAN` | Média de idades dos professores por escola (anos) | Numéricos |
| `TC_EXP_MEAN` | Média de experiência dos professores por escola (anos) | Numéricos |
| `TC_PERM_PERC` | Percentagem de professores com contrato efetivo | `0.0` a `1.0` |

### Valores Plausíveis - Matemática, Leitura e Literacia Financeira

| Coluna | Descrição | Intervalo típico |
|--------|-----------|------------------|
| `PV1MATH` a `PV10MATH` | Valores plausíveis 1-10 em Matemática | 0 a 1000 |
| `PV1READ` a `PV10READ` | Valores plausíveis 1-10 em Leitura | 0 a 1000 |
| `PV1FLIT` a `PV10FLIT` | Valores plausíveis 1-10 em Literacia Financeira | 0 a 1000 |

### Valores Plausíveis - Pensamento Criativo

| Coluna | Descrição | Intervalo típico |
|--------|-----------|------------------|
| `PV1CRTH_NC` a `PV10CRTH_NC` | Valores plausíveis 1-10 em Pensamento Criativo (Number Correct) | 0 a 60 |

> **Nota:** As variáveis `PV*CRTH_NC` têm dados disponíveis para ~6793 de 10868 registos (os restantes são alunos que não fizeram esta avaliação).

## Notas
- Descartadas por elevada correlação com outras variáveis:

`ISCEDP` - Levels of education programmes (ISCED 2011)

`HISCED` - Highest level of education of parents (ISCED)

`TC_EXP_MEDIA` - mean teacher experience per school (years)
