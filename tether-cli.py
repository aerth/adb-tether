#!/usr/bin/env python

# MIT LICENSE
# AUTHOR: aerth@isupon.us

from os import system
import curses, sys, traceback, os
    
def main():
    try:   
        def get_param(prompt_string):
             screen.clear()
             screen.border(0)
             screen.addstr(2, 2, prompt_string)
             screen.refresh()
             screen.addstr(1,2, "ANDROID-DEBIAN USB TETHER", curses.A_STANDOUT)
             input = screen.getstr(10, 10, 600)
             return input
        
        
        def get_params(prompt_string,second_string):
             screen.clear()
             screen.border(0)
             screen.addstr(2, 10, prompt_string)
             screen.addstr(4, 10, second_string)
             screen.refresh()
             screen.addstr(1,2, "ANDROID-DEBIAN USB TETHER", curses.A_STANDOUT)
             input = screen.getstr(10, 10, 60)
             return input
        
        
        def execute_cmd(cmd_string):
             system("reset")
             a = system( cmd_string )
             
             if a == 0:
                  print "Command executed correctly"
                  
             else:
                  print "Command terminated with error"
             raw_input("Press enter")
             #system("reset") 
        def launch_cmd(cmd_string):
             system("reset")
             a = system( cmd_string )
             print ""
             if a == 0:
                  print "Command executed correctly"
                  
             else:
                  print "Command terminated with error"
             raw_input("Press enter")
             #x = ord('q')
             #print ""
             #system("reset") 
        x = 0
        while x != ord('q'):
           
             system("reset")
             #x = screen.getch()
             screen = curses.initscr()
             screen.clear()
             screen.border(0)
             #screen.start_color()
             #curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)
             #screen.keypad(1)
             pos = 2

             #curr_y, curr_x = screen.getyx()
             #next_y, next_x = get_next_direction()
             #screen.move(next_y, next_x)
             screen.refresh()

             #x = 3
             screen.addstr(1,2, "ANDROID-DEBIAN USB TETHER V0.1", curses.A_STANDOUT)
             
             screen.addstr(2,2, "Please fork on github.com/aerth/android-debian-usb-tether", curses.A_BOLD)         
             screen.addstr(4,2, "Grab Tetherbot from http://graha.ms/androidproxy/Tetherbot.apk", curses.A_BOLD)    
             
             
                  
             screen.addstr(5, 2, "1 - Install Dependencies [using sudo apt-get]")
             screen.addstr(6, 2, "      (includes android-tools-adb android-tools-fastboot ")
             screen.addstr(7,2, "       android-tools-utils gvfs-backends jmtpfs and git)")

             
             screen.addstr(8, 2, "2 - USB ADB START")
             screen.addstr(9, 2, "3 - USB ADB STATUS")
             screen.addstr(10, 2, "4 - KILL ADB SRV")
             screen.addstr(11, 2, "5 - Connected Androids")             
             screen.addstr(12, 2, "6 - Connect Android via adb")
             screen.addstr(13, 2, "7 - ENABLE USB TETHER (port 1080 SOCKS)")             

             screen.addstr(14, 2, "8 - ENABLE SSH PROXY")
             screen.addstr(15, 2, "9 - SSH to Server")
             screen.addstr(16, 2, "0 - SSH to Server (with id_rsa)")
             screen.addstr(17, 2, "a - SCP Push (with id_rsa)")
             screen.addstr(18, 2, "b - SCP Get (with id_rsa)")
             screen.addstr(20, 2, "Thanks for using Free / Libre Open Source Software!", curses.A_BOLD)
             
             
             
             screen.keypad(1)
             screen.addstr(3, 50, "Press q or CTRL + C to Exit")
             s = curses.newwin(1, 15, 2, 8)
             s.box()
             #screen.refresh()
        
             x = screen.getch()
             
             if x == ord('1'):
                  confirm = get_params("Downloading and installing dependencies!","Are you sure? Installing PHP, Apache2, \n        php-gd , composer, enabling a2mod rewrite \n        type yes")
                  curses.endwin()
                  if confirm == "yes":
                       execute_cmd("sudo apt-get install android-tools-adb android-tools-fastboot android-tools-utils gvfs-backends jmtpfs git")                   

             if x == ord('2'):
                  curses.endwin()
                  execute_cmd("adb start-server")
                  execute_cmd("echo Now connect your android via USB. Make sure its in debugging mode. Run command #5 to see if it is properly connected.")
             if x == ord('3'):
                  curses.endwin()
                  execute_cmd("adb get-state")  
             if x == ord('4'):
                  iface = get_param("are you sure? stopping adb server!")
                  curses.endwin()
                  if confirm == "yes":
                        execute_cmd("adb kill-server")      
             if x == ord('5'):
                  curses.endwin()
                  execute_cmd("adb devices -l")  
             if x == ord('6'):
                  curses.endwin()
                  execute_cmd("adb shell su")
             if x == ord('7'):
                  user = get_param("At this point you must pick up your phone open Tetherbot app and Start Socks.")
                  curses.endwin()
                  execute_cmd("adb forward tcp:1080 tcp:1080")      
             if x == ord('8'):
                  user = get_param("At this point you must pick up your phone open Tetherbot app and Start Tunnel to your favorite server.")
                  curses.endwin()
                
                  execute_cmd("adb forward tcp:4444 localabstract:Tunnel")
             if x == ord('9'):
                  curses.endwin()
                  user = get_param("What username to ssh?")
                  execute_cmd("ssh -p 4444 " + user + "@localhost")
             if x == ord('0'):
                  user = get_param("What username to ssh?")
                  curses.endwin()
                  execute_cmd("ssh -p 4444 " + user + "@localhost -v -i ~/.ssh/id_rsa")          
             if x == ord('a'):
                  user = get_param("What username to ssh?")
                  files = get_param("What files to push?")
                  curses.endwin()
                  execute_cmd("scp -v -i ~/.ssh/id_rsa -P 4444 " + files + " " + user + "@localhost:~/ ")          

             if x == ord('b'):
                  user = get_param("What username to ssh?")
                  files = get_param("What files to get?")
                  curses.endwin()
                  execute_cmd("scp -v -i ~/.ssh/id_rsa -P 4444 " + user + "@localhost:~/" + files + " . ")          


        curses.endwin()
    except KeyboardInterrupt:
        print "\n Have a Grateful Day! :D \n"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    os.system('reset')
   

if __name__ == "__main__":
    main()

