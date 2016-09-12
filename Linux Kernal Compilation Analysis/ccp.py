#######################################################################################
# Lav Shinde
# 2013CSB1032
#######################################################################################


#######################################################################################
#Importing libraries
#######################################################################################
import subprocess
import os
import time


#######################################################################################
#Initialization of variables
#######################################################################################

#Enter the name of the compressed file for the kernel to be combined
kernelVersionFile = raw_input("Enter filename of kernel: (Press Enter if file is linux-3.18.38.tar.xz) ")

#If default chosen for tarball name
if kernelVersionFile == "":
    kernelVersionFile = "linux-3.18.38.tar.xz"

#Get the name of the folder formed after extraction
folderName = "linux-kernel-build"

#Enter directory in which compressed kernel file is stored
filePresent = raw_input("Please copy paste tarball in same folder as this script and press enter: ")

#Identify where is the current code located
sourcePath = os.path.dirname(os.path.realpath(__file__))



#####################################################################################
#Commands for the initial setup of the file and directory structure
#####################################################################################

#Create the folder in the directory where python script is present
makeFolder = subprocess.Popen("cd " + sourcePath + "; mkdir " + folderName ,shell=True, stdout=subprocess.PIPE)
#Wait until this process makes the folder and terminates
makeFolder.wait()

#Extract the tarball in the above created folder
extractSource = subprocess.Popen("cd " + sourcePath + "; tar -xvJf " + kernelVersionFile + " -C " + folderName + " --strip-components=1",shell=True, stdout=subprocess.PIPE)
print "Extracting...."
output, err = extractSource.communicate()



######################################################################################
#Commands to move into extracted directory and build from source
#Along with logging time and % CPU and Memory Data
######################################################################################

#Setting default configurations
configFromSource = subprocess.Popen("cd " + sourcePath + "/" + folderName + "; make defconfig", shell=True, stdout=subprocess.PIPE)
print "Setting Default Configurations...."
output, err = configFromSource.communicate()

#Start top to account for memory and CPU use
checkStats = subprocess.Popen("top -b | grep -e load -e %C -e Mem -e cc > " + sourcePath + "/output.txt",shell=True, stdout=subprocess.PIPE);

#Note the start time before execution
startTime = time.time()

#Execute the compilation of the linux kernel
buildFromSource = subprocess.Popen("cd " + sourcePath + "/" + folderName + "; make", shell=True, stdout=subprocess.PIPE)
print "Compiling...."
output, err = buildFromSource.communicate()
print "Build Completed!!"

#Total time taken for execution of process
totalTime = time.time() - startTime
print "Time taken is: " + str(totalTime)



###################################################################################
#Cleaning up tasks and deleting processes
###################################################################################

#Now kill the top which had been started
topPid = subprocess.check_output(["pidof","top"])
topPid = topPid.split()
for i in topPid:
    kill = subprocess.Popen("kill -9 " + i, shell=True, stdout=subprocess.PIPE)
    output,err = kill.communicate()

#Kill all the remaining processes
checkStats.kill()