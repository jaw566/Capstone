import subprocess

result = subprocess.call(['./brake_check.sh'], shell=True)
print(result)
#print(subprocess.call(['./brake_check']))