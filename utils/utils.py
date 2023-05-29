import os
from PIL import Image


def image_scale(image_path, output_path, new_width=None, new_height=None, scale=None):
    image = Image.open(image_path)
    width, height = image.size
    if scale is not None:
        new_width, new_height = int(scale * width), int(scale * height)
    if new_width is not None and new_height is not None:
        resized_image = image.resize((new_width, new_height), resample=Image.LANCZOS)
        resized_image.save(output_path)


def rename_files(input_path, output_path, default_name):
    files = os.listdir(input_path)
    files.sort()

    for i, file_name in enumerate(files, start=1):
        file_name, file_extension = os.path.splitext(file_name)
        new_file_name = f"{default_name}{i}{file_extension}"

        old_file_path = os.path.join(input_path, file_name + file_extension)
        new_file_path = os.path.join(output_path, new_file_name)

        os.rename(old_file_path, new_file_path)
