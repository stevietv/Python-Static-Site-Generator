import os
import pathlib
from generate_html import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    input_file = open(from_path, 'r')
    markdown = input_file.read()
    input_file.close()

    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()
    
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_folder = os.path.dirname(dest_path)
    os.makedirs(dest_folder, exist_ok=True)

    output_file = open(dest_path, 'w')
    output_file.write(template)
    output_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    file_list = os.listdir(dir_path_content)
    for item in file_list:
        source = os.path.join(dir_path_content, item)
        if os.path.isfile(source) and pathlib.Path(source).suffix == ".md":
            dest = os.path.join(dest_dir_path, item.replace("md", "html"))
            generate_page(source, template_path, dest)
        else:
            sub_source = os.path.join(dir_path_content, item)
            sub_dest = os.path.join(dest_dir_path, item)
            generate_pages_recursive(sub_source, template_path, sub_dest)
        

