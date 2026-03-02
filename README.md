# 📈 Análise Estatística: Tabela FIPE 2022

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status">
</p>

> **Análise Descritiva de Dados:** Script automatizado para processamento estatístico de dados automotivos, focado em extrair métricas de tendência central e dispersão da base de dados FIPE 2022.

---

## 🎯 Objetivo do Projeto
Este trabalho aplica conceitos fundamentais de **Estatística Descritiva** para diagnosticar o comportamento do mercado de carros usados. Utilizando a biblioteca `Pandas`, o script realiza o pipeline completo: desde a ingestão e limpeza até a geração de um relatório técnico detalhado.

---

## 📊 Inteligência Estatística

O motor de análise foca em duas frentes principais para entender os dados:

### 🔹 Medidas de Tendência Central
* **Média:** Identifica o perfil médio de fabricação da frota.
* **Mediana:** Define o ponto central da idade dos veículos, mitigando distorções de *outliers*.
* **Moda:** Aponta o valor de mercado com maior recorrência (densidade).

### 🔹 Medidas de Dispersão
* **Amplitude:** Define o espectro temporal (Gap entre o clássico e o novo).
* **Desvio Padrão:** Mensura a volatilidade e variação dos preços em torno da média.
* **Variância:** Quantifica a dispersão estatística da idade da frota.

---

## ⚙️ Pipeline de Dados
O fluxo de execução foi desenhado para ser eficiente e limpo:

1.  **Ingestão Seletiva:** Carregamento apenas das colunas necessárias para otimizar o uso de memória.
2.  **Tratamento (Data Cleaning):** Eliminação de registros inconsistentes ou nulos via `dropna`.
3.  **Engine Estatística:** Processamento vetorial das métricas via métodos nativos do Pandas.
4.  **Output:** Relatório formatado no console com máscaras de moeda brasileira (BRL).

---

## 💻 Visualização do Relatório

Ao executar o sistema, você obterá um dashboard textual organizado:

```text
============================================================
        TRABALHO DE ESTATÍSTICA - TABELA FIPE 2022
============================================================
MÉDIA (Ano do Modelo):        2012
MEDIANA (Idade dos Carros):   10.0 anos
MODA (Preço Médio):           R$ 35.000,00
------------------------------------------------------------
AMPLITUDE (Ano):              37 anos (De 1985 a 2022)
DESVIO PADRÃO (Preço):        R$ 45.230,15
VARIANTE/VARIÂNCIA (Idade):   54.20
------------------------------------------------------------
Total de registros analisados: 15420 linhas.
============================================================