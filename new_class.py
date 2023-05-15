import sys
import os

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
    file.write("\t\t" + sys.argv[1] + "(const " + sys.argv[1]  + "& copy);\n")
    file.write("\t\t" + sys.argv[1] + "& operator=(const " + sys.argv[1] + "& copy);\n")
    file.write("};\n")
    
    file.write("\n#endif")
    
def cpp_write(file, i):
    file.write('#include "../inc/' + (sys.argv[i]) + '.hpp"\n\n')
        
    file.write(sys.argv[i] + "::" + sys.argv[i] + "() {\n")
    file.write('std::cout << "Default constructor called" << std::endl;')
    file.write("\n}\n\n")
    
    file.write(sys.argv[i] + "::~" + sys.argv[i] + "() {\n")
    file.write("\n}\n\n")
    
    file.write(sys.argv[i] + "::" + sys.argv[i] + "(const " + sys.argv[1]  + "& copy) {\n")
    file.write("\n}\n\n")
    
    file.write(sys.argv[i] + "& " + sys.argv[1] + "::operator=(const " + sys.argv[1] + "& copy) {\n")
    file.write("\n}\n\n")
        
def cpp_file(i):
    file = sys.argv[i]
    
    if (os.path.exists("src/" + file + ".cpp")):
      print('file "' + file + '.cpp" already exists')
      return
    
    try:
      file_open = open("src/" + file + ".cpp", "a")
    except OSError:
      print('Error creating "' + file_open + '"')
      return
    
    cpp_write(file_open, i)

def hpp_file(i):
    file = sys.argv[i]
    
    if (os.path.exists("inc/" + file + ".hpp")):
      print('file "' + file + '.hpp" already exists')
      return
    
    try:
      file_open = open("inc/" + file + ".hpp", "a")
    except OSError:
      print('Error creating "' + file_open + '"')
      return
    
    hpp_write(file_open, i)
  
for i in range(len(sys.argv) - 1):
    hpp_file(i + 1)
    cpp_file(i + 1)