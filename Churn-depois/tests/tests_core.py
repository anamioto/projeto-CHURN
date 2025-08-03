import pandas as pd
import pytest
import os

from pre_processamento import PreProcessamento

# Setup: criar um DataFrame de teste e salvar como CSV
@pytest.fixture
def dados_csv(tmp_path):
    df = pd.DataFrame({
        'customer_id': [1, 2],
        'signup_date': ['2022-01-01', '2022-01-15'],
        'last_purchase_date': ['2022-01-20', '2022-02-01'],
        'product_category': ['eletronico', None],
        'total_spent': [1000.0, 500.0],
        'num_orders': [10, 5],
        'cancel_date': [None, None],
        'data_ingestion': ['2022-02-05', '2022-02-10'],
        'city': ['São Paulo', None],
        'payment_method': ['pix', 'boleto'],
        'product_id': ['A1', 'B2'],
        'churn': ['no', 'yes'],
        'days_since_last_purchase': [10, None]
    })
    caminho = tmp_path / "clientes_teste.csv"
    df.to_csv(caminho, index=False)
    return str(caminho)

# Teste: execução completa do pipeline
def test_pipeline_completo(dados_csv, tmp_path):
    saida = tmp_path / "clientes_processados.csv"
    proc = PreProcessamento(dados_csv)
    proc.executar_pipeline(str(saida))

    df_resultado = pd.read_csv(saida)

    # Verifica se arquivo foi gerado
    assert os.path.exists(saida)

    # Verifica colunas criadas
    assert 'fidelidade' in df_resultado.columns
    assert 'score_gasto' in df_resultado.columns
    assert any(col.startswith("cat_") for col in df_resultado.columns)
    assert any(col.startswith("pay_") for col in df_resultado.columns)

    # Verifica tipo da coluna churn
    assert df_resultado['churn'].isin([0, 1]).all()

# Teste: tratamento de nulos
def test_preenchimento_nulos(dados_csv):
    proc = PreProcessamento(dados_csv)
    proc.carregar_dados()
    proc.preencher_nulos()

    assert proc.df['city'].isnull().sum() == 0
    assert proc.df['product_category'].isnull().sum() == 0
    assert proc.df['payment_method'].isnull().sum() == 0
    assert proc.df['days_since_last_purchase'].isnull().sum() == 0

# Teste: transformação de datas
def test_tratamento_datas(dados_csv):
    proc = PreProcessamento(dados_csv)
    proc.carregar_dados()
    proc.tratar_datas()

    assert pd.api.types.is_datetime64_any_dtype(proc.df['signup_date'])
    assert pd.api.types.is_datetime64_any_dtype(proc.df['last_purchase_date'])
    assert pd.api.types.is_datetime64_any_dtype(proc.df['data_ingestion'])

# Teste: codificação de churn
def test_codificacao_churn(dados_csv):
    proc = PreProcessamento(dados_csv)
    proc.carregar_dados()
    proc.codificar_churn()

    assert set(proc.df['churn'].unique()).issubset({0, 1})