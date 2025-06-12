import os
import shutil
from os_interact import copy_files_recursive, generate_page, generate_sub_pages, get_content, makedirs_for_content

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
    
    files_to_make = get_content(dir_path_content)
    makedirs_for_content(files_to_make, dir_path_content, dir_path_public)
    generate_sub_pages(files_to_make, dir_path_content, template_path, dir_path_public)
    print("Generating sub-pages")

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )
    
main()
