import pwd, os;

print("""
$$$$$$$\  $$\                     $$\                  $$\           $$\   $$\                     
$$  __$$\ $$ |                    $$ |                 $$ |          $$ |  $$ |                    
$$ |  $$ |$$ | $$$$$$\   $$$$$$\  $$ |  $$\  $$$$$$\ $$$$$$\         $$ |  $$ | $$$$$$\  $$\   $$\ 
$$$$$$$\ |$$ |$$  __$$\ $$  __$$\ $$ | $$  |$$  __$$\\_$$  _|        $$$$$$$$ | \____$$\ \$$\ $$  |
$$  __$$\ $$ |$$ /  $$ |$$ /  $$ |$$$$$$  / $$$$$$$$ | $$ |          $$  __$$ | $$$$$$$ | \$$$$  / 
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$  _$$<  $$   ____| $$ |$$\       $$ |  $$ |$$  __$$ | $$  $$<  
$$$$$$$  |$$ |\$$$$$$  |\$$$$$$  |$$ | \$$\ \$$$$$$$\  \$$$$  |      $$ |  $$ |\$$$$$$$ |$$  /\$$\ 
\_______/ \__| \______/  \______/ \__|  \__| \_______|  \____/$$$$$$\\__|  \__| \_______|\__/  \__|
                                                              \______|                             
                                                                                                   
                                                                                                   """)
print("Installation client for Blooket Hacks (macOS)")
e = pwd.getpwuid(os.getuid()).pw_name
os.system("curl -o /Users/"+e+"/Desktop/Bookmarklets.html -k https://raw.githubusercontent.com/RedNotSus/Blooket-Cheats/main/obfuscated/Bookmarklets.html")
print("""If the operation was successfull, you will see an HTML file on your desktop.
Send the HTML file to google chrome via: ...:Bookmarks and Lists:Import Bookmarks and Settings...
Then Select HTML file.""")
