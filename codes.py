#!/usr/bin/env python3
# Coded By AuxGrep
# 2023
# PY-APKTOOL 2023

import sys
import os
import time
import subprocess
import platform

""" ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

# check platform
if platform.system() != 'Linux' or platform.system() == 'Windows':
    os.system('clear')
    sys.system('use Linux !! fuck windows!! Exiting!!!!') 

# root check
if not 'SUDO_UID' in os.environ.keys():
    sys.exit('\nRun this Program as root')


# Function to validate user input
def validate_input(prompt, valid_options, error_message="Invalid input. Please try again."):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print(error_message)
# menu
os.system('clear')
main_menu = ['[1] Java 8 installation',
             '[2] Decompile APK',
             '[3] Compile APK',
             '[4] Sign Apk',
             '[5] Delete Compiled Apks',
             f'[0]{BOLD}{RED} === Exit ==={END}'
]

def py_easy_tool():
    while True:
        try:
            os.system('clear')
            print(f"{BOLD}{YELLOW}{NEGATIVE}==== PY APK EASY TOOL ===={END}".center(100))
            print(f'{BOLD}{BLUE}Author: AuxGrep{END}'.center(95))
            for x in main_menu:
                time.sleep(0.3)
                print(x)
            print('')
            user_choose = int(validate_input(f'{BOLD}{CYAN}Enter category No:{END} ', ['0','1', '2', '3', '4', '5']))

            if user_choose == 0:
                break
            
            # Add a function to install Java 8 and other dependencies
            elif user_choose == 1:    
                def install_java_8():
                    os.system('clear')
                    print(f'{BOLD}{YELLOW}Java 8 installation{END}'.center(100))
                    print(f'{BOLD}{GREEN}---> Installing nodejs{END}')
                    subprocess.run(['apt', 'install', 'npm', '-y'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                    print(f'{BOLD}{GREEN}---> Installing npm{END}')
                    subprocess.run(['apt', 'install', 'nodejs', '-y'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                    print(f'{BOLD}{GREEN}---> Installing aapt repackaging tool{END}')
                    subprocess.run(['apt', 'install', 'aapt', '-y'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                    print(f'{BOLD}{GREEN}---> Installing android-framework{END}')
                    subprocess.run(['apt', 'install', 'android-framework-res', '-y'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                    os.system('clear')
                    print(f'{BOLD}{YELLOW}unpacking JAVA 8{END}'.center(100))
                    try:
                        work_directory = os.getcwd()
                        if os.path.exists(f'{work_directory}/java-set/bin/java') == True:
                            pass
                        else:
                            os.system('clear')
                            sys.exit(f'{BOLD}{RED}java directory not FOund{END}')
                        os.system(f'update-alternatives --install "/usr/bin/java" "java" "{work_directory}/java-set/bin/java" 1')
                        print(f'{BOLD}{YELLOW}Kindly Choose java 8 as default{END}')
                        print('')
                        os.system('update-alternatives --config java')
                    except Exception as e:
                        os.system('clear')
                        print(f'{BOLD}{RED}We got Errors{END}')
                        sys.exit(e)   

                        
                install_java_8()
                input(f"{BOLD}{YELLOW}\nPress Enter to continue...{END}")
                    
            elif user_choose == 2:
                def get_apk_path(prompt):
                    while True:
                        apk_path = input(prompt)
                        if os.path.isfile(apk_path) and apk_path.endswith('.apk'):
                            return apk_path
                        else:
                            print(f'{BOLD}{RED}ERROR: Check the file path again and make sure it is apk!\n{END}')
                
                def decompile_apk():
                    os.system('clear')
                    print(f'{BOLD}{YELLOW}=== APK DECOMPILING ==={END}'.center(100))
                    apk = get_apk_path(f'{BOLD}{CYAN}Enter full path of apkfile(eg: /home/auxgrep/instagram.apk):{END} ')

                    with open('Apk-location.txt', mode='w') as andro_hacker:
                        andro_hacker.write(apk)

                    os.system('clear')

                    print(f'{BOLD}{YELLOW}=== APK DECOMPILING started ==={END}'.center(100))
                    print('')
                    grab_apk = apk.split('/')[-1]
                    grab_name = grab_apk.split('.apk')[0]
                    decompile = f"java -jar {os.getcwd()}/tools/apktool_2.7.0.jar d -f --only-main-classes -o {os.getcwd()}/Decompiled/{grab_name} {apk}"
                    start = os.system(decompile)
                decompile_apk()
                input(f"{BOLD}{YELLOW}\nPress Enter to continue...{END}")
                
            # HII ni function ya ku compile apk(build)   
            elif user_choose == 3:
                def compile_apk():
                    os.system('clear')
                    print(f'{BOLD}{YELLOW}=== APK COMPILING started ==={END}'.center(100))
                    print('')

                    with open('Apk-location.txt', mode='r') as apk:
                        check = apk.read()

                    # Get a list of directories in the "Decompiled" folder
                    directories = sorted([f for f in os.listdir(f'{os.getcwd()}/Decompiled') if os.path.isdir(os.path.join(f'{os.getcwd()}/Decompiled', f))])

                    # Print the list of directories and their corresponding numbers
                    for i, directory in enumerate(directories):
                        print(f'{i+1}. {directory}')

                    print('')

                    while True:
                        # Ask the user to input a number corresponding to the directory they want to compile
                        choice = input(f'{BOLD}{CYAN}Enter the number of the apk directory to compile (use "custom" if u have your own decompiled apk):{END} ')

                        if choice == 'custom':
                            # If the user enters "custom", break the loop and ask for the directory name
                            break

                        try:
                            # Try to convert the user input to an integer
                            choice = int(choice)

                            if choice < 1 or choice > len(directories):
                                # If the number is out of range, print an error message and ask again
                                print(f'{BOLD}{RED}Invalid choice! Please enter a number between 1 and {len(directories)}.{END}')
                            else:
                                # If the number is valid, break the loop and get the corresponding directory name
                                folder = directories[choice-1]
                                break
                        except ValueError:
                            # If the user input is not a valid integer, print an error message and ask again
                            print(f'{BOLD}{RED}Invalid input! Please enter a number or "custom".{END}')

                    if choice == 'custom':
                        # If the user enters "custom", ask for the directory name
                        while True:
                            print('Cooming soon!!')
                            return

                    os.system('clear')
                    print(f'{BOLD}{YELLOW}Compiling.....{END}'.center(100))
                    grab_apk = check.split('/')[-1]
                    grab_name = grab_apk.split('.apk')[0]
                    compile1 = f"java -jar {os.getcwd()}/tools/apktool_2.7.0.jar b -f --use-aapt2 -o '{os.getcwd()}/Compiled/{grab_apk}' '{os.getcwd()}/Decompiled/{folder}'"
                    os.system(compile1)
                compile_apk()
                input(f"{BOLD}{YELLOW}\nPress Enter to continue...{END}")
                
            # HII ni function ya ku signing APKS    
            elif user_choose == 4:
                def signing_apk():
                    os.system('clear')
                    print(f'{BOLD}{YELLOW}=== Apk Signing ==={END}'.center(100))
                    print('')
                    
                    compiled_dir = f'{os.getcwd()}/Compiled/'
                    apks = os.listdir(compiled_dir)
                    
                    for i, apk in enumerate(apks, start=1):
                        time.sleep(0.2)
                        print(f"{i}. {apk}")
                    print('')
                    
                    while True:
                        try:
                            apk_num = int(input(F"{BOLD}{CYAN}Enter the number of the APK you want to sign:{END} "))
                            if apk_num < 1 or apk_num > len(apks):
                                print(f"{BOLD}{RED}Invalid number. Please enter a number between 1 and {len(apks)}{END}")
                                continue
                            else:
                                apk_to_sign = apks[apk_num-1]
                                break
                        except ValueError:
                            print(f"{BOLD}{RED}Invalid input. Please enter a number.{END}")
                    
                    apk_path = os.path.join(compiled_dir, apk_to_sign)
                    os.system('clear')
                    print(f"{BOLD}{YELLOW}Selected APK: {apk_to_sign} for Signing{END}".center(100))
                    print('')
                    apk_path = os.path.join(compiled_dir, apk_to_sign)
                    time.sleep(2)
                    try:
                        cmd = f"java -jar {os.getcwd()}/tools/apksigner.jar sign  --key {os.getcwd()}/tools/apkeasytool.pk8 --cert \
                            {os.getcwd()}/tools/apkeasytool.pem --v4-signing-enabled false --out {os.getcwd()}/Compiled/{apk_to_sign} \
                                {os.getcwd()}/Compiled/{apk_to_sign}"
                        os.system(cmd)
                        print(f'{BOLD}{GREEN}Signing {apk_to_sign} was completed successful{END}')
                    except Exception as e:
                        os.system('clear')
                        print('We got Errors')
                        print(f'{BOLD}{RED}{e}{END}')
                signing_apk()
                input(f"{BOLD}{YELLOW}\nPress Enter to continue...{END}")
                
            # Deleting compiled apks   
            elif user_choose == 5:  
                           
                def clean():
                    os.system('clear')
                    print(f'{BOLD}{YELLOW}=== Cleaning Compiled Apks ==={END}'.center(100))
                    print('')
                    compiled_dir = os.path.join(os.getcwd(), 'Compiled')
                    apks = os.listdir(compiled_dir)

                    for i, apk in enumerate(apks, start=1):
                        time.sleep(0.2)
                        print(f"{i}. {apk}")
                    print('')

                    while True:
                        try:
                            apk_num = int(input(f"{BOLD}{CYAN}Enter Compiled apk you want to delete:{END} "))
                            if apk_num < 1 or apk_num > len(apks):
                                print(f"{BOLD}{RED}Invalid number. Please enter a number between 1 and {len(apks)}{END}")
                                continue
                            else:
                                apk_to_delete = apks[apk_num-1]
                                break
                        except ValueError:
                            print(f"{BOLD}{RED}Invalid input. Please enter a number.{END}")

                    apk_path = os.path.join(compiled_dir, apk_to_delete)
                    os.remove(apk_path)
                    print(f'{BOLD}{GREEN}{apk_to_delete} deleted successfully{END}')
                    print('')
                clean()
                input(f"{BOLD}{YELLOW}\nPress Enter to continue...{END}")
        except KeyboardInterrupt:
            os.system('clear')
            print('User cancelled')
            sys.exit()
        except Exception as e:
            os.system('clear')
            sys.exit(e)
    