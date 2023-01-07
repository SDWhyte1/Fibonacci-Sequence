def fib(n3): #function which takes number of sequence user wants to see
    n1 = 0 #hard code in the first element
    n2 = 1 #hard code in the 2nd element
    counter = 2 #as first 2 characters are hard coded counter is increased by 2
    holder = [] #array to output seq
    holder.append(n1) #appends first element to array
    holder.append(n2) #appends second element to array
    while counter < n3: #checks counter is less than length user wants to see
        nth = n1 + n2 #next element in list
        n1 = n2 #will increase the pointer by 1
        n2 = nth #will increase the pointer by 1
        holder.append(nth) #adds nth element to array
        counter = counter +1 #increases counter
        #print(counter)
    print(holder) #prints out array when breaks out the loop

#fib(0,1)
invalidNumber = True #will ensure user enters a valid number
while invalidNumber:
    seq = input("How many numbers of the fib sequence would you like to know ? ")
    try:
        seq = int(seq)
        invalidNumber = False
    except:
        print("Please enter a number")

if seq <= 0: #makes sure the number is positive otherwise will break out
    print("Please enter a positive number")
elif seq == 1:
    print ("You only entered 1, therefore 0 is the first number of the sequence")
else:
    fib(seq)
