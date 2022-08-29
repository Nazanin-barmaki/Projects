from ast import Mod
import math
use = int(input('chand bar mikhahid az mashinhesab estefade konid?: '))
use_type = input('B = Basic or A= Advanced?): ')
if use_type == "B" or use_type == "b" or use_type == "Basic":
    

        operation = input(''' type in the math operation you would like to complete':
        + for addition 
        - for subtraction
        * for multiplication
        / for division
        ** for exponential
        // for floor division
        % for Modulus
        ** for Exponentiation
        ''')
        i=i+1
        print ("Round",i)
for i in range(use):
        number_1 = float(input('enter you firt number :'))
        number_2 = float(input('enter your second number:'))

        if operation == '+' or operation == 'jam'or operation == 'be alave':
        print('{} + {}' = '.format(number_1 , number_2')
        print(number_1 + number_2)
        counter+=1
        
     elif operation == '-' or operation =='menha'or operation == 'tafrigh':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        counter-=1

        
     elif operation == '*'or operation =='zarb':
        print('{} * {}' ='.format(number_1 , number_2))
        print(number_1 * number_2)
        counter-=1

     elif operation == '**' or operation == 'tavan':   
       print('{} * {} = '.format(number_1, number_2))
            print(number_1 ** number_2)
            counter-=1

     elif operation == '/' or operation == 'taghsim':
          print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            counter-=1

     elif operation == '//' or operation == 'taghsim sahih':
          print('{} // {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            counter-=1  

     elif operation == '%' or operation == 'baghimande':
          print('{} /% {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            counter-=1  
            
     #Advanced

     elif use_type == "A" or use_type == "a" or use_type == "Advanced" or use_type == "advanced":

         operation = input(''' type in the math operation you would like to complete':
         % for Modulus
         || for Absolute value
         √  for radical
         sqr for radical
         fact for factorial
         sin , cos , tan  ,cot''')

           i=i+1
        print ("Round",i)

          for i in range(use):
        number_1 = float(input('enter you firt number :'))
        number_2 = float(input('enter your second number:'))

        if operation == 'sin':
           sin=math.sin(number_1)
         print('sin of number:',sin)

        elif operation=='cos':
         cos=math.cos(number_1)
         print('cos of number:',cos)

        elif operation=='tan':
         tan=math.tan(number_1)
         print('tan of number:',tan)

        elif:
         cot=math.cot(number_1)
         print('cot of number:',cot)
       
        elif operation=='radical':
            radical=math.sqrt(number1)
            print('radical of number:',radical)

        elif operation=='mod'):
            mod=math.mod(number_1)
            print('mod of number:',mod)

        elif operation=='ghadremotlagh':
            ghadremotlagh=math.ghadremotlagh(number_1)
            print('ghadremotlagh of number:',ghadremotlagh)

        else:
            print('Thanks for using , good luck:)')





        

