import csv


def create_csv(ret, neuro=True):
    if neuro:
        with open(r'NeuroGen.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(ret)

    if not neuro:
        with open(r'KhaasFood.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(ret)
