import sys
import os
from colorama import Fore

if (len(sys.argv) < 2):
    print("Usage: class {classes} ...")
    quit()
    
nbr_class = len(sys.argv) - 1

def hpp_write(file, i):
    file.write("#ifndef " + (sys.argv[i]).upper() + "_HPP\n")
    file.write("#define " + (sys.argv[1]).upper() + "_HPP\n")
    
    file.write("\n#include <iostream>\n\n")
    
    file.write("class " + sys.argv[i] + " {\n")
    file.write("\tprivate:\n")
    file.write("\t\t\n\tprotected:\n")
    file.write("\t\t\n\tpublic:\n")
    file.write("\t\t" + sys.argv[i] + "();\n")
    file.write("\t\t~" + sys.argv[i] + "();\n")
    file.write("\t\t" + sys.argv[i] + "(const " + sys.argv[i]  + "& copy);\n")
    file.write("\t\t" + sys.argv[i] + "& operator=(const " + sys.argv[i] + "& copy);\n")
    file.write("};\n")
    
    file.write("\n#endif")
    
def cpp_write(file, i):
    file.write('#include "../inc/' + (sys.argv[i]) + '.hpp"\n\n')
        
    file.write(sys.argv[i] + "::" + sys.argv[i] + "() {\n")
    file.write('\tstd::cout << "Default constructor called" << std::endl;')
    file.write("\n}\n\n")
    
    file.write(sys.argv[i] + "::~" + sys.argv[i] + "() {\n")
    file.write('\tstd::cout << "Default destructor called" << std::endl;')
    file.write("\n}\n\n")
    
    file.write(sys.argv[i] + "::" + sys.argv[i] + "(const " + sys.argv[i]  + "& copy) {\n")
    file.write('\tstd::cout << "Default copy constructor called" << std::endl;\n')
    file.write('\t*this = copy;')
    file.write("\n}\n\n")
    
    file.write(sys.argv[i] + "& " + sys.argv[i] + "::operator=(const " + sys.argv[i] + "& copy) {\n")
    file.write('\tstd::cout << "Default assignment operator called" << std::endl;\n')
    file.write('\t(void)copy;')
    file.write("\n}\n\n")
        
def cpp_file(i):
    file = sys.argv[i]
    
    if not (os.path.exists("src")):
      print(Fore.RED + 'Error: ' + Fore.RESET + 'folder "src" not present for class "' + file + '"')
      return
    
    if (os.path.exists("src/" + file + ".cpp")):
      print(Fore.RED + 'Error: ' + Fore.RESET + 'file "' + file + '.cpp" already exists')
      return
    
    try:
      file_open = open("src/" + file + ".cpp", "a")
    except OSError:
      print(Fore.RED + 'Error: ' + Fore.RESET + ' cannot create "' + file + '.cpp"')
      return
    
    cpp_write(file_open, i)
    
    print(Fore.GREEN + 'Success:' + Fore.RESET + '.cpp files successfully created! for class "' + file + '"')

def hpp_file(i):
    file = sys.argv[i]
    
    if not (os.path.exists("inc")):
      print(Fore.RED + 'Error: ' + Fore.RESET + 'folder "inc" not present for class "' + file + '"')
      return
    
    if (os.path.exists("inc/" + file + ".hpp")):
      print(Fore.RED + 'Error: ' + Fore.RESET + 'file "' + file + '.hpp" already exists')
      return
    
    try:
      file_open = open("inc/" + file + ".hpp", "a")
    except OSError:
      print(Fore.RED + 'Error: ' + Fore.RESET + ' cannot create "' + file + '.cpp"')
      return
    
    hpp_write(file_open, i)
    
    print(Fore.GREEN + 'Success: ' + Fore.RESET + '.hpp files successfully created for class "' + file + '"')
  
for i in range(len(sys.argv) - 1):
    hpp_file(i + 1)
    cpp_file(i + 1)