# Web AAC
Repositori de l'arxiu docker-compose.yml usat per crear els containers del projecte (MySQL, PHPMyAdmin i Wordpress) i dels tests fets pels membres per al 1er sprint.

## Instal·lació batería proves
1. Baixar-se el repo (cal tenir configurat SSH a Github).
2. Entrar a la carpeta python_scripts.
```bash
cd cecti_grup2/python_scripts/
```
4. Crear un venv.

```bash
python -m venv ./venv
```
3. Utilitzar [pip](https://pip.pypa.io/en/stable/) per instal·lar els paquets de l'arxiu requirements.txt.
```bash
./venv/bin/python -m pip install -r requirements.txt
```

## Execució proves
Executar prova individual
```bash
./venv/bin/python -m pytest -k nom_funcio_test
```
Executar bateria de proves
```bash
./venv/bin/python -m pytest
```
Per generar arxiu .html amb els resultats de la execució
```bash
./venv/bin/python -m pytest --html=acc_website_tests_report.html
```
