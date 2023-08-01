import os
import time
import math
import src.SubstitutionCipher as sc
import src.TranspositionCipher as tc
import src.PrivateKeyCryptography as xkc
import src.PublicKeyCryptography as pkc
import menu.Menu as menu
from src.miscellaneous.misc import isPrime

def main(): # type: ignore
    ch = 'Y'
    while ch == 'Y' or ch == 'y': # loop for start screen
        choice = menu.MainMenu()
        
        if choice == '1':
            ch1 = 'Y'
            while ch1 == 'Y' or ch1 == 'y':
                choice1 = menu.MenuSubstitution()
                
                if choice1 == '1':
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                   CAESAR CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu1()
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
             CAESAR CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Please ENTER to continue...')
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter your Message: ' + plaintext)
                                            key = int(input('Enter your Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 26')
                                            print('Please ENTER to continue...')
                                        
                                    print('Encrypted Message: \'' + sc.CaesarCipher(plaintext, key) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                    
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('\nERROR: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = int(input('\nEnter a Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 26')
                                            print('Please ENTER to continue...')
                                            
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    ciphertext = sc.CaesarCipher(plaintext, key)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                        
                                    print('Contents of the file are successfully encrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                      
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
             CAESAR CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Please ENTER to continue...')
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)      
                                            key = int(input('Enter your Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 26')
                                            print('Please ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + sc.CaesarCipher(ciphertext, key, False) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = int(input('\nEnter a Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 26')
                                            print('Please ENTER to continue...')
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    plaintext = sc.CaesarCipher(ciphertext, key, False)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                        
                                    print('\nContents of the file is successfully decrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                
                        # checkpoint 1
                        elif choice2 == '3':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
         CAESAR CIPHER BRUTE-FORCE ATTACK
***************************************************
                                        ''')
                                    ciphertext = str(input('Enter the Ciphertext: '))
                                    c = len(ciphertext)
                                    assert c > 0
                                except AssertionError:
                                    print('\nERROR: Empty String cannot be decrypted')
                                    input('Press ENTER to continue...')
                                    
                            print('\nBrute-Force Decrytion are as follows:')
                            sc.CaesarBruteForce(ciphertext)
                            input('\nPress ENTER to continue...')
                                    
                        elif choice2 == '4':
                            break
                        elif choice2 == '5':
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit1(choice2)
                 
                elif choice1 == '2':
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
               ADVANCED CAESAR CIPHER
***************************************************
                            ''')
                        choice2 = menu.OperationMenu1()

                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
         ADVANCED CAESAR CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Please ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter your Message: ' + plaintext)
                                            key = int(input('Enter a Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 94')
                                            print('Please ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + sc.CaesarCipher2(plaintext, key) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = int(input('\nEnter a Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 94')
                                            print('Please ENTER to continue...')
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    ciphertext = sc.CaesarCipher2(plaintext, key)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                        
                                    print('Contents of the file are successfully encrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                              
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
         ADVANCED CAESAR CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Please ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            key = int(input('Enter your Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 94')
                                            print('Please ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + sc.CaesarCipher2(ciphertext, key, False) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = int(input('\nEnter the Key: '))
                                            break
                                        except ValueError:
                                            print('ERROR: Key should be a finite integral value from 1 - 94')
                                            print('Please ENTER to continue...')
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    plaintext = sc.CaesarCipher2(ciphertext, key, False)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                        
                                    print('\nContents of the file is successfully decrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                        
                        elif choice2 == '3':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
     ADVANCED CAESAR CIPHER BRUTE-FORCE ATTACK
***************************************************
                                        ''')
                                    ciphertext = str(input('Enter the Ciphertext: '))
                                    c = len(ciphertext)
                                    assert c > 0
                                except AssertionError:
                                    print('\nERROR: Empty String cannot be decrypted')
                                    input('Press ENTER to continue...')
                                    
                            print('\nBrute-Force Decrytion are as follows:')
                            sc.CaesarBruteForce2(ciphertext)
                            input('\nPress ENTER to continue...')
                            
                        elif choice2 == '4':
                            break
                        elif choice2 == '5':
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit1(choice2)
                
                elif choice1 == '3': # binary cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                   BINARY CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
             BINARY CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Please ENTER to continue...')
                                            
                                    enb, morse = sc.BinaryEncrypt(plaintext)
                                    print('Binary Equivalent: ', enb)
                                    print('Morse Code Equivalent: ', morse)
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            print('File Found!')
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except(IOError):
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    ciphertext, morse = sc.BinaryEncrypt(plaintext)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                    
                                    print('Contents of the file are successfully encrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)

                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
             BINARY CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Please ENTER to continue...')
                                            
                                    print('Binary Decrypted: ', sc.BinaryDecrypt(ciphertext))
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            print('File Found!')
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                        
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                        
                                    try:
                                        fout = open(file, 'w')
                                    except(IOError):
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    
                                    plaintext = sc.BinaryDecrypt(ciphertext)
                                    fout.write(plaintext)
                                    fout.close()
                                    
                                    print('Contents of the file successfully decrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                        elif choice2 == '3':
                            break
                        elif choice2 == '4': # exit
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                                
                elif choice1 == '4':
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
        MONOALPHABETIC SUBSTITUTION CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
   MONOALPHABETIC SUBSTITUTION CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Please ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + sc.MASC(plaintext) +'\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                    
                                    try:
                                        if os.path.exists(file):
                                            print('File found')
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('\nERROR: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = sc.MASC(plaintext)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                    
                                    print('Contents of the file are successfully encrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
   MONOALPHABETIC SUBSTITUTION CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Please ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + sc.MASC(ciphertext, False) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            print('File found')
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    plaintext = sc.MASC(ciphertext, False)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                        
                                    print('\nContents of the file is successfully decrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '3': # go back
                            break
                        elif choice2 == '4': # exit
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                            
                elif choice1 == '5': # base-64
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                   BASE-64 CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
                BASE-64  ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = bytes(str(input('Enter your Message: ')), 'utf-8')
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Please ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + sc.base64Crypt(plaintext).decode() + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                    
                                    try:
                                        if os.path.exists(file):
                                            print('File found')
                                        fin = open(file, 'rb')
                                    except (IOError, FileNotFoundError):
                                        print('\nERROR: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    try:
                                        fout = open(file, 'wb')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break

                                    ciphertext = sc.base64Crypt(plaintext)
                                    fout.write(ciphertext)
                                    fout.close()
                                        
                                    print('Contents of the file are successfully encrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 =='3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
                BASE-64 DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = bytes(str(input('Enter the Ciphertext: ')), 'utf-8')
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Please ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + sc.base64Crypt(ciphertext, False).decode() + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            print('File found')
                                        fin = open(file, 'rb')
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    try:
                                        fout = open(file, 'wb')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = sc.base64Crypt(ciphertext, False)
                                    fout.write(plaintext)
                                    fout.close()
                                        
                                    print('\nContents of the file is successfully decrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '3':
                            break
                        elif choice2 == '4': # exit
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                
                elif choice1 == '6': # Affine Cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                   AFFINE CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
             AFFINE CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Please ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter your Message: ' + plaintext)
                                            print('Length of the Plaintext: ' + str(len(plaintext)))
                                            k1 = int(input('Enter Key - 1: '))
                                            if k1 <= 0:
                                                raise ValueError
                                            if math.gcd(k1, len(plaintext)) == 1:
                                                break
                                            else:
                                                print('ERROR: GCD of Key1 and size of message should be exactly 1')
                                                print('i.e. Key1 and length of message must have to be coprime')
                                                input('Press ENTER to continue...')
                                                continue
                                        except ValueError:
                                            print('ERROR: Key1 should be a finite integral value > 0')
                                            print('Please ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter your Message: ' + plaintext)
                                            print('Length of the Plaintext: ' + str(len(plaintext)))
                                            print('Enter Key - 1: ' + str(k1))
                                            k2 = int(input('Enter Key - 2: '))
                                            if k2 < 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Key2 should be a finite integral value >= 1')
                                            print('Please ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + sc.AffineCipher(plaintext, k1, k2) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2': # Fetch from File
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            print('Length of the text: ' + str(len(plaintext)))
                                            k1 = int(input('\nEnter Key - 1: '))
                                            if k1 <= 0:
                                                raise ValueError
                                            if math.gcd(k1, len(plaintext)) == 1:
                                                break
                                            else:
                                                print('ERROR: GCD of Key1 and size of message should be exactly 1')
                                                print('i.e. Key1 and length of message must have to be coprime')
                                                input('Press ENTER to continue...')
                                                continue
                                        except ValueError:
                                            print('ERROR: Key1 should be a finite integral value > 0')
                                            print('Please ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            print('Length of the text: ' + str(len(plaintext)))
                                            print('\nEnter Key - 1: ' + str(k1))
                                            k2 = int(input('Enter Key - 2: '))
                                            if k2 < 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Key2 should be a finite integral value >= 1')
                                            print('Please ENTER to continue...')
                                            
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = sc.AffineCipher(plaintext, k1, k2)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully encrypted')
                                    input('Please ENTER to continue...')
                                            
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
             AFFINE CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Please ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            print('Length of the Ciphertext: ' + str(len(ciphertext)))
                                            k1 = int(input('Enter Key - 1: '))
                                            if k1 < 1:
                                                raise ValueError
                                            if math.gcd(k1, len(ciphertext) == 1):
                                                break
                                            else:
                                                print('ERROR: GCD of Key1 and size of message should be exactly 1')
                                                print('i.e. Key1 and length of message must have to be coprime')
                                                input('Press ENTER to continue...')
                                                continue
                                        except ValueError:
                                            print('ERROR: Key1 should be a finite integral value > 0')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Cipertext: ' + ciphertext)
                                            print('Length of the Ciphertext: ' + str(len(ciphertext)))
                                            print('Enter Key - 1: ' + str(k1))
                                            k2 = int(input('Enter Key - 2: '))
                                            if k2 < 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Key2 should be a finite integral value >= 1')
                                            
                                    print('Decrypted Message: \'' + sc.AffineCipher(ciphertext, k1, k2, False) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2': # Fetch from File
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            print('Length of the text: ' + str(len(ciphertext)))
                                            k1 = int(input('\nEnter Key - 1: '))
                                            if k1 <= 0:
                                                raise ValueError
                                            if math.gcd(k1, len(ciphertext)) == 1:
                                                break
                                            else:
                                                print('ERROR: GCD of Key1 and size of message should be exactly 1')
                                                print('i.e. Key1 and length of message must have to be coprime')
                                                input('Press ENTER to continue...')
                                                continue
                                        except ValueError:
                                            print('ERROR: Key1 should be a finite integral value > 0')
                                            print('Please ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            print('Length of the text: ' + str(len(ciphertext)))
                                            print('Enter Key - 1: ' + str(k1))
                                            k2 = int(input('Enter Key - 2: '))
                                            if k2 < 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Key2 should be a finite integral value >= 1')
                                            print('Please ENTER to continue...')
                                            
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = sc.AffineCipher(ciphertext, k1, k2, False)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully decrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                        elif choice2 == '3':
                            break
                        elif choice2 == '4': # exit
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                                
                elif choice1 == '7': # Playfair Cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                  PLAYFAIR CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
             PLAYFAIR CIPHER ENCRYPTION
***************************************************
                                        ''')
                                    print('Please note that in this cipher consequtive repeating pair of characters of')
                                    print('the text will be substituted with a X character next to it. Spaces and special')
                                    print('characters will be removed. Also wherever necessary a padding of X will be')
                                    print('added an the end.')
                                    plaintext = str(input('Enter your Message: '))
                                    c = len(plaintext)
                                    assert c > 0
                                except AssertionError:
                                    print('ERROR: Empty string cannot be encrypted')
                                    input('Press ENTER to continue...')
                                    
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
             PLAYFAIR CIPHER ENCRYPTION
***************************************************
                                        ''')
                                    print('Please note that in this cipher consequtive repeating pair of characters of')
                                    print('the text will be substituted with a X character next to it. Spaces and special')
                                    print('characters will be removed. Also wherever necessary a padding of X will be')
                                    print('added an the end.')
                                    print('Enter your Message: ' + plaintext)
                                    keyword = str(input('Enter Secret Keyword: '))
                                    c = len(keyword)
                                    assert c >= 3
                                except AssertionError:
                                    print('ERROR: Secret Keyword should be minimum of 3 characters long')
                                    input('Press ENTER to continue...')
                                            
                            print('Encrypted Message: \'' + sc.PlayfairCipher(plaintext, keyword) + '\'')
                            input('Press ENTER to continue...')
                                            
                        elif choice2 == '2':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
             PLAYFAIR CIPHER DECRYPTION
***************************************************
                                        ''')
                                    ciphertext = str(input('Enter the Ciphertext: '))
                                    c = len(ciphertext)
                                    assert c > 0
                                except AssertionError:
                                    print('ERROR: Empty string cannot be encrypted')
                                    input('Press ENTER to continue...')
                                    
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
             PLAYFAIR CIPHER DECRYPTION
***************************************************
                                        ''')
                                    print('Enter the Ciphertext: ' + ciphertext)
                                    keyword = str(input('Enter Secret Keyword: '))
                                    c = len(keyword)
                                    assert c > 0
                                except AssertionError:
                                    print('ERROR: Secret Keyword should be minimum of 3 characters long')
                                    input('Press ENTER to continue...')
                                    
                            print('Decrypted Message: \'' + sc.PlayfairCipher(ciphertext, keyword, False) + '\'')
                            input('Press ENTER to continue...')
                                
                        elif choice2 == '3':
                            break
                        elif choice2 == '4': # exit
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                
                elif choice1 == '8': # Vigenere Cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                  VIGENÈRE CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
            VIGENÈRE CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be encrypted')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter your Message: ' + plaintext)
                                            keyword = str(input('Enter Secret Keyword: '))
                                            c = len(keyword)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Secret Keyword should be minimum of 3 characters long')
                                            input('Press ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + sc.VigenereCipher(plaintext, keyword) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2': # fetch from file
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            keyword = str(input('\nEnter the Secret Keyword: '))
                                            c = len(keyword)
                                            assert c >= 3
                                        except AssertionError:
                                            print('ERROR: Secret Keyword should be minimum of 3 characters long')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = sc.VigenereCipher(plaintext, keyword)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully encrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
            VIGENÈRE CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decryted')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            keyword = str(input('Enter Secret Keyword: '))
                                            c = len(keyword)
                                            assert c >= 3
                                        except AssertionError:
                                            print('ERROR: Secret Keyword should be minimum of 3 characters long')
                                            input('Press ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + sc.VigenereCipher(ciphertext, keyword, False) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2': 
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            keyword = str(input('\nEnter the Secret Keyword: '))
                                            c = len(keyword)
                                            assert c >= 3
                                        except AssertionError:
                                            print('ERROR: Secret Keyword should be minimum of 3 characters long')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = sc.VigenereCipher(ciphertext, keyword, False)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully decrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '3':
                            break
                        elif choice2 == '4': # exit
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
  
                elif choice1 == '9': # OTP
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                ONE-TIME PAD (OTP)
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  OTP ENCRYPTION
***************************************************
                                        ''')
                                    plaintext = str(input('Enter a Message: '))
                                    c = len(plaintext)
                                    assert c > 0
                                except AssertionError:
                                    print('ERROR: Empty string cannot be encrypted')
                                    input('Press ENTER to continue...')
                                    
                            key, encrypt = sc.OTPEncrypt(plaintext)
                            print('Your Key is: \'' + key + '\'')
                            print('Encrypted Message: \'' + encrypt + '\'')
                            print('Please keep the Key secret, if you lost it, you will not be able to decrypt the enciphered message')
                            print()
                            input('Press ENTER to continue...')
                                
                        elif choice2 == '2':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  OTP DECRYPTION
***************************************************
                                        ''')
                                    ciphertext = str(input('Enter the Ciphertext: '))
                                    c = len(ciphertext)
                                    assert c > 0
                                except AssertionError:
                                    print('ERROR: Empty string cannot be encrypted')
                                    input('Press ENTER to continue...')
                                    
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  OTP DECRYPTION
***************************************************
                                        ''')
                                    print('Enter the Ciphertext: ' + ciphertext)
                                    key = str(input('Enter the Secret Key: '))
                                    c = len(key)
                                    assert c > 0 and c == len(ciphertext)
                                except AssertionError:
                                    print('ERROR: Length of the Secret Keyword should be equal to the length of the ciphertext')
                                    input('Press ENTER to continue...')
                                    
                            print('Decrypted Message: \'' + sc.OTPDecrypt(ciphertext, key) + '\'')
                            input('Press ENTER to continue...')
                                    
                        elif choice2 == '3':
                            break
                        elif choice2 == '4': # exit
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                                
                elif choice1 == '10': # go back
                    break
                elif choice1 == '11': # exit
                    menu.ChoiceExit()
                else:
                    menu.NoChoiceExit3(choice1)
                    
        elif choice == '2': # Transposition cipher
            ch1 = 'Y'
            while ch1 == 'Y' or ch1 == 'y':
                choice1 = menu.MenuTransposition()
                
                if choice1 == '1': # Simple Transposition cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
            SIMPLE TRANSPOSITION CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu1()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
      SIMPLE TRANSPOSITION CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be encrypted')
                                            input('Press ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter your Message: ' + plaintext)
                                            key = int(input('Enter Key(No. of Columns): '))
                                            if key <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Number of columns is a integral value which should be greater than 1')
                                            input('Press ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + tc.STCE(plaintext, key) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = int(input('\nEnter key(Number of Coloumns): '))
                                            if key <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Number of columns is a integral value which should be greater than 1')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = tc.STCE(plaintext, key)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully encrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
      SIMPLE TRANSPOSITION CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            key = int(input('Enter Key(No. of Columns): '))
                                            if key <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Number of coloumns is a integral value which is greater than 1')
                                            input('Press ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + tc.STCD(ciphertext, key) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = int(input('\nEnter key(Number of Coloumns): '))
                                            if key <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Number of columns is a integral value which should be greater than 1')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = tc.STCD(ciphertext, key)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully decrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '3':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
  SIMPLE TRANSPOSITION CIPHER BRUTE-FORCE ATTACK
***************************************************
                                      ''')
                                    ciphertext = str(input('Enter your Message: '))
                                    c = len(ciphertext)
                                    assert c > 0
                                except AssertionError:
                                    print('\nERROR: Empty string cannot be encrypted')
                                    input('Press ENTER to continue...')
                                            
                            print('\nBrute-Force Decryption: ')
                            tc.STCBFD(ciphertext)
                            input('\nPress ENTER to continue...')
                                    
                        elif choice2 == '4':
                            break
                        elif choice2 == '5':
                            menu.ChoiceExit()
                        else:  
                            menu.NoChoiceExit1(choice2)
                        
                elif choice1 == '2': # RailFence cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                 RAIL-FENCE CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu1()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
           RAIL-FENCE CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be encrypted')
                                            input('Press ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter your Message: ' + plaintext)        
                                            depth = int(input('Enter the depth of Rail-Fence: '))
                                            if depth <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Depth of Rail-Fence must have to be greater than 1')
                                            input('Press ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + tc.RailFenceEncrypt(plaintext, depth) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            depth = int(input('Enter the depth of Rail-Fence: '))
                                            if depth <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Depth of Rail-Fence must have to be greater than 1')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = tc.STCE(plaintext, depth)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully encrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
           RAIL-FENCE CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be encrypted')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            depth = int(input('Enter the depth of the Rail-Fence: '))
                                            if depth <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Depth of Rail-Fence must have to be greater than 1')
                                            input('Press ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + tc.RailFenceDecrypt(ciphertext, depth) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            depth = int(input('Enter the depth of Rail-Fence: '))
                                            if depth <= 1:
                                                raise ValueError
                                            break
                                        except ValueError:
                                            print('ERROR: Depth of Rail-Fence must have to be greater than 1')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = tc.STCD(ciphertext, depth)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully decrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '3':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
       RAIL-FENCE CIPHER BRUTE-FORCE ATTACK
***************************************************
                                        ''')
                                    ciphertext = str(input('Enter the Ciphertext: '))
                                    c = len(ciphertext)
                                    assert c > 0
                                except AssertionError:
                                    print('ERROR: Empty string cannot be decrypted')
                                    input('Press ENTER to continue...')
                                    
                                print('Brute-Force Decryption: ')
                                tc.RailFenceBruteForce(ciphertext)
                                input('Press ENTER to continue...')
                                    
                        elif choice2 == '4':
                            break
                        elif choice2 == '5':
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit1(choice2)
                                
                elif choice1 == '3': # Coloumnar Cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                  COLUMNAR CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
            COLUMNAR CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the plaintext contains the \'~\' character, it will be considered as padding.')
                                            plaintext = str(input('\nEnter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be encrypted')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the plaintext contains the \'~\' character, it will be considered as padding too.')
                                            print('\nEnter your Message: ' + plaintext)
                                            key = str(input('Enter Key: '))
                                            c = len(key)
                                            assert c >= 3
                                            for i in range(len(key)):
                                                for j in range(len(key)):
                                                    if i == j:
                                                        continue
                                                    if key[i] == key[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Key should be a minimum of 3 characters long')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Key for Coloumnar cipher should have distict characters')
                                            input('Press ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + tc.ColumnarEncrypt(plaintext, key) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            file = str(input('\nEnter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = str(input('Enter Key: '))
                                            c = len(key)
                                            assert c > 3
                                            for i in range(len(key)):
                                                for j in range(len(key)):
                                                    if i == j:
                                                        continue
                                                    if key[i] == key[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of key should be at least 3 characters long') 
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Key for Coloumnar cipher should have distinct characters')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = tc.ColumnarEncrypt(plaintext, key)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully encrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
            COLUMNAR CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            key = str(input('Enter Key: '))
                                            c = len(key)
                                            assert c > 3
                                            for i in range(len(key)):
                                                for j in range(len(key)):
                                                    if i == j:
                                                        continue
                                                    if key[i] == key[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Key should be a minimum of 3 characters long')
                                            print('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Invalid Key')
                                            print('Press ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + tc.ColumnarDecrypt(ciphertext, key) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key = str(input('Enter Key: '))
                                            c = len(key)
                                            assert c > 3
                                            for i in range(len(key)):
                                                for j in range(len(key)):
                                                    if i == j:
                                                        continue
                                                    if key[i] == key[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of key should be at least 3 characters long') 
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Invalid Key')
                                            input('Press ENTER to continue...')
                                          
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = tc.ColumnarDecrypt(ciphertext, key)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully decrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '3':
                            break
                        elif choice2 == '4':
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                                            
                elif choice1 == '4': # Double Transposition Cipher
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
       DOUBLE COLUMNAR TRANSPOSITION CIPHER
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
  DOUBLE COLUMNAR TRANSPOSITION CIPHER ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            plaintext = str(input('\nEnter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Press ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            print('\nEnter your Message: ' + plaintext)
                                            key1 = str(input('Enter Key - 1: '))
                                            c = len(key1)
                                            assert c >= 3
                                            for i in range(len(key1)):
                                                for j in range(len(key1)):
                                                    if i == j:
                                                        continue
                                                    if key1[i] == key1[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key1 should be at least 3 characters in size')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Key1 can accept only string of distinct characters')
                                            input('Press ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            print('\nEnter your Message: ' + plaintext)
                                            print('Enter Key - 1: ' + key1)
                                            key2 = str(input('Enter Key - 2: '))
                                            c = len(key2)
                                            assert len(key2) == len(key1)
                                            for i in range(len(key2)):
                                                for j in range(len(key2)):
                                                    if i == j:
                                                        continue
                                                    if key2[i] == key2[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key2 should be equal to the length of Key1')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Key2 can accept only string of distinct characters')
                                            input('Press ENTER to continue...')
                                            
                                    print('Encrypted Message: \'' + tc.DCTE(plaintext, key1, key2) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            file = str(input('\nEnter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    if len(plaintext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            print('\nEnter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key1 = str(input('\nEnter Key - 1: '))
                                            c = len(key1)
                                            assert c >= 3
                                            for i in range(len(key1)):
                                                for j in range(len(key1)):
                                                    if i == j:
                                                        continue
                                                    if key1[i] == key1[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key1 should be at least 3 characters in size')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Key1 can accept only string of distinct characters')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('In this cipher, when required, a padding of \'~\' character will be added.')
                                            print('But if the text contains the \'~\' character, it will be considered as padding as well')
                                            print('\nEnter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            print('\nEnter Key - 1: ' + key1)
                                            key2 = str(input('Enter Key - 2: '))
                                            c = len(key2)
                                            assert len(key2) == len(key1)
                                            for i in range(len(key2)):
                                                for j in range(len(key2)):
                                                    if i == j:
                                                        continue
                                                    if key2[i] == key2[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key2 should be equal to the length of Key1')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Key2 can accept only string of distinct characters')
                                            input('Press ENTER to continue...')
                                            
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = tc.DCTE(plaintext, key1, key2)
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully encrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
  DOUBLE COLUMNAR TRANSPOSITION CIPHER DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            ciphertext = str(input('Enter the Ciphertext: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be decrypted')
                                            input('Press ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            key1 = str(input('Enter Key - 1: '))
                                            c = len(key1)
                                            assert c >= 3
                                            for i in range(len(key1)):
                                                for j in range(len(key1)):
                                                    if i == j:
                                                        continue
                                                    if key1[i] == key1[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key1 should be at least 3 characters in size')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Invalid Key')
                                            input('Press ENTER to continue...')
                                            
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the Ciphertext: ' + ciphertext)
                                            print('Enter Key - 1: ' + key1)
                                            key2 = str(input('Enter Key - 2: '))
                                            c = len(key2)
                                            assert len(key2) == len(key1)
                                            for i in range(len(key2)):
                                                for j in range(len(key2)):
                                                    if i == j:
                                                        continue
                                                    if key2[i] == key2[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key2 should be equal to the length of Key1')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Invalid Key')
                                            input('Press ENTER to continue...')
                                            
                                    print('Decrypted Message: \'' + tc.DCTD(ciphertext, key1, key2) + '\'')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c >= 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    if len(ciphertext) == 0:
                                        print('ERROR: File is empty')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            key1 = str(input('\nEnter Key - 1: '))
                                            c = len(key1)
                                            assert c >= 3
                                            for i in range(len(key1)):
                                                for j in range(len(key1)):
                                                    if i == j:
                                                        continue
                                                    if key1[i] == key1[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key1 should be at least 3 characters in size')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Invalid Key')
                                            input('Press ENTER to continue...')
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            if flag == True:
                                                print('File Found')
                                            print('\nEnter Key - 1: ' + key1)
                                            key2 = str(input('Enter Key - 2: '))
                                            c = len(key2)
                                            assert len(key2) == len(key1)
                                            for i in range(len(key2)):
                                                for j in range(len(key2)):
                                                    if i == j:
                                                        continue
                                                    if key2[i] == key2[j]:
                                                        c = 0
                                                        raise TypeError
                                        except AssertionError:
                                            print('ERROR: Length of Key2 should be equal to the size of Key1')
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Invalid Key')
                                            input('Press ENTER to continue...')
                                            
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    plaintext = tc.DCTD(ciphertext, key1, key2)
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                            
                                    print('Contents of the file are successfully decrypted')
                                    input('Please ENTER to continue...')
                                    
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '3':
                            break
                        elif choice2 == '4':
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
        
                elif choice1 == '5':
                    break
                elif choice1 == '6':
                    menu.ChoiceExit()
                else:
                    menu.NoChoiceExit5()
                
        elif choice == '3': # Private-Key Cryptography
            ch1 = 'Y'
            while ch1 == 'Y' or ch1 == 'y':
                choice1 = menu.MenuXKC()
                
                if choice1 == '1': # DES
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
             DATA ENCRYPTION STANDARD
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            c = 0
                            flag = False
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  DES ENCRYPTION
***************************************************
                                        ''')
                                    file = str(input('Enter the absolute path of the TEXT file: '))
                                    c = len(file)
                                    assert c >= 1
                                except AssertionError:
                                    print('ERROR: The minimum size of the filename should be at least 1')
                                    input('Please ENTER to continue...')
                                    
                            try:
                                if os.path.exists(file):
                                    flag = True
                                fin = open(file)
                            except (IOError, FileNotFoundError):
                                print('Error: Either I/O access is restricted or the File not found')
                                input('Press ENTER to continue...')
                                
                            plaintext = fin.read()
                            fin.close()
                            
                            if len(plaintext) == 0:
                                print('ERROR: File is empty')
                                input('Press ENTER to continue...')
                                break
                            
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
                  DES ENCRYPTION
***************************************************
                                        ''')
                                    print('Enter the absolute path of the TEXT file: ' + file)
                                    if flag == True:
                                        print('File Found')
                                    key = str(input('Enter the Secret key: '))
                                    c = len(key)
                                    assert c > 0 and c <= 8
                                except AssertionError:
                                    print('ERROR: DES Key size should be in range 1 - 8')
                                    input('Press ENTER to continue...')
                            
                            START = time.time()
                            ciphertext = xkc.DES_Cipher(plaintext, key)
                            END = time.time()
                            timespan = END - START
                            print('Encrption Complete!')
                            print('Encryption finished in {} seconds'.format(timespan))
                                    
                            try:
                                fout = open(file, 'w')
                            except IOError:
                                print('ERROR: Write access is restricted')
                                input('Press ENTER to continue...')
                                break
                                    
                            fout.write(ciphertext)
                            fout.close()
                                    
                            print('Contents of the text file successfully encrypted')
                            input('Press ENTER to continue...')
                                            
                        elif choice2 == '2':
                            c = 0
                            flag = False
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  DES DECRYPTION
***************************************************
                                        ''')
                                    file = str(input('Enter the absolute path of the TEXT file: '))
                                    c = len(file)
                                    assert c >= 1
                                except AssertionError:
                                    print('ERROR: The minimum size of the filename should be at least 1')
                                    input('Please ENTER to continue...')
                                    
                            try:
                                if os.path.exists(file):
                                    flag = True
                                fin = open(file)
                            except (IOError, FileNotFoundError):
                                print('Error: Either I/O access is restricted or the File not found')
                                input('Press ENTER to continue...')
                                    
                            ciphertext = fin.read()
                            fin.close()
                            
                            if len(plaintext) == 0:
                                print('ERROR: File is empty')
                                input('Press ENTER to continue...')
                                break
                            
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
                  DES DECRYPTION
***************************************************
                                        ''')
                                    print('Enter the absolute path of the TEXT file: ' + file)
                                    if flag == True:
                                        print('File Found')
                                    key = str(input('Enter the Secret key: '))
                                    c = len(key)
                                    assert c > 0 and c <= 8
                                except AssertionError:
                                    print('ERROR: DES Key size should be in range 0 - 8')
                                    input('Press ENTER to continue...')
                                
                            START = time.time()
                            plaintext = xkc.DES_Cipher(ciphertext, key, False)
                            END = time.time()
                            timespan = END - START
                            print('Decrption Complete!')
                            print('Decryption finished in {} seconds'.format(timespan))
                            
                            try:
                                fout = open(file, 'w')
                                # certain texts in the file are not decoded properly
                                # Encoding should be in Windows(CRLF) UTF-8
                            except IOError:
                                print('ERROR: Write access is restricted')
                                input('Press ENTER to continue...')
                                break
                                    
                            fout.write(plaintext)
                            fout.close()
                                    
                            print('Contents of the text file successfully decrypted')
                            input('Press ENTER to continue...')
                        
                        elif choice2 == '3':
                            break
                        elif choice2 == '4':
                            menu.ChoiceExit()
                        else:  
                            menu.NoChoiceExit2(choice2)
                
                elif choice1 == '2': # Triple DES
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
          TRIPLE DATA ENCRYPTION STANDARD
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  TDES ENCRYPTION
***************************************************
                                  ''')
                                    file = str(input('Enter the absolute path of the TEXT file: '))
                                    c = len(file)
                                    assert c >= 1
                                except AssertionError:
                                    print('ERROR: The minimum size of the filename should be at least 1')
                                    input('Please ENTER to continue...')
                                    
                            try:
                                if os.path.exists(file):
                                    flag = True
                                fin = open(file)
                            except (IOError, FileNotFoundError):
                                print('Error: Either I/O access is restricted or the File not found')
                                input('Press ENTER to continue...')
                                            
                            plaintext = fin.read()
                            fin.close()
                            
                            if len(plaintext) == 0:
                                print('ERROR: File is empty')
                                input('Press ENTER to continue...')
                                break
                            
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
                  TDES ENCRYPTION
***************************************************
                                        ''')
                                    print('Enter the absolute path of the TEXT file: ' + file)
                                    if flag == True:
                                        print('File Found')
                                    key = str(input('Enter the Secret key: '))
                                    c = len(key)
                                    assert c > 0 and c <= 24
                                except AssertionError:
                                    print('ERROR: TDES Key size should be in range 1 - 24')
                                    input('Press ENTER to continue...')
                            
                            START = time.time()
                            ciphertext = xkc.TDES_Cipher(plaintext, key)
                            END = time.time()
                            timespan = END - START
                            print('Encrption Complete!')
                            print('Encryption finished in {} seconds'.format(timespan))
                                    
                            try:
                                fout = open(file, 'w')
                            except IOError:
                                print('ERROR: Write access is restricted')
                                input('Press ENTER to continue...')
                                break
                                    
                            fout.write(ciphertext)
                            fout.close()
                                    
                            print('Contents of the text file successfully encrypted')
                            input('Press ENTER to continue...')
                                            
                        elif choice2 == '2':
                            c = 0
                            flag = False
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  TDES DECRYPTION
***************************************************
                                        ''')
                                    file = str(input('Enter the absolute path of the TEXT file: '))
                                    c = len(file)
                                    assert c >= 1
                                except AssertionError:
                                    print('ERROR: The minimum size of the filename should be at least 1')
                                    input('Please ENTER to continue...')
                                    
                            try:
                                if os.path.exists(file):
                                    flag = True
                                fin = open(file)
                            except (IOError, FileNotFoundError):
                                print('Error: Either I/O access is restricted or the File not found')
                                input('Press ENTER to continue...')
                                   
                            ciphertext = fin.read()
                            fin.close()
                            
                            if len(plaintext) == 0:
                                print('ERROR: File is empty')
                                input('Press ENTER to continue...')
                                break
                            
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
                  TDES DECRYPTION
***************************************************
                                        ''')
                                    print('Enter the absolute path of the TEXT file: ' + file)
                                    if flag == True:
                                        print('File Found')
                                    key = str(input('Enter the Secret key: '))
                                    c = len(key)
                                    assert c > 0 and c <= 24
                                except AssertionError:
                                    print('ERROR: TDES Key size should be in range 0 - 24')
                                    input('Press ENTER to continue...')
                                   
                            START = time.time()
                            plaintext = xkc.TDES_Cipher(ciphertext, key, False)
                            END = time.time()
                            timespan = END - START
                            print('Decrption Complete!')
                            print('Decryption finished in {} seconds'.format(timespan))
                            os.remove(file)
                                    
                            try:
                                fout = open(file, 'w')
                                # certain texts in the file are not decoded properly
                                # Encoding should be in Windows(CRLF) UTF-8
                            except IOError:
                                print('ERROR: Write access is restricted')
                                input('Press ENTER to continue...')
                                break
                                    
                            fout.write(plaintext)
                            fout.close()
                                    
                            print('Contents of the text file successfully decrypted')
                            input('Press ENTER to continue...')
                        
                        elif choice2 == '3':
                            break
                        elif choice2 == '4':
                            menu.ChoiceExit()
                        else:  
                            menu.NoChoiceExit2(choice2)
                
                elif choice1 == '3': # AES
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
           ADVANCED ENCRYPTION STANDARD
***************************************************
                        ''')
                        choice2 = menu.OperationMenu2()
                        
                        if choice2 == '1':
                            c = 0
                            flag = False
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  AES ENCRYPTION
***************************************************
                                        ''')
                                    print('NOTE: This function can encrypt a file of any kind')
                                    file = str(input('Enter the absolute path of the file: '))
                                    c = len(file)
                                    assert c >= 1
                                except AssertionError:
                                    print('ERROR: The minimum size of the filename should be at least 1')
                                    input('Please ENTER to continue...')
                                    
                            try:
                                if os.path.exists(file):
                                    flag = True
                                fin = open(file, 'rb') # opening a new file to read from in binary mode
                            except (IOError, FileNotFoundError):
                                print('ERROR: Either I/O access is restricted or the File not found')
                                input('Press ENTER to continue...')
                            
                            plaintext = fin.read()
                            fin.close()
                            
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
                  AES ENCRYPTION
***************************************************
                                        ''')
                                    print('NOTE: This function can encrypt a file of any kind')
                                    print('Enter the absolute path of the file: ' + file)
                                    password = bytes(input('\nEnter a Password: '), 'utf-8')
                                    c = len(password)
                                    assert c >= 8 and c <= 32
                                except AssertionError:
                                    print('ERROR: AES Key size should be in range 8 - 32')
                                    input('Press ENTER to continue...')
                                    
                            print('\nPlease wait while your data is being encrypted...')
                            START = time.time()
                            ciphertext = xkc.AES_Encrypt(plaintext, password)
                            END = time.time()
                            timespan = END - START
                            print('Encryption Complete!')
                            print('Encryption process finished in {} seconds'.format(timespan))
                            
                            try:
                                fout = open(file, 'wb')
                            except IOError:
                                print('ERROR: Write access is restricted')
                                input('Press ENTER to continue...')
                                break
                                        
                            fout.write(ciphertext)
                            fout.close()
                                    
                            print('\nYour file is encrypted successfully.')
                            input('Press ENTER to continue...')
                                            
                        elif choice2 == '2':
                            c = 0
                            flag = False
                            while c == 0:
                                try:
                                    menu.clrscrn() 
                                    print('''
***************************************************
                  AES DECRYPTION
***************************************************
                                        ''')
                                    file = str(input('Enter the absolute path of the file: '))
                                    c = len(file)
                                    assert c >= 1
                                except AssertionError:
                                    print('ERROR: The minimum size of the filename should be at least 1')
                                    input('Please ENTER to continue...')
                                    
                            try:
                                if os.path.exists(file):
                                    flag = True
                                fin = open(file, 'rb')
                            except (IOError, FileNotFoundError):
                                print('ERROR: Either I/O access is restricted or the File not found')
                                input('Press ENTER to continue...')
                                
                            ciphertext = fin.read()
                            fin.close()
                            
                            c = 0
                            while c == 0:
                                try:
                                    menu.clrscrn()
                                    print('''
***************************************************
                  AES DECRYPTION
***************************************************
                                        ''')
                                    print('Enter the absolute path of the file: ' + file)
                                    password = bytes(input('\nEnter the Password: '), 'utf-8')
                                    c = len(password)
                                    assert c >= 8 and c <= 32
                                except AssertionError:
                                    print('ERROR: AES Key size should be in range 8 - 32')
                                    input('Press ENTER to continue...')
                                    
                            print('\nPlease wait while your data is being decrypted...')
                            START = time.time()
                            plaintext= xkc.AES_Decrypt(ciphertext, password)
                            END = time.time()
                            if plaintext == bytes(1):
                                print('\nERROR: Either the entered password is invalid or ciphertext is corrupted or tampered')
                                input('Press any key to continue')
                                break
                            timespan = END - START
                            print('Decryption Complete!')
                            print('Decryption process finished in {} seconds'.format(timespan))
                                    
                            try:
                                fout = open(file, 'wb')
                            except IOError:
                                print('ERROR: Write access is restricted!')
                                input('Press ENTER to continue...')
                                break
                                    
                            fout.write(plaintext)
                            fout.close()
                                    
                            print('\nYour file is decrypted successfully')
                            input('Press ENTER to continue...')
                                    
                        elif choice2 == '3':
                            break
                        elif choice2 == '4':
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                                    
                elif choice1 == '4': # go back
                    break
                elif choice1 == '5': # exit
                    menu.ChoiceExit()
                else:
                    menu.NoChoiceExit1(choice1)
                          
        elif choice == '4': # Public-Key Cryptography
            ch1 = 'Y'
            while ch1 == 'Y' or ch1 == 'y':
                choice1 = menu.MenuPKC()
                
                if choice1 == '1': # RSA
                    ch2 = 'Y'
                    while ch2 == 'Y' or ch2 == 'y':
                        menu.clrscrn() 
                        print('''
***************************************************
                 RSA CRYPTOGRAPHY
***************************************************
                        ''')
                        choice2 = menu.OperationMenu3()
                        
                        if choice2 == '1':
                            menu.clrscrn() 
                            p = q = 0
                            while isPrime(p) == False:
                                print('''
***************************************************
                RSA KEY GENERATION
***************************************************
                                  ''')
                                print('Enter two prime numbers: ')
                                print('(The larger the number, the stronger the encryption but takes longer time to execute)')
                                print()
                                try:
                                    p = int(input('a. Prime #1: '))
                                except ValueError:
                                    print('This Field can accept only integer values with base 10')
                                    input('Press ENTER to continue...')
                                    menu.clrscrn()
                                    continue
                                    
                                if isPrime(p):
                                    break
                                else:
                                    print('Not a Prime number!')
                                    input('Press ENTER to continue...')
                                    menu.clrscrn()
                                    continue
                                    
                            while isPrime(q) == False:
                                menu.clrscrn()
                                print('''
***************************************************
                RSA KEY GENERATION
***************************************************
                                  ''')
                                print('Enter two prime numbers: ')
                                print('(The larger the number, the stronger the encryption but takes longer time to execute)')
                                print()
                                print('a. Prime #1: {}'.format(p))
                                try:
                                    q = int(input('b. Prime #2: '))
                                except ValueError:
                                    print('This Field can accept only integer values with base 10')
                                    input('Press ENTER to continue...')
                                    menu.clrscrn()
                                    continue
                                    
                                if isPrime(q):
                                    break
                                else:
                                    print('Not a Prime number!')
                                    input('Press ENTER to continue...')
                                    menu.clrscrn()
                                    continue
                                        
                            print('\nGenerating Keys: ')
                            private_key, public_key = pkc.RSA_KEYGEN(p, q)
                            print('Your Public-Key is:', public_key)
                            print('Your Private-Key is:', private_key)
                                
                            input('Press ENTER to continue...')
                                    
                        elif choice2 == '2':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
                  RSA ENCRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            plaintext = str(input('Enter your Message: '))
                                            c = len(plaintext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty message cannot be encrypted')
                                            input('Press ENTER to continue...')

                                    c = 0
                                    while c == 0:
                                        menu.clrscrn()
                                        print('Enter your Message: ' + plaintext)
                                        try:
                                            x = str(input("Enter Receipent's Public Key: "))
                                            c = len(x)
                                            assert ',' in x and c > 3
                                            for i in x:
                                                if i in ' ,0123456789':
                                                    continue
                                                else:
                                                    raise TypeError
                                        except AssertionError:
                                            print('ERROR: Invalid Key')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Entry for Public Key should be in the form \'x, y\' where x and y are integers of base 10')
                                            c = 0
                                            input('Press ENTER to continue...')
                                   
                                    n, e = x.replace(' ', '').split(',')
                                    recipents_public_key = int(n), int(e)
                                    
                                    print('\nPlease wait while your data is being encrypted...')
                                    START = time.time()
                                    ciphertext = pkc.RSA_CRYPT(plaintext, recipents_public_key)
                                    END = time.time()
                                    timespan = END - START
                                    print('Your Ciphertext is: ' + '\'' + ciphertext + '\'') # output maybe illegible
                                    print('Encryption Process finished in {} seconds.'.format(timespan))
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c > 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                    
                                    plaintext = fin.read()
                                    fin.close()
                                    
                                    c = 0
                                    while c == 0:
                                        menu.clrscrn()
                                        print('Enter the absolute path of the TEXT file: ' + file)
                                        try:
                                            recipents_public_key = str(input("\nEnter Receipent's Public Key: "))
                                            c = len(recipents_public_key)
                                            assert ',' in recipents_public_key and c > 3
                                            for i in recipents_public_key:
                                                if i in ' ,0123456789':
                                                    continue
                                                else:
                                                    raise TypeError
                                        except AssertionError:
                                            print('ERROR: Invalid Key')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Entry for Public Key should be in the form \'x, y\' where x and y are integers of base 10')
                                            c = 0
                                            input('Press ENTER to continue...')
                                            
                                    n, e = recipents_public_key.replace(' ', '').split(',')
                                    print('\nPlease wait while your data is being encrypted...')
                                    START = time.time()
                                    ciphertext = pkc.RSA_CRYPT(plaintext, (int(n), int(e)))
                                    END = time.time()
                                    timespan = END - START
                                    print('Encryption Complete!')
                                    print('Encryption process finished in {} seconds'.format(timespan))
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    fout.write(ciphertext)
                                    fout.close()
                                    
                                    print('Contents of the file are successfully encrypted')
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '3': # go back
                                    break
                                elif choice3 == '4': # exit
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                            
                        elif choice2 == '3':
                            ch3 = 'Y'
                            while ch3 == 'Y' or ch3 == 'y':
                                menu.clrscrn() 
                                print('''
***************************************************
                  RSA DECRYPTION
***************************************************
                                      ''')
                                choice3 = menu.InputMethod()
                                
                                if choice3 == '1':
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            x = str(input('\nEnter your Private Key: '))
                                            c = len(x)
                                            assert ',' in x and c > 3
                                            for i in x:
                                                if i in ' ,0123456789':
                                                    continue
                                                else:
                                                    raise TypeError
                                        except AssertionError:
                                            print('ERROR: Invalid Key')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Entry for Private Key should be in the form \'x, y\' where x and y are integers of base 10')
                                            c = 0
                                            input('Press ENTER to continue...')
                                            
                                    n, d = x.replace(' ', '').split(',')
                                    private_key = int(n), int(d)
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('\nEnter your Private Key: ' + str(private_key))
                                            ciphertext = str(input('Copy and then Paste the Encrypted Message here: '))
                                            c = len(ciphertext)
                                            assert c > 0
                                        except AssertionError:
                                            print('ERROR: Empty string cannot be decrypted')
                                            input('Press ENTER to continue...')
                                            
                                    print('\nPlease wait while your data is being decrypted...')
                                    START = time.time()
                                    plaintext = pkc.RSA_CRYPT(ciphertext, private_key)
                                    END = time.time()
                                    timespan = END - START
                                    print('Your Decrypted Message is: \'' + plaintext + '\'')
                                    print('Decryption Process finished in {} seconds.'.format(timespan))
                                    input('Press ENTER to continue...')
                                    
                                elif choice3 == '2':
                                    c = 0
                                    flag = False
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            file = str(input('Enter the absolute path of the TEXT file: '))
                                            c = len(file)
                                            assert c > 1
                                        except AssertionError:
                                            print('ERROR: The minimum size of the filename should be at least 1')
                                            input('Please ENTER to continue...')
                                            
                                    try:
                                        if os.path.exists(file):
                                            flag = True
                                        fin = open(file)
                                    except (IOError, FileNotFoundError):
                                        print('Error: Either I/O access is restricted or the File not found')
                                        input('Press ENTER to continue...')
                                    
                                    ciphertext = fin.read()
                                    fin.close()
                                    
                                    c = 0
                                    while c == 0:
                                        try:
                                            menu.clrscrn()
                                            print('Enter the absolute path of the TEXT file: ' + file)
                                            x = str(input('Enter your Private Key: '))
                                            c = int(x)
                                            assert ',' in x and c > 3
                                            for i in x:
                                                if i in ' ,0123456789':
                                                    continue
                                                else:
                                                    raise TypeError
                                        except AssertionError:
                                            print('ERROR: Invalid Key')
                                            c = 0
                                            input('Press ENTER to continue...')
                                        except TypeError:
                                            print('ERROR: Entry for Public Key should be in the form \'x, y\' where x and y are integers of base 10')
                                            c = 0
                                            input('Press ENTER to continue...')
                                            
                                    n, d = x.replace(' ', '').split(',')
                                    private_key = int(n), int(d)
                                    
                                    print('\nPlease wait while your data is being decrypted...')
                                    START = time.time()
                                    plaintext = pkc.RSA_CRYPT(str(ciphertext), private_key)
                                    END = time.time()
                                    timespan = END - START
                                    print('Decryption Complete!')
                                    print('Decryption process finished in {} seconds'.format(timespan))
                                    
                                    try:
                                        fout = open(file, 'w')
                                    except IOError:
                                        print('ERROR: Write access is restricted!')
                                        input('Press ENTER to continue...')
                                        break
                                    
                                    fout.write(plaintext)
                                    fout.close()
                                    
                                    print('Contents of the file are successfully decrypted')
                                    input('Press ENTER to continue...')
                                
                                elif choice3 == '3':
                                    break
                                elif choice3 == '4':
                                    menu.ChoiceExit()
                                else:
                                    menu.NoChoiceExit2(choice3)
                                    
                        elif choice2 == '4':
                            break
                        elif choice2 == '5':
                            menu.ChoiceExit()
                        else:
                            menu.NoChoiceExit2(choice2)
                            
                elif choice1 == '2':
                    break
                elif choice1 == '3':
                    menu.ChoiceExit()
                else:
                    menu.NoChoiceExit4(choice1)
                                       
        elif choice == '5': # Exit
            menu.ChoiceExit() 
        else:
            menu.NoChoiceExit1(choice)
                    
if __name__ == '__main__':
    menu.clrscrn()
    if os.name == 'nt':
        print('System Detected:')
        os.system('ver')
        print()
        input('Press ENTER to continue...')
        main()
    else:
        print('System Detected:')
        os.system('uname --kernel-name --kernel-release --machine')
        print()
        input('Press ENTER to continue...')
        main()