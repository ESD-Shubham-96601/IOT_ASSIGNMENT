

def count_vowels(string):
    vowels="aeiouAEIOU"
    count=0

    for ch in string:
        if ch in vowels:
            count+=1
    return count


def count_consonants(string):
    vowels="aeiouAEIOU"
    count=0

    for ch in string:
        if ch.isalpha() and ch not in vowels:
            count+=1
    return count


def calculate_ratio(vowels,consonants):
    if consonants==0:
        return "Ratio cannot be calculated (consonants = 0)"
    ratio=vowels/consonants
    return ratio

string=input("enter a string")

vowel_count=count_vowels(string)
consonant_count=count_consonants(string)

ratio=calculate_ratio(vowel_count,consonant_count)

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Ratio of vowels to consonants:", ratio)