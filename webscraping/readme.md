# Webscraping
Repositori d'un script per automatitzar la descarrega d'arxius PDF de la web [auladehistoria](https://auladehistoria.org). Script fet per a M04 Anàlisi Forense.

## Instal·lació batería proves
1. Baixar-se el repo (cal tenir configurat SSH a Github).
2. Entrar a la carpeta python_scripts.
```bash
cd cecti_grup2/webscraping/
```
4. Crear un venv.

```bash
python -m venv ./venv
```
3. Utilitzar [pip](https://pip.pypa.io/en/stable/) per instal·lar els paquets de l'arxiu requirements.txt.
```bash
./venv/bin/python -m pip install -r requirements.txt
```

## Execució script
```bash
./venv/bin/python -m web_scraping
```
