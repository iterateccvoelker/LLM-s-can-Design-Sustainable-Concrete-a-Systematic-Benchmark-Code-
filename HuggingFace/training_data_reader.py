# Open the file for reading
import pandas as pd


def preprocess_aac_data():
    """
    Function for reading and parsing AAC_dataset.txt
    """
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


def preprocess_interpolation_data():
    """
    Function for reading and parsing interpolation_testing_samples.txt
    """
    data = []
    with open('interpolation_testing_samples.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                data.append(line)
    data_with_features_and_labels = []
    for line in data:
        pieces = line.split(',Completion: ')
        if len(pieces) < 2:
            continue
        new_row = (pieces[0], float(pieces[1]))
        data_with_features_and_labels.append(new_row)
    df = pd.DataFrame(data_with_features_and_labels, columns=['question', 'answer'])
    df_sorted = df.sort_values(by='answer', ascending=False)

    top_20_index = int(0.2 * len(df_sorted))
    low = df_sorted.iloc[top_20_index:]
    high = df_sorted.head(top_20_index)

    train_data = low.sample(frac=1, random_state=42)
    train_data.reset_index(inplace=True, drop=True)

    test_data = high.sample(frac=1, random_state=42)
    test_data.reset_index(inplace=True, drop=True)

    return train_data, test_data


if __name__ == '__main__':
    train, test = preprocess_interpolation_data()
    print(train)