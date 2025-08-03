# Projeto CHURN - Predição de Evasão de Clientes

## 📋 Visão Geral

Este projeto implementa um sistema de Machine Learning para predição de churn (evasão) de clientes, utilizando técnicas avançadas de análise de dados e algoritmos de classificação para identificar clientes com alta probabilidade de cancelamento. 

> Esta é uma **proposta de documentação**, como parte do curso da Alura de Princípios de Engenharia de Software para Cientistas de Dados.
>> Fique a vontade para clonar, fazer as modificações necessárias e aplicar **boas práticas em seus projetos**.

## 🎯 Objetivos

- **Objetivo Principal**: Desenvolver um modelo preditivo para identificar clientes propensos ao churn
- **Objetivos Específicos**:
  - Analisar padrões comportamentais dos clientes
  - Implementar e comparar diferentes algoritmos de ML
  - Fornecer insights acionáveis para retenção de clientes
  - Criar visualizações interpretáveis dos resultados

## 🏗️ Arquitetura do Projeto
*- Apresentar toda a arquitetura e design do projeto.*
> Neste repositório temos duas pastas: Churn-DEPOIS e Churn-ANTES
>> Churn-DEPOIS representa como ficou o projeto após a aplicação das boas práticas na estrutura e design.
>> Churn-ANTES representa um projeto legado e sem as boas práticas.
>> Ambos contém arquivos demonstrativos e vazios. Durante o curso é demonstrado quais são os arquivos com conteúdo e que deverão ser utilizados.
  
```
projeto-CHURN/
├── Churn-depois/
│   ├── data/                    # Datasets e arquivos de dados
│   │   ├── raw/                 # Dados brutos
│   │   ├── processed/           # Dados processados
│   │   └── external/            # Dados externos
│   ├── notebooks/               # Jupyter notebooks
│   │   ├── 01_exploratory_analysis.ipynb
│   │   ├── 02_data_preprocessing.ipynb
│   │   ├── 03_feature_engineering.ipynb
│   │   └── 04_model_training.ipynb
│   ├── src/                     # Código fonte
│   │   ├── data/                # Scripts de processamento de dados
│   │   ├── features/            # Scripts do processo de Feature engineering
│   │   ├── models/              # Scripts de treinamento/teste dos Modelos de ML
│   │   └── visualization/       # Scripts de visualização
│   ├── models/                  # Modelos treinados salvos
│   ├── doc/                 # Relatórios, documentações extras e figuras
│   │   └── figures/         # Figuras
|   |   └── apresentations/  # Apresentações de slides
|   |   └── reports/         # Apresentações executivas
│   ├── requirements.txt         # Dependências
│   └── README.md               # Documentação principal
```

## 🔧 Tecnologias Utilizadas

### Linguagens e Frameworks
- **Python 3.8+**: Linguagem principal
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica
- **Scikit-learn**: Algoritmos de Machine Learning
- ...

### Visualização
- **Matplotlib**: Gráficos básicos
- **Seaborn**: Visualizações estatísticas
- ...

### Ferramentas de Desenvolvimento
- **Jupyter Notebook**: Desenvolvimento interativo
- **Git**: Controle de versão
- **Pip**: Gerenciamento de dependências
- ...

## 📊 Metodologia

### 1. Análise Exploratória
- Estatísticas descritivas dos dados
- Identificação de padrões e outliers
- Análise de correlações entre variáveis
- Visualização da distribuição do target (churn)
- ...

### 2. Pré-processamento
- Tratamento de valores ausentes
- Codificação de variáveis categóricas
- Normalização/padronização de features numéricas
- Divisão dos dados (train/validation/test)
- ...

### 3. Feature Engineering
- Criação de novas variáveis derivadas
- Seleção de features relevantes
- Tratamento de desbalanceamento de classes
- ...

### 4. Modelagem
Algoritmos implementados:
- **Logistic Regression**: Modelo baseline
- **Modelo 2**: Modelo de x
- ...

### 5. Avaliação
Métricas utilizadas:
- **Accuracy**: Precisão geral
- **Precision**: Precisão por classe
- **Recall**: Sensibilidade
- **F1-Score**: Média harmônica
- **Confusion Matrix**: Matriz de confusão
- ...

## 🚀 Como Executar

### Pré-requisitos
```bash
# Python 3.8 ou superior
python --version

# Git para clonar o repositório
git --version
```

### Instalação
*- Breve explicação de como instalar/rodar o seu projeto.*
  
```bash
# 1. Clone o repositório
git clone https://github.com/anamioto/projeto-CHURN.git
cd projeto-CHURN/Churn-depois

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

### Execução
*- Explicação da ordem do seu pipeline e como rodar de forma individual cada etapa.*

```bash
# 1. Execute os notebooks na ordem
jupyter notebook notebooks/01_exploratory_analysis.ipynb
jupyter notebook notebooks/02_data_preprocessing.ipynb
jupyter notebook notebooks/03_feature_engineering.ipynb
jupyter notebook notebooks/04_model_training.ipynb

# 2. Ou execute scripts individuais
python src/data/process_data.py
python src/models/train_model.py
python src/models/evaluate_model.py
```

## 📈 Resultados Principais

### Performance dos Modelos
*- Apresentar um comparativo dos resultados dos modelos.*

| Modelo | Accuracy | Precision | Recall | F1-Score | 
|--------|----------|-----------|--------|----------|
| LogisticRegression | 0.69 | 0.70 | 0.41 | 0.81 | 
| Modelo 2 | 0.00 | 0.00 | 0.00 | 0.00 | 
| Modelo 3 | 0.00 | 0.00 | 0.00 | 0.00 | 

### Features Mais Importantes
*- Destacar as features mais importantes, exemplo:*
  
1. **Tenure** (tempo como cliente)
2. **Monthly Charges** (cobrança mensal)
3. **Total Charges** (cobrança total)
4. **Contract Type** (tipo de contrato)
5. **Payment Method** (método de pagamento)

### Insights de Negócio
*- Adicionar achados e tomadas de decisões feitas.*

## 📁 Estrutura dos Dados

### Dataset Principal
*- Apresentar uma breve descrição do dataset utilizado.*
- **Registros**: ~7,000 clientes
- **Features**: 21 variáveis
- **Target**: Churn (0: Não, 1: Sim)
- **Taxa de Churn**: 26.5%

### Principais Variáveis
*- Apresentar quais são as variáveis utilizadas.*
- **Demográficas**: Gender, SeniorCitizen, Partner, Dependents
- **Serviços**: PhoneService, InternetService, OnlineSecurity
- **Contratuais**: Contract, PaperlessBilling, PaymentMethod
- **Financeiras**: MonthlyCharges, TotalCharges, Tenure

## 🔄 Pipeline de ML
*- Descrever como rodar o pipeline criado.*

```python
# Exemplo simplificado do pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=100))
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

## 📚 Dependências
*- Destacar as dependências de bibliotecas e suas versões minimas necessarias para rodar o projeto.*

```txt
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

## 🤝 Contribuindo
*- Um passo-a-passo para incentivar que novas ideias ou melhorias possam ser feitas no seu projeto.*

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-feature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. **Push** para a branch (`git push origin feature/nova-feature`)
5. Abra um **Pull Request**

## 📝 Próximos Passos
*- Apresentar quais são as ideias de melhoria e próximos passos a serem desenvolvidos.*

### Melhorias Técnicas
- [ ] Implementar validação cruzada estratificada
- [ ] Otimização de hiperparâmetros com Optuna
- [ ] Implementar SHAP para interpretabilidade
- [ ] Deploy do modelo em produção

### Análises Adicionais
- [ ] Análise de cohort dos clientes
- [ ] Segmentação de clientes (clustering)
- [ ] Análise temporal do churn
- [ ] A/B testing para estratégias de retenção

## 👥 Autor
*- Descreva brevemente quem é você e sua formação.*

**Ana Clara Mioto**
- GitHub: [@anamioto](https://github.com/anamioto)
- Formação: Bacharel em Informática Biomédica, Mestre em Bioengenharia
- Especialização: Data Science e Machine Learning

## 📄 Licença

*Adicionar licença ao projeto caso haja.*

## 📞 Contato

Para dúvidas, sugestões ou colaborações:
- **Issues**: Abra uma issue no GitHub
- **Email**: [incluir email]
- **LinkedIn**: [incluir perfil]
- **Instagram**: @ana_mioto

---

## 🔍 Glossário
*- Explicação/significado de termos de négocio e técnicos para entendimendo do seu projeto.*

- **Churn**: Taxa de evasão/cancelamento de clientes
- **Feature Engineering**: Processo de criação e seleção de variáveis
- **Pipeline**: Sequência automatizada de processamento
- **Cross-validation**: Técnica de validação de modelos
- **Ensemble**: Combinação de múltiplos modelos
- ...

---

*Documentação atualizada em: Agosto 2025*
