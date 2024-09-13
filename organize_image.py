import os
import pandas as pd
import shutil

# def organize_images(image_folder, csv_file, output_dir):
#   """Organizes images into separate folders based on article type.

#   Args:
#     image_folder: Path to the folder containing images.
#     csv_file: Path to the CSV file with image IDs and article types.
#     output_dir: Path to the output directory where folders will be created.
#   """

#   # Create output directory if it doesn't exist
#   if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

#   # Load CSV data into a DataFrame
#   df = pd.read_csv(csv_file)

#   # Iterate through images and move them to appropriate folders
#   for filename in os.listdir(image_folder):
#     if filename.endswith('.jpg'):  # Assuming images are JPEGs
#       # Check if image ID exists in CSV
#       if filename in df['id'].values:
#         article_type = df[df['id'] == filename]['articleType'].values['Shirts']
#         output_folder = os.path.join(output_dir, article_type)
#         if not os.path.exists(output_folder):
#           os.makedirs(output_folder)
#         shutil.move(os.path.join(image_folder, filename), output_folder)
#       else:
#         print(f"Image '{filename}' not found in CSV.")

def organize_images(image_folder, csv_file, output_dir):
  """Organizes images into separate folders based on article type.

  Args:
    image_folder: Path to the folder containing images.
    csv_file: Path to the CSV file with image IDs and article types.
    output_dir: Path to the output directory where folders will be created.
  """

  # Create output directory if it doesn't exist
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  # Load CSV data into a DataFrame
  df = pd.read_csv(csv_file)

  # Iterate through images and move them to appropriate folders
  for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):  # Assuming images are JPEGs
      # Check if image ID exists in CSV
      if filename in df['id'].values:
        article_type = df[df['id'] == filename]['articleType'].values[0]
        if article_type == 'Shirts':  # Filter for 'Shirts'
          output_folder = os.path.join(output_dir, article_type)
          if not os.path.exists(output_folder):
            os.makedirs(output_folder)
          shutil.move(os.path.join(image_folder, filename), output_folder)
        else:
          print(f"Image '{filename}' has article type '{article_type}', not 'Shirts'.")

# Example usage:
image_folder = "images"
csv_file = 'Women_dataset.csv'
output_dir = 'organized_images'
organize_images(image_folder, csv_file, output_dir)
