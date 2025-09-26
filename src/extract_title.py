
def extract_title(markdown: str):
  lines = markdown.split('\n')
  for line in lines:
    if line.strip().startswith('#'):
      return line.strip()[1:].strip()
  raise Exception("No title found")
  