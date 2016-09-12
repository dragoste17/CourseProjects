Shinde Lav Chandrakant
2013CSB1032
=================================================================================================

Assumptions and Pre-Requisites:

1) The same directory structure obtained after decompressing the default linux-3.18.38.tar.xz is assumed to hold true even if some other file is used

2) You need to be in a folder with access to a normal user so that super user is not required (for example home, documents etc.)

3) The tarball needs to be put in the same folder which is currently has the python script

4) The decompressed version will be created in the same folder as the python script and so will the compiled product so make sure to have sufficient space on the drive

5) The code only compiles the linux kernel and not the modules. This is because it does not have much impact in the time taken or performance with the default configurations and also the question says compilation of linux kernel. Also, it neither installs the modules or the kernel itself as it requires super user access and is not mentioned in the question.

6) The build-essentials and gcc needs to be installed on the system to execute the make files of the linux kernel

=================================================================================================

How to execute:

1) After keeping the .tar.xz linux kernel file in the same folder as the script execute

                        python ccp.py

2) The script will then ask to provide name of file, by default is linux-3.18.38.tar.xz
   If your file is something else then provide that name with the extension

3) Then the script will remind you to put the .tar.xz in the same folder as that of the script.
   Once the condition is satisfied press enter

4) The extraction and compilation will now begin. It will take approximately 12 minutes to run
   The time taken will be displayed at the end along with the creation of result output files