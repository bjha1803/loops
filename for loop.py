marks=[60,45,25,23,24]
'''
marks.append(90)
print(marks)

marks=[60,45,56]
marks.insert(1,90)
print(marks)

print(90 in marks)

print(len(marks))

marks =(87,23,87,26,26,26)
print(marks.count(87))

marks =(87,23,25,28,27,26)
print(marks.index(26))
'''

'''marks =(87,23,25,28,27,26)
for i in marks:
    print(i)
    if i == 23:
        break
    
'''

def calculate_memory_allocated(req_size, requests):
    memory_allocated = 0
    for request in requests:
        # If the request is for memory allocation (positive number), add it to memory_allocated
        if request > 0:
            memory_allocated += request
        # If the request is for memory deallocation (negative number), subtract it from memory_allocated
        else:
            memory_allocated -= abs(request)
    return memory_allocated

# Input
req_size = int(input())
requests = list(map(int, input().split()))

# Output
print(calculate_memory_allocated(req_size, requests))
