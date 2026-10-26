def count_vowels(text):
    count=0
    for char in text:
        if char in "aeiou":
            count=count+1
    print(count)
count_vowels("hello world")