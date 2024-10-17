# Tests Web AAC
Repositori dels tests fets pels membres dels grups 3 i 4 per al 1er sprint.

## Instal·lació
1. Baixar-se el repo.
2. Crear un venv.

```bash
python -m venv ./venv
```
3. Utilitzar [pip](https://pip.pypa.io/en/stable/) per instal·lar els paquets de l'arxiu requirements.txt.
```bash
./venv/bin/python -m pip install -r requirements.txt
```

## Execució
Executar test individual
```bash
.venv/bin/python -m pytest -k nom_funcio_test
```
Executar bateria de proves
```bash
.venv/bin/python -m pytest
```
Per generar arxiu .html amb els resultats de la execució
```bash
.venv/bin/python -m pytest --html=acc_website_tests_report.html
```
