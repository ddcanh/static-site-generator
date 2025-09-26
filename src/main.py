import os
import shutil
from generate_pages_recursive import generate_pages_recursive

def prepare_target_dir(dir_path):
  if os.path.exists(dir_path):
    try:
      shutil.rmtree(dir_path)
    except OSError as e:
      print(f"Error: {e}")
  
  os.makedirs(dir_path)

def copy_all_files(src, dst):
  for file in os.listdir(src):
    if os.path.isfile(os.path.join(src, file)):
      src_file = os.path.join(src, file)
      dst_file = os.path.join(dst, file)
      shutil.copy(src_file, dst_file)
    elif os.path.isdir(os.path.join(src, file)):
      src_dir = os.path.join(src, file)
      dst_dir = os.path.join(dst, file)
      os.makedirs(dst_dir, exist_ok=True)
      copy_all_files(src_dir, dst_dir)



def main():
  prepare_target_dir("./public")
  copy_all_files("./static", "./public")
  generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
  main()
