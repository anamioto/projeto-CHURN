import pandas as pd
from typing import Optional

class PreProcessamento:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.df: Optional[pd.DataFrame] = None

    def carregar_dados(self) -> None:
        self.df = pd.read_csv(self.caminho_arquivo)

    def tratar_datas(self) -> None:
        for coluna in ['signup_date', 'last_purchase_date', 'cancel_date', 'data_ingestion']:
            if coluna in self.df.columns:
                self.df[coluna] = pd.to_datetime(self.df[coluna], errors='coerce')

    def preencher_nulos(self) -> None:
        self.df['city'] = self.df['city'].fillna("Desconhecido")
        self.df['payment_method'] = self.df['payment_method'].fillna("outro")
        self.df['product_category'] = self.df['product_category'].fillna("outro")
        self.df['days_since_last_purchase'] = self.df['days_since_last_purchase'].fillna(
            self.df['days_since_last_purchase'].median()
        )

    def codificar_churn(self) -> None:
        self.df['churn'] = self.df['churn'].map({'yes': 1, 'no': 0}).fillna(0).astype(int)

    def criar_colunas_derivadas(self) -> None:
        self.df['fidelidade'] = self.df['num_orders'] / (self.df['days_since_last_purchase'] + 1)
        self.df['score_gasto'] = self.df['total_spent'] * self.df['num_orders']

    def codificar_categoricas(self) -> None:
        self.df = pd.get_dummies(self.df, columns=['product_category', 'payment_method'], prefix=['cat', 'pay'])

    def salvar_dados(self, caminho_saida: str) -> None:
        self.df.to_csv(caminho_saida, index=False)

    def executar_pipeline(self, caminho_saida: str) -> None:
        self.carregar_dados()
        self.tratar_datas()
        self.preencher_nulos()
        self.codificar_churn()
        self.criar_colunas_derivadas()
        self.codificar_categoricas()
        self.salvar_dados(caminho_saida)
