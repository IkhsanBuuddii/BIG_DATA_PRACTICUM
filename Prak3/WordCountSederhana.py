from collections import defaultdict

def map_function(text):
    for word in text.split():
        yield (word, 1)

def reduce_function(pairs):
    result = defaultdict(int)
    for word, count in pairs:
        result[word] += count
    return result
    
text = "contoh teks sederhana untuk menghitung frekuensi kata"
mapped = map_function(text)
reduced = reduce_function(mapped)
print(reduced)
