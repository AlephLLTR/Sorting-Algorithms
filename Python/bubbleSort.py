def bubble(array):                          
    n = len(array)                          
    while n != 0:                           
        N = 0                               
        for i in range(1, n):                
            if array[i - 1] > array[i]:      
                aux = array[i - 1]           
                array[i - 1] = array[i]      
                array[i] = aux               
                N = i                       
        n = N                               
    print(
