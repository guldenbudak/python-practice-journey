from collections import Counter
cnt = Counter()
frequency = {}
text = "Bugün hava çok güzel bugün dışarı çıkmak güzel"
split_lower = text.lower().split()
frequency = split_lower
print(frequency)
print(Counter(split_lower).most_common(3))