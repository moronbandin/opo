import csv
import os

# Define o camiño base onde crear as carpetas
base_path = '/home/user/github/grc/docs'

# Configuración básica para o ficheiro mkdocs.yml
config = """
site_name: MkDocs
site_description: Temas
site_author: Eu
theme:
  language: gl
  name: 'material'
  palette:
    primary: 'blue grey'
    accent: 'yellow'
  logo: 'images/logo.png'
  favicon: 'images/favicon.ico'    
  font:
    text: Roboto
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/moronbandin
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/moronbandin

nav:
"""

# Lista para gardar as entradas de navegación
nav_entries = []

# Explorar tódalas subcarpetas dentro do directorio base
for folder_name in (os.listdir(base_path)):
    folder_path = os.path.join(base_path, folder_name)
    if os.path.isdir(folder_path):
        # Asumimos que cada carpeta ten un arquivo index.md
        doc_title = folder_name.split('_')[0]  # Usar o ID do tema para o título no nav
        category = folder_name.split('_')[1]  # Usar a categoría para agrupar
        nav_entries.append(f"  - {category}/{doc_title}: '{folder_name}/index.md'")

# Engadir as entradas de navegación á configuración
config += "\n".join(nav_entries)

# Escribir a configuración ao ficheiro mkdocs.yml
with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    f.write(config)

print("Ficheiro mkdocs.yml creado correctamente.")
