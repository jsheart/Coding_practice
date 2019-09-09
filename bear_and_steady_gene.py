
# coding: utf-8

# In[1]:


from collections import Counter
def steadyGene(gene):
    n = len(gene) // 4
    table = {}
    total_count = 0
    for key, count in Counter(gene).items():
        if count > n:
            table[key] = count - n
            total_count += count - n
    if total_count == 0:
        return 0
    left = count = 0
    min_left = -1
    length = float('inf')
    for index in range(len(gene)):
        if gene[index] in table:
            table[gene[index]] -= 1
            if table[gene[index]] >= 0:
                count += 1
        while count == total_count:
            if index - left + 1 < length:
                length = index - left + 1
                min_left = left
            if gene[left] in table:
                table[gene[left]] += 1
                if table[gene[left]] > 0:
                    count -= 1
            left += 1
    return length   

if __name__ == '__main__':
    
    gene = "TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC"
    
    result = steadyGene(gene)
    
    print(result)

