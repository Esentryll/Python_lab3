from tqdm import tqdm

def compare(a, b):
    return a['age'] < b['age']

def insertion_sort(data):
    with tqdm(total=len(data), desc="Sorting ") as sort_bar:
        for i in range(1,len(data)):
            value = data[i]
            j = i - 1
            while j >= 0 and compare(value, data[j]):
                data[j+1] = data[j]
                j -= 1
            data[j+1] = value
            sort_bar.update(1)
    return data