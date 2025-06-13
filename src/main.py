import os
import shutil
from os_interact import copy_files_recursive, generate_page, get_content_recursive, makedirs_for_content

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    all_content = get_content_recursive(dir_path_content)
    makedirs_for_content(all_content, dir_path_content, dir_path_public)

    print("Generating page...")
    print(all_content)
    for item in all_content:
        if os.path.isfile(item):
            dest_path = item.replace(str(dir_path_content), str(dir_path_public))
            dest_path_html = f'{dest_path[:-2]}html'
            generate_page(
                    item,
                    template_path,
                    os.path.join(dest_path_html),
            )
    
main()
