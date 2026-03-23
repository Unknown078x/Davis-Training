t = (5, 1, 8, 3)

# pehle element ko hi max aur min maan lo
max_val = t[0]
min_val = t[0]

# ab baaki elements check karo
for num in t:
    
    if num > max_val:
        max_val = num
        
    if num < min_val:
        min_val = num

print("Max =", max_val)
print("Min =", min_val)