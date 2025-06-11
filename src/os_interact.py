import os
import shutil

def delete_public(dir):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except Exception as e:
            print(f'Failed to delete {path}. Reason: {e}')

def copy_source(src, dest):
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dest_item = os.path.join(dest, item)
        if os.path.isdir(src_item):
            if not os.path.exists(dest_item):
                os.makedirs(dest_item)
            copy_source(src_item, dest_item)
        else:
            shutil.copy2(src_item, dest_item)
