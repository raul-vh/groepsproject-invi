import csv

def transform_text_to_csv(input_file, output_file):
    header = None
    rows = []
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith('# FromNodeId'):
            header = line.split('\t')
        elif not line.startswith('#'):
            rows.append(line.split('\t'))

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header)
        writer.writerows(rows)
    return