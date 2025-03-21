# goal : bridge shuffle two lists together.
def f_Shuffle ( x , y ) :

    v_NewArray = []
    # find the shortest list
    v_MinLength = min ( len ( x ) , len ( y ) )

    # look up the same index number for each list and add it to the array.
    for n in range ( v_MinLength ) :
        v_NewArray.append ( x[n] )
        v_NewArray.append ( y[n] )

    # if one list is longer, add all the rest to the end.
    if len ( x ) > v_MinLength :
        v_NewArray.extend ( x[v_MinLength:] )

    elif len ( y ) > v_MinLength :
        v_NewArray.extend ( y[v_MinLength:] )
            
    print ( v_NewArray )

if __name__ == "__main__" :

    l_Array1 = ['a','b','c']
    l_Array2 = [1,1,3,4,5,6,7]
    
    f_Shuffle ( l_Array1 , l_Array2 )