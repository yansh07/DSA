def HashMap(target, array):
    seen = {}

    for i, num in enumerate(array):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

target = 13
array = [2, 7, 11, 15]
test = HashMap(target, array)
print(test)

# How this works?
# The magic is in the Hashing Function. It takes a key and immediately tells the computer exactly where in memory to find the corresponding value. This gives it that sweet, sweet O(1) (constant) average time complexity for both lookups and insertions.