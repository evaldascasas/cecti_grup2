import requests
from bs4 import BeautifulSoup
import re
import os
import zipfile
import subprocess

# Definir els headers per a la petició GET
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Petició GET inicial per obtenir enllaços de la pàgina principal
try:
    url = "https://auladehistoria.org/temario-oposiciones-geografia-historia/"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracció d'enllaços de temes i annexos
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if "tema-" in href or "anexo" in href or "album-61" in href:
            links.append(href)

    # Desar els enllaços en un fitxer txt
    with open("links.txt", "w") as file:
        for link in links:
            file.write(link + "\n")

    print(f"[INFO] Els enllaços s'han guardat en links.txt. Total enllaços trobats: {len(links)}")
except requests.exceptions.RequestException as e:
    print("Error en la connexió:", e)

# Llegir els enllaços des de links.txt
with open("links.txt", "r") as file:
    links = [line.strip() for line in file.readlines()]

# Patró per cercar els enllaços dels PDFs en el codi JavaScript
pattern = re.compile(r'window\.df_option_\d+\s*=\s*\{[^}]*"source"\s*:\s*"([^"]+\.pdf)"')

# Fitxer per guardar els enllaços dels PDFs trobats
with open("download_links.txt", "w") as output_file:
    for index, link in enumerate(links, start=1):
        print(f"[INFO] Processant enllaç {index}/{len(links)}: {link}")
        try:
            # Realitzar la petició GET per carregar la pàgina del temari
            response = requests.get(link, headers=headers)

            # Comprovar si la petició ha estat exitosa
            if response.status_code == 200:
                print(f"[INFO] Pàgina carregada correctament: {link}")
            else:
                print(f"[ERROR] No s'ha pogut carregar la pàgina: {link}")
                continue

            # Buscar els enllaços als PDFs mitjançant la regex
            matches = pattern.findall(response.text)
            if matches:
                for match in matches:
                    output_file.write(match + "\n")
                    print(f"[ENLLAÇ TROBAT] {match}")
            else:
                print(f"[INFO] No s'han trobat enllaços de descàrrega en la pàgina: {link}")
        except Exception as e:
            print(f"[ERROR] Error en accedir a {link}: {e}")

print("Extracció completa! Els enllaços s'han guardat a download_links.txt")

# Crear la carpeta per desar els PDFs descarregats
os.makedirs("pdfs", exist_ok=True)

# Llegir els enllaços des de download_links.txt
with open("download_links.txt", "r") as file:
    links = [line.strip().replace("\\", "") for line in file.readlines()]  # Normalitzar les URLs

# Descarregar cada PDF amb wget
for index, link in enumerate(links, start=1):
    print(f"[INFO] Descarregant {index}/{len(links)}: {link}")
    try:
        subprocess.run(["wget", "-P", "pdfs", link], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error en descarregar {link}: {e}")

# Crear un fitxer ZIP amb tots els PDFs descarregats
with zipfile.ZipFile("documents.zip", "w") as zipf:
    for root, _, files in os.walk("pdfs"):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

print("Descarrega i compressió completa! Els documents s'han guardat a documents.zip")
