def bucket_sort(arr):
    bucket = []
    
    # 1. Create empty buckets (jitne elements utne buckets bana liye for safety)
    for i in range(len(arr)):
        bucket.append([])
        
    # 2. Scatter: Elements ko buckets mein daalo
    for j in arr:
        index_b = int(10 * j) # Example logic: 0.42 -> bucket 4
        bucket[index_b].append(j)
        
    # 3. Sort individual buckets
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i]) # Chhote level pe sort fast hota hai
        
    # 4. Gather: Wapas ek list mein jodo
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

# Test
x = [0.897, 0.565, 0.656, 0.123, 0.665, 0.3434] 
print(bucket_sort(x))

# The Catch (Isme Ghaata Kya Hai?)
# Space: Tujhe extra memory chahiye buckets banane ke liye.

# Worst Case: Agar saare students nalayak hain aur sabke 0 marks aaye, toh saare papers Bucket 1 mein chale jayenge. Phir ye normal sorting jitna hi slow ho jayega.