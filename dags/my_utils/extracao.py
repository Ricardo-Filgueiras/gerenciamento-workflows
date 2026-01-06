# importações
from pathlib import Path
# from airflow.macros import ds_add

def helo():
    print("hello world")
    
# funções de extração de dados 
def tags(tag):
    
    import os 
    import yfinance as yf
    import pandas as pd

    ticker = tag
    petro = yf.Ticker(ticker)
    historico = petro.history(period="1mo")
    historico['acao_tag'] = ticker
    historico.reset_index(inplace=True)
     
    # Caminho absoluto baseado na raiz do projeto
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    historico.to_json(str(data_dir / f"{ticker[:4]}.json"))
    historico.to_csv(str(data_dir / f"{ticker[:4]}.csv"))

# criar funcão de extração para múltiplas ações 
def get_history(ticker, ds=None, ds_nodash=None): 
    file_path = f'/opt/airflow/data/stock/{ticker}/{ticker}_{ds_nodash}.csv'
    Path(file_path).parent.mkdir(parents=True, exist_ok=True) 
    yf.Ticker(ticker).history(
        period ="1d",
        interval = "1h",
        start = ds_add(ds, -1) ,
        end = ds ,
        prepost = True
    ).to_csv(file_path)