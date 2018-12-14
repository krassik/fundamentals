def show_excitement():
    # Your code goes here!
    n = 5
    s = "I am super excited for this course!"
    five_sen = ""
    while(n):
        five_sen += (' ' + s)
        n = n - 1
        
    return s

print show_excitement()