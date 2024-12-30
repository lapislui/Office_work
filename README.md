learning about Basic Linux command  

    'ls'
to list all files and folder in directory   
mkdir - to make directory in current working folder  
cp   - to copy file from one location to other   
&nbsp; 'cp file_name location'  
mv - to move file from one location to other   
rm -to remove/delete filefom one location to other  
&nbsp; rm -r - for removing dirctory
cd - to change working directory  
touch - create new file
yum install package_name- to install any application   \
sudo su - to enter admin mode  
&nbsp; sudo command -to enter  
    exit - to exit from admin mode
    echo - to print some text in terminal   
        -n - output without new line
        -e -  all using backslashes
        \b -  removes space bet text
        \n -  prints in new line 
        \t - horizontal tab
        \v - vertical tab  
        $x- to print var in terminal  
        $((x+y))- to print add of var in terminal
          
    'sudo yum install git'  

installing git on ubuntu  

more basic commands like pwd,whoami,date etc  
  
set - to set func and others var
unset- to unset setted var
export to set env var  
  
env - to see eviourment var  
  
expr - to give expression    
  
    expr 21 + 2  
      
it prints output in terminal  
  
    expr 21+2  
      
it prints 21+2 as text on terminal  
  
    a=hello  
    expr length $a  
      
this set a and prints its length on screen  
  
    #!/bin/bash
    echo this is sample script  
      
This sets shell to interept with  
  
    nano 1.sh
    sh 1.sh

Saving shell script  and running it 

Using multiple editor like vim   
-> using multiple commands like:  
-> i - text before cursor  
-> O - text on prev line  
-> o - text on next line  
-> a - append text after cursor  
-> A - append at end of line  
  
    :wq  
      
saving and exiting vim editor  
  
    sudo useradd username  
      
creating user  
after creating user in system its foldr will be displayed in home user folder   
  
    cd ..
    ls  

       
now creating group  
  
    sudo groupadd grp1
    
