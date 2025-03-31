import os

# Define source directory and output file
src_dir = "src"
output_file = "output.txt"

# Open the output file for writing
with open(output_file, "w", encoding="utf-8") as out_file:
    # Walk through all files in the src directory
    for root, _, files in os.walk(src_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    out_file.write(f"=== {file_name} ===\n")
                    out_file.write(file.read() + "\n\n")
            except Exception as e:
                out_file.write(f"Error reading {file_name}: {e}\n\n")

print(f"Data written to {output_file}")
