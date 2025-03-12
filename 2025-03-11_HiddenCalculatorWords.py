# goal : Act like you are entering numbers into a calculator, then flipping it.

def HiddenCalculatorWords() :
    
    # Dictionary of numbers to letters.

    d_Words = \
        {
            1 : 'I',
            2 : 'Z',
            3 : 'E',
            4 : 'H',
            5 : 'S',
            6 : 'G',
            7 : 'L',
            8 : 'B',
            0 : 'O'
         }
    
    # Get input and initilize Letters string.

    print ("-----")
    v_input = input ( )

    v_Letters = ""

    # Make sure input is only integers.

    for v_Character in v_input :

        try :
            int(v_Character)
        except :
            print ("Invalid character in input.")
            return

        # Make sure input is in dictionary, if so add it to letters string.

        v_Character = int(v_Character)
        if v_Character not in d_Words :
            print ("Invalid character in input.")
            return
        
        else :
            v_Letters += d_Words[int(v_Character)]
        
    # Reverse the string.

    v_result = v_Letters[::-1]
    print("-----")
    print(v_result)

    return

# # #

HiddenCalculatorWords()