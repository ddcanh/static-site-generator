
import os

from html_markdown import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  try:
    with open(from_path, 'r') as from_file:
      with open(template_path, 'r') as template_file:
        markdown = from_file.read()
        template = template_file.read()

        title = extract_title(markdown)
        node = markdown_to_html_node(markdown)
        html = node.to_html()

        template = template.replace("{{ Title }}", title, 1)
        template = template.replace("{{ Content }}", html, 1)

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, 'w') as dest_file:
          dest_file.write(template)

  except Exception as err:
    print(f'Error generating page: {err}')