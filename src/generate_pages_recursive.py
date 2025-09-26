from ntpath import isfile
import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")
  try:
    os.makedirs(dest_dir_path, exist_ok=True)
    for file in os.listdir(dir_path_content):
      if os.path.isfile(os.path.join(dir_path_content, file)) and file.endswith(".md"):
        file_html = os.path.splitext(file)[0] + ".html"
        generate_page(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file_html))
      elif os.path.isdir(os.path.join(dir_path_content, file)):
        generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file))

  except Exception as err:
    print(f'Error generating page: {err}')