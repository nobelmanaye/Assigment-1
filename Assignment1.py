'''
Nobel Manaye

Jan 24th, 2020

'''

# 1


    #a) 108

    #b)  108


    #c) 108
# 2

     #a) -99

     # b) -77

     # c) 205

# 3

    # a) 00111000
    # b) 11010101
    # c) 11111111



# 4)
    #a)38
    #b)1B6
    #c)D7

def unsignedDecimalToBinary(decimal):
    count = 0
    newdec = decimal                                     
    
    while (2**count) < newdec:
        tester = 2**count
        print('tester',tester)
        
        if newdec-tester > 0:
            
            count += 1
            
        else:
            
            
            break
    if decimal == 1:
        return '1'
    elif decimal == 0:
        
        return '0'
    elif decimal == 2:
        return '10'
    
   
    ls = []
    count -= 1
    binary = 0
    while decimal >=1:
       
        
        if tester >= decimal:
            count -= 1
            tester = 2**count
            
        
        else:
            

            decimal -= tester
            if count > 0:
            
        
                ls.append(count)
            count -= 1
            tester = 2**count
        
    print(ls)
    for item in ls:
        binary += 10**item
    newbinary = str(binary)
    return newbinary



def unsignedBinaryToDecimal(unsignedbinary):
    ls = []
    decimal = 0
    
    for character in str(unsignedbinary):
        ls.append(int(character))
    count = (len(ls)-1)
    for character in ls:
        decimal += character*(2**count)
        count -= 1
    return decimal


def addOne(unsignedbinary):
    decimal = (unsignedBinaryToDecimal(unsignedbinary))
    newdecimal = decimal +1
    
    
    return unsignedDecimalToBinary(newdecimal)




def twosCompToDecimal(twobitbin):
    invertedbinary = ''
    

    if twobitbin[0] == '1':
        
        decimal = (unsignedBinaryToDecimal(twobitbin)-1)
        unsignedbinary = unsignedDecimalToBinary(decimal)
        print(unsignedbinary)
        for digit in unsignedbinary:
            if digit == '1':
                invertedbinary += '0'
            else:
                invertedbinary += '1'
        return -1*(unsignedBinaryToDecimal(invertedbinary))
    else:
        return unsignedBinaryToDecimal(twobitbin)

def decimalToTwosComp(decimal):
    invertedbinary = 0
    if decimal < 0:
        decimal *= -1
        unsignedbinary = unsignedDecimalToBinary(decimal)
        for digit in unsignedbinary:
            if digit == '1':
                invertedbinary += '0'
            else:
                invertedbinary += '1'
        finalbinary = addOne(invertedbinary)
        return finalbinary
    else:
        return unsignedDecimalToBinary(decimal)
    
def signExtend(twobitbin,digitnumber):
    extendedtwobitbin = ''
    length = abs(len(twobitbin)-digitnumber)
    print(length)

    if twobitbin[0] == '0':
        
        
        for i in range(length):
            extendedtwobitbin += '0'

            return extendedtwobitbin + twobitbin
    else:
        if length == 1:
            extendedtwobitbin += '0'
            return extendedtwobitbin + twobitbin
    
        else:
            extendedtwobitbin += '1'
            for i in range(length-1):
                extendedtwobitbin += '0'

                return extendedtwobitbin + twobitbin
            
                
        
        

   

        
            

##        count = 8-len(binary)
##        
##        for i in range(count):
##            
##            fullbitbinary += '0'
##            
##        fullbitbinary += binary
##
##        return fullbitbinary
    
        
        
        
        
                
        
    
    
    
        
    
    
            
        

if __name__ == "__main__":

        
    
     print(signExtend('1101',5))
    
    
    
    
