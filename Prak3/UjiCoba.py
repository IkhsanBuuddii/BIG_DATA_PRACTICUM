import csv
from collections import defaultdict

# Path ke file CSV
file_path = r'C:\Users\User\Downloads\ThrowbackDataThursday Week 11 - Film Genre Stats.csv'

# Fungsi Map: Memecah teks menjadi kata-kata dan mengeluarkan pasangan (kata, 1)
def map_function(text):
    for word in text.split(','):
        yield (word.strip(), 1)

# Fungsi Reduce: Menghitung jumlah kemunculan setiap kata
def reduce_function(pairs):
    result = defaultdict(int)
    for word, count in pairs:
        result[word] += count
    return result

# Mengumpulkan semua kata dari setiap kolom
all_words = []
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    for row in reader:
        for value in row:
            all_words.extend(map_function(value))

# Menghitung frekuensi kata dengan reduce_function
word_counts = reduce_function(all_words)

# Menghitung rata-rata untuk kolom numerik
total_movies_released = 0
total_gross = 0
total_tickets_sold = 0
count = 0

# Membaca ulang untuk menghitung rata-rata
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            movies_released = int(row.get('Movies Released', 0))
            gross = int(row.get('Gross', 0))
            tickets_sold = int(row.get('Tickets Sold', 0))
            
            total_movies_released += movies_released
            total_gross += gross
            total_tickets_sold += tickets_sold
            count += 1
        except ValueError:
            # Skip rows with invalid data
            continue

# Menghitung rata-rata
average_movies_released = total_movies_released / count if count > 0 else 0
average_gross = total_gross / count if count > 0 else 0
average_tickets_sold = total_tickets_sold / count if count > 0 else 0

# Menampilkan hasil
print("Frekuensi kata dalam seluruh kolom:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

print("\nRata-Rata:")
print(f"Rata-rata jumlah film dirilis: {average_movies_released:.2f}")
print(f"Rata-rata gross: {average_gross:.2f}")
print(f"Rata-rata tiket terjual: {average_tickets_sold:.2f}")

# Jika Anda ingin menyimpan hasil ke file
output_file_path = r'C:\Users\User\Downloads\word_frequencies_and_averages.csv'
with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Count'])
    for word, count in word_counts.items():
        writer.writerow([word, count])
    
    writer.writerow([])  # Empty row for separation
    writer.writerow(['Metric', 'Value'])
    writer.writerow(['Average Movies Released', average_movies_released])
    writer.writerow(['Average Gross', average_gross])
    writer.writerow(['Average Tickets Sold', average_tickets_sold])
