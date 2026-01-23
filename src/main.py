import os
import shutil
import sys
from generate_static import generate_pages_recursive, generate_page

def main():
    basepath = sys.argv[1]
    publish_static_to_public()
    generate_pages_recursive("content", "template.html", "docs", basepath)


def publish_static_to_public():
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    
    files_to_copy = os.listdir("static")
    copy_files(files_to_copy)

def copy_files(file_list, base_path = ""):
    dest_folder = os.path.join("docs", base_path)
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    for item in file_list:
        source = os.path.join("static", base_path, item)
        if os.path.isfile(source):
            dest = os.path.join("docs", base_path)
            print(f"copying file from {source} to {dest}")
            shutil.copy(source, dest)
        else:
            sub_list = os.listdir(source)
            new_base = os.path.join(base_path, item)
            copy_files(sub_list, new_base)


main()