import subprocess


proc = subprocess.run(["dir"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

print(proc)
print(proc.returncode)
print(proc.stdout.decode())