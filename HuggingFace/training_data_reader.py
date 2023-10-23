# Open the file for reading
import pandas as pd


def preprocess_training_data():
    data = []
    with open('AAC_dataset.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                data.append(line)
    data_with_features_and_labels = []
    for line in data:
        pieces = line.split(' compressive strength: ')
        if len(pieces) < 2:
            continue
        new_row = (pieces[0], pieces[1])
        data_with_features_and_labels.append(new_row)
    df = pd.DataFrame(data_with_features_and_labels, columns=['X', 'y'])

    return df


if __name__ == '__main__':
    data = preprocess_training_data()
    print(data)