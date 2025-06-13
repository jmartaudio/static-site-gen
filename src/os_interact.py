import os
import shutil
from markdown_to_htmlnode import markdown_to_html_node, extract_title

def get_content_recursive(dir_path_content):
    folder_content = []
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        folder_content.append(item_path)
        if os.path.isdir(item_path):
            folder_content.extend(get_content_recursive(item_path))
    return folder_content
                        
def makedirs_for_content(folder_content, dir_path_content, dir_path_public):
    for item in folder_content:
        if os.path.isdir(item):
            dir_path = item.replace(str(dir_path_content), str(dir_path_public))
            os.makedirs(dir_path)

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    
    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", str(title))
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
