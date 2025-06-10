import os
import sys
import time

abu = '\033[90m'
r = '\033[0m'

def main(folder_path):
    files = os.listdir(folder_path)
    jpg_files = [f for f in files if f.lower().endswith('.jpg')]
    jpg_files.sort()

    total_files = len(jpg_files)
    if total_files == 0:
        print(f"{abu}tidak ada file .jpg di folder tersebut{r}")
        return

    delay = max(0.01, min(0.1, 1.0 / total_files))
    for i, filename in enumerate(jpg_files, start=1):
        old_path = os.path.join(folder_path, filename)
        new_filename = f"{i}.jpg"
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)

        progress = int((i / total_files) * 100)
        sys.stdout.write(f"\r{abu}progress: {progress}% ({filename} -> {new_filename}){r}")
        sys.stdout.flush()

        time.sleep(delay) 

    print(f"\n{abu}semua file berhasil diubah namanya.{r}")

folder = input(f"\n{abu}masukkan path folder: {r}")
main(folder)
