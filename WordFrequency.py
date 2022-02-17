infile = open('Al.txt','r')

word_freq = {}

for line in infile:
    line = line.strip()
    line = line.lower()
    words = line.split()
    line = line.rstrip()

    for word in words:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1
    word_freq[word]
    
print(word_freq)