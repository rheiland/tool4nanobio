"""
~/dev/tool4ise$ grep -r tool4ise .
./middleware/invoke:/usr/bin/invoke_app "$@" -C "start_jupyter -A -T @tool tool4ise.ipynb" -t tool4ise \
./bin/tool4ise.py:    dirname = os.path.expanduser('~/.local/share/tool4ise')
./bin/tool4ise.py:    dirname = os.path.expanduser('~/.local/share/tool4ise')
./bin/tool4ise.py:        full_path = os.path.expanduser("~/data/results/.submit_cache/tool4ise")
./bin/tool4ise.py:            full_path = os.path.join(cachedir, "tool4ise")
./bin/tool4ise.py:        os.system("submit  mail2self -s 'nanoHUB tool4ise' -t 'Your Run completed.'&")
./bin/tool4ise.py:            s.run(run_name, "-v ncn-hub_M@brown -n 8 -w 1440 tool4ise-r7 config.xml")   # "-r7" suffix??
./bin/tool4ise.py:                        cachename='tool4ise',
./bin/tool4ise.py:                            cachename='tool4ise',
./README.md:# tool4ise
./tool4ise.ipynb:    "import tool4ise"
./tool4ise.ipynb:    "tool4ise.gui"
"""
import sys
import shutil
import os
import platform


num_args = len(sys.argv)
print('num_args=',num_args)
if (num_args < 2):
#    print("Usage: %s <new tool name>")
    print("Usage: %s <your repo name>")
    sys.exit(1)
gui_name = sys.argv[1]
print('gui_name=',gui_name)


# NOTE: let's not do this now; rather edit the invoke script *on* github to avoid 
#       the (Windows) problem of making it a non-executable file
#with open('middleware/invoke', 'r') as myfile:
#    new_text = myfile.read().replace('tool4ise', gui_name)
#with open('middleware/invoke', 'w') as myfile:
#    myfile.write(new_text)

#--------------
old_file = os.path.join("bin", 'tool4ise.py')
new_file = os.path.join("bin", gui_name + '.py')
try:
    shutil.move(old_file, new_file)
    print('Renaming ',old_file, ' to ',new_file)
except:
    print("  ---> Cannot rename ",old_file," to ",new_file, ", but we will continue")

print('Replacing gui_name in ',new_file)
with open(new_file, 'r') as myfile:
    new_text = myfile.read().replace('tool4ise', gui_name)
with open(new_file, 'w') as myfile:
    myfile.write(new_text)

#--------------
old_file = 'tool4ise.ipynb'
new_file = gui_name + '.ipynb'
try:
    shutil.move(old_file, new_file)
    print('Renaming ',old_file, ' to ',new_file)
except:
    print("  ---> Cannot rename ",old_file," to ",new_file, ", but we will continue")

print('Replacing gui_name in ',new_file)
with open(new_file, 'r') as myfile:
    new_text = myfile.read().replace('tool4ise', gui_name)
with open(new_file, 'w') as myfile:
    myfile.write(new_text)


#--------------
"""
In /data:
python xml2jupyter.py PhysiCell_settings.xml
Copy the generated user_params.py to ../bin
"""
print('Trying to run xml2jupyter.py on your .xml file in /data')
os.chdir("data")
cmd = "python xml2jupyter.py PhysiCell_settings.xml"
try:
    os.system("python xml2jupyter.py PhysiCell_settings.xml")
except:
    print("  ---> Cannot execute: ",cmd)


new_file = os.path.join("..","bin")
try:
    shutil.copy("user_params.py", new_file)
except:
    print("  ---> Cannot copy data/user_params.py to bin/user_params.py")
    print("         You will need to do that manually.\n")

if platform.system() != 'Windows':
    try:
        print("Trying to import hublib.ui")
        import hublib.ui
    except:
        print("hublib.ui is not found, will try to install it.")
        os.system("pip install -U hublib")
