import subprocess
import pandas as pd

def run_kubectl_command():
    # Prompt the user to enter the kubectl command
    command = input("Enter the kubectl command (e.g., 'kubectl get all'): ")
    try:
        # Execute the command and capture its output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error running the command:")
        print(e.stderr)
        return None

def parse_kubectl_output(output):
    tables = []
    table = []
    headers = []
    for line in output.strip().split("\n"):
        if line.startswith("NAME") and headers == []:
            headers = line.split()
        elif line.startswith("NAME") and headers != []:
            # Save the current table
            if table:
                tables.append((headers, table))
            # Start a new table
            headers = line.split()
            table = []
        else:
            table.append(line.split())
    
    if table:  # Append the last table
        tables.append((headers, table))
    
    return tables

def save_to_excel(tables, filename="kubernetes_output.xlsx"):
    with pd.ExcelWriter(filename) as writer:
        for i, (headers, rows) in enumerate(tables):
            sheet_name = f"Table_{i + 1}"
            df = pd.DataFrame(rows, columns=headers)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"Data saved to {filename}")

def main():
    output = run_kubectl_command()
    if output:
        tables = parse_kubectl_output(output)
        save_to_excel(tables)

if __name__ == "__main__":
    main()
