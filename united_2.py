#!/bin/python
#Made by - Kieran Docherty- 2017
#This is the base for any tkinter programs i write
#Can use console and Gui at same time
import random
import tkinter as tk #Import is required i name it tk for ease of use
import time # \/
#Not required but here bc I often use them
import pygame
import random
import sys
import time
import pdb
 
"""
x = 0,200 and
y 0, 200
1 in 2 chance that you will battle anywhere else no battles
"""
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
ORANGE = (255, 0, 255)
GREEN = (127, 255, 0)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

LARGE_FONT = ("Verdana", 12)



#All stats for all pokemon are going to be definded up here and then put into global and this is going to be the only
#time we use global, I also think we can make pokemon (The ones you have an array but we will need to disscuss that):

#pok_(x) = [attack, defense, speed, health, weakness] each of these can go as high as we like, health should always be the highest.
#/\Need stat for weakness

#Also need to find out how to increase the number in stats but ik have that code on my Dungeon crawler game
#parts.

#All starting pokemon have similar stats but for example Char has highest attck but health is same as Squit.

#Anything we need to say about the code try to put here or "#" next to them.

#Every varible must be definded as 0 up here and globaled or definded as " "


global Char_stats, Squit_stats, Duld_stats, f_pok, fpokstats, duld, char, squirt, damage_taken, defence_gained
global damage_given,defense_earned, level, pokemon, own_poke
#global all pokemon stats might be able to put all pokemon in on array?
level = 5
Char_specail = {'Name' : 'Ember', 'Attack' : 25,'AP' : 25, 'Weak' : 5, 'APMax' : 25}
Char_stats = {'Name': 'Charzard', 'Attack' : 17.5, 'Defense' : 2.5, 'Health' : 35,'Type' : "Fire", 
              'Specail' : Char_specail , 'Exp' : 0, 'MaxHealth' : 35, 'Level' : 10, 'Req' : 20, 'Pic' : """
                                                                                                    
                                                                                                    
                                 `.--.`                                                             
                            `:+ossoooosss+/`                                                        
                         ./os++++++++++++++so:                                                      
                       .ss+++++++++++++++++++os/                                                    
                      .hh++++++++++++++++++++++os`                                                  
                     .s+d+++++++++++++++oyyo+++++y.                                                 
                    `hsNs+++++++++++++++ysydho++++y`                                                
                    oMMm++++++++++++++++y+`sMNs+++s+                                                
                   -MMNo+++++++++++++++ss .mMMNo+++h                                                
                  -ymds++++++++++++++++N+/dMMMMs+++d.                                               
                .ss+++++++++++++++++++yMMMMMMNMs+++h-                                               
               /y+++++++++++++++++++++dNNMMNmdNo+++y:                                               
              /y++++++++++++++++++++++shddhhdmh++++y:                                               
             `h++++++++++++++++++++++++++oooo++++++h-                                   `.          
              yo++++o++++++++++++++++++++++++++++++d`                                  `+.          
              .yo+++so++++oo+++++++++++++++++++o+++d`                                  /yo`         
               `hhso++++++o++++++++++++++++oosys+++d.                              ..`:syy-   `     
          //-.  `yhmhysooo+++ooossssyyhdhhhddy+++++h-            `...             :sssyyyyo`./-     
         `d++oo+:-ohhddysyyyyyyyyyyyyhmhhhhsoys++++s+       .-:/osooh`           .yyyyyyyyyssy:     
        `/hoyo++ooshdhdy+/////////++sdhhsosyyo+++++oh--:/+oooosyyysyo            `ssyyyy+yyyyy/     
       `ys+hso+++++++syyyysssssssyyssssshhyo+++++++ooooo+++++++++hyyso-           .:osyo:yyyyyo     
        `/sooo+++++++++osyhysssssssso+//+oyo+++++++++++++++++++++oooss-             .-+-+yyyyyy..   
          `+s++++++++++++oh:////::::::--..-oy+++++++++++++++++++++so-               ..-.oyyyyyys/   
            .+s++++++++++h:.-:::::::-......./yo+++++++++++++++++os/`              `...../yooyyyy/   
              .oso++++++ss.....---...........-yo++++++++++++++os+.                `.....-o--syyy.   
                -oyyssssd-....................-so++++ossyyysso:`                  `......-..-ss-    
                  .+yyyyy.......................yo++++sssyy.`                     `..........s/     
                    `-/h/.......................-yo+++++++y/                       `........-s.     
                       s-........................-h++++++++h.                        `..://o+-      
                       s-.........................+y+++++++oy                           so+h`       
                       ++..........................h++++++++y/                         `d++h        
                       -s..........................os++++++++h`                        os++y        
                        h........................../h++++++++so                       /y++oo        
                        y:.........................-d+++++++++h`                    `+s++/h:        
                        :s..........................d+++++++++s+                   .ss++++h`        
                         y:........................-d++++++++++h                `.+s+++++d/         
                       `/sh-......................./y++++++++++m+:.`      ```.-+os++++++hy          
                     `/so+oh:......................yo++ysssyysom+osooooooooosso++++++++dh`          
                    -so+++++yo-...................-h+++++++++ohd+++++++++++++++++++++sdy`           
                   :y++++++++oso:-................yo+++++++++++d+++++++++++++++++++oyh+             
                   h+++++++++++oyy+:---.......--:ys++++++++++++hs++++++++++++++++osso-              
                  `d++++++++++osssyyso/::::::::+ho+++++++++++++hs++++++++++++oso++o:                
                   os+++++++++ossssssyds+oo+++sho++++++++++++++d+ssssssssso++/-/+:                  
                    /yo+++++++ssssssyh/    `.-hs++++++++++++++od/:--------:/+//.                    
                 `.:+sdmhsooosssssshh.        .h+++++++++++++oy--://////::-`                        
             `-+osso+++oyhysssssssshh-         /y++osssssssydo`                                     
           -o++yyso+++++++++ossssssssd.       `h+++++oossoosss`                                     
           +oy/.-+hoy++++oosssssssyyhs`       -h+oo++oo+++sssso                                     
            .//+ho++yyssssoooo++//:-`         `hh+:ohy-+yh-`dh/                                     
                                               `o+-.hh:+yh-++`                                      
                                                  -:: -. .-`     
"""}

Squit_specail = {'Name' : 'Water Gun', 'AP' : 25,'Attack' : 20,'Weak' : 5, 'APMax' : 25}
Squit_stats = {'Name': 'Squirtale', 'Attack' : 15, 'Defense' : 5.25, 'Health' : 32.5,'Type' : "Water",
               'Specail' :Squit_specail, 'Exp' : 0, 'MaxHealth' : 32.5, 'Level' : 10, 'Req' : 20, 'Pic' : """
                                `..-----::-----..                                                   
                            ..-:--....-----------::-.                                               
                         `-:-..`....----------------::-`                                            
                       .---......-----------:---------:::.                                          
                     `-:::----------------:/:-----------:::`                                        
                     -:/:------------------:/-.-s+--------::.                                       
                    `/`/------------------om-   -y/---------/.                                      
                   `+o::-----------------omNd/:/hh:----------/`                                     
                   /+my-----------------:mNMMNNmmy-----------:/                                     
                   o+m/-----------------oNNMMMmoo+------------/`                                    
                  `o+o------------------shsmNdo+o.:-----------:-                                    
                 .:/+:------------------+++oo//o:`:-----------:-                                    
                `:-::----:---------------:://///.-------------/.                                    
                `/::-----:--::::------------------------------/                                     
                 :::/::::://::::://////:::::::::::::/--------::                                     
                  ::-::::::------------:::::::::::::--------:/`                                     
                   -::-------------------------------------:+.                                      
                    `-::----------------------------------:/:-                                      
                      `-::-----------------------------::/:./+:.                                    
                       `-//:::----------------------::///:-.+o++:`                                  
                  `.---::::////:::::------------:::////////-+ooo++-                                 
              `.--:------:-.::://///////////////+::---::::::+sooo++:                                
          `--::--------::````.-:::::::::::::::+:-..-----:::::/sosso+/                               
       `-::-----------::```````.-:::::::::::/+:-...------:::::/oooss+/                              
 `-----:-------------:...-.```````.--::::::/+--...-------::::::oooooso-                             
 -:-::-::-----------:.`````.......````...--+-------------::::::+sooo++s.                            
  -:::+:-----------:.````````````.-:----../:-------------::::::/ooo++++o                            
 .:::://::---------:``````````````-.`````./---:/:-------::::::/./oo++++o.                           
::-:::::::::::::::/-``````````````:``````/---//:+------::::::/:./oo+++++:                           
.-----:::::::::::::-.`````````````:`````./--::::::----::::::/:-.+oo+++++/                           
                  -`:`````````````:````-:--::::::-::://+::+::-..soo+++++/                           
                  -`.:```````````--```-/::::::::::::::/+//+---./oooo++++/                           
                  :``--``````````:.```...--:::::::::////://--..soooo++++/                           
                  -``.:.........`:``````````...-:-///::::+:--..yssoooo+s-         `..-----..`       
                  ..`:````......-/----.........:..:::::::/+--..ysssoooss`     `.-:::::::::::::-.    
                  ./:.```````````:`````.........::::::::::+---.ossssyss+    .::::::::::::::::::::.  
                `--::````````````:`````````````.:+/:://///+/::-/ssyysss.   -:::::::::::::::::::::/- 
               `----:.```````````:```````````.-:::++::::::::://-osssss/  .::::::::::::::::::::::::/.
              .:-----/.``````````:````````..-::://:------------:/sssso``-::::::::::::::::::::::::::/
             `:-------/:-.....```:``....--::::://:--------------:osso..:::::::::::://::::://:::::::/
             :---------://::::::://::::::::::://-----------------:so-:::::::::::://::::::::::::::::+
            .:----------:///////////+///::::://-------------------+/:::::::::::::+:::::::::::::::::/
            :----------::::++/:::::::////////+--------------------:+:::::::::::::+::::::::::::::::/`
            :--------::::::::////:::::::::///+:--------------------+:::::::::::::+:::::::::::::::/- 
            ::::-::::::::::::::/.-:::::::::///+:------------------:+::::::::::::::+/::::::::::::/.  
           `::::::::::::::::::-     ```....-:::::----------------::+:::::::::::::::///:::::::::-`   
         `:/:/::::::::::::::::                  -:------------:::::+:::::::::::::::::://////-.      
         ..:+:::/::::::::::::`                   ::::-----::::::::::  `...---:::::::::--..`         
           /::-:+::::/:-..`                      .::::::::::::::::::                                
               -/:-..                             /::::::::::::::::/                                
                                                  :::::::::::::::::/-                               
                                                  -::----/::::/---:::                               
                                                          .---     
"""}

Duld_specail = {'Name' : 'Leaves', 'AP' : 25, 'Attack' : 20, 'Weak' : 5, 'APMax' : 25}
Duld_stats = {'Name': 'Duldasuar', 'Attack' : 13, 'Defense' : 3.5, 'Health' : 47.5,'Type' : "Grass",
              'Specail' : Duld_specail, 'Exp' : 0, 'MaxHealth' : 35, 'Level' : 10, 'Req' : 20,'Pic' : """

                    y                                                                               
            NsshN h//oN                                                                             
             h+//y+////yN                                                                           
         hsyydo///oo/////oyhd NNNN                                                                  
          soosy+///++++////////////////////////++osydN                                              
          Nooodo/////::///////////////////////////::::+sdN                                          
           yoohs//////::::::::::://+++++//////////////:::/s                                         
           soosy////////::::::::::::::::++++////////////::::+d                                      
           ooosy//////////:::::::::::::::::/o/////////////::::s                                     
         Nsooohs//////////////:::::::::::o++oo+++///////////:::y              Ndyso+/:oN            
        Nsooooho////////////////////////y/:::::::/+++++oooooooooooo+++++oossys+//:::::-:d           
       Nsoooohs+///////////////////////s+::::::::::::/+////::::::::::--------::://:::::-:d          
      Nsoooosyo+///////////////////////y::::::::::::::::::::::+o++++/:::::::::::::::::::-:N         
      soooosyoo///////////////////////y/::::::::::::::::::::::yhyyyyyyyso+/:::::::::::::::o         
     oooooohoo+//////////////////////+y::::::::::::::::::::::::+yhyyyyyyyyyyso+:::::::::://         
    ooooooyooo///////////////////++ooyo::::::::::::::::::::::::::+syyyyyyyyyyyy+:::::::::::sN       
  Noooooossooo/////////////////+oooooh:::::::::::::::::::::::::::::/oyyyyyyyys/:::::::::::::+       
  sooooooyoooo///////////////+oooooosy::::::::::::::::::::::::::::::::/osyso/::::oo+:::::::/:/d     
 doooooooyoooo+/////////////oooooossoo::::::::::::/+++/:::::::/::::::::::::::::::yyh+:/:::+.://h    
 sooooooosooooo+//////////+oooooss+:s:::::::::::/syhdd:-//::::++:::::::::::::::::+yy/:+/:/y+``//h   
 ooooooooooooooo+////////+ooooss+:::s::::::::::+yssshdh.`-+::::++::::::oyyo/::::::/:::+/:osss``+/   
dooooooooooooooooo++/+++ooosys/:::::o:::::::::+yss--syys  `+/:::+::::::syyyyo/::::::::/::o/ss/ `++  
dooooooooooooooooooooooooshhhyso/::/+:::::::::yss/  /ssy`  `+::::::::::+hyyyhs:::::::::::+ oss  //h 
dooooooooooossoooooooosyhhyyyyyh/::+:::::::::+yss-  :ssy-   `+:::::::::/hyyyo/:::::::::::+ /sy  `o+ 
Nooooooooooooosssossyhhhyyyyyyh+:::/:::::::::ssss/  +ssy.    //:::::::::o+/::::::::::::::+`+ss   o: 
 soooooooooooooosydhhyyyyyyyyho::::::::::::::yssss++sssh`    `o::::::::::::::::::::::::::o+ss/ `-+:h
 Nsooooooooooossoshyyyyyyyyyh+:::::::::::::::+ssssssssss      o::::::::::::::::::::::::::+ssy-://::y
  Nhoooooooosyo::yyyyyyyyyyy+::::::::::::::::://+oossss+-----:/:::::::::::::::::::::::::::///::::/:y
     ysooooyo::::oyyyyyyyss/:::::::::::::::::/::::::::::::::::::::::::::::::::::::::::/::::::::///o 
     N yyyy/:::::::://:::::::::::::::::::::::://////::::::::::::::::::::::::::/:::::::/::://////+h  
         y::::::::::::::::::::::::::::::/:::::::::/+/-+oo++////////:::::::::::///////oosy++/:/od    
        y:::::::::::::::::::::::::::::::///::::::::://sssssysssssssooooooosssssssssyyhhs+:/+y       
       h::::::::::::://:::+:::::::::::::::////:::::::::/+ssoo++++++++++++++++++++ooso+:/+y          
      N/:::::::oso+/::+so+s:::::::::::::::::/+o+/::::::::://++o++++++////+++++o+++//+o+h            
      s:::::::/hyyhys+:/ssy::::::::::::/::::::/osoo+///::::::::////+++++++++++/+oo++/--d            
      /:::::::oyyyyyyhy+:sh:::::::::::syyo:::::+syooosoooooo++++++++++oooosso++/::::---N            
     N::::::::yyyyyyyyyh::h:::::::::::dyyh+:::::+yoooooooooooooooooooooooooo+/ssso/:--/             
      ::::::::yyyyyyyyy+:+ss::::::::::sys/:oss+/:osoooooooooooooooooossooooo/ohyyyyo:-y             
      ::::::::yyyyyyys/:/ooy+::::::::::::::syyyys+yoooooooooooooosyssooooooo:hyyyysos+N             
      +:::::::/oyyys/::/oooo +:::::::::::::+hyyyysyhooooooosyhdNhoooooooooo+:yyyyyoood              
      y+/:::::::::::::/ooooohyo:::::::::::::yyyyysohysssss      Nsooooooooo+:/shyyooy               
      Noo+/::::::::::/oooooydh s::::::::::::/hyyysoshooood       Nsoooooooo+:::+o+/s                
        oooo+//////++oooooo     d/:::::::::::+yyyysshsyoN          yoooooooo/:::::+N                
         oooooooooooooooos       Ny::::::::::::/+++:s                sooooso/://+o/                 
         Nhooo+sooo:sos:+          Ns/::::::::::::::s                  ys+`/o++` ++                 
             +-h  s+d   d            Nho/+:+://.-+o/`+                    hy    Nd                  
                                          +oNNo::d                                       """}

Osh_stats = {'Name': 'Oshiwish', 'Attack' : 20, 'Defense' : 6.5, 'Health' : 40,'Type' : "Water",
              'Exp' : 0, 'MaxHealth' : 40, 'Level' : level, 'Req' : 10,'Specail' :25, 'Pic' : """
                              so++/   /+oss                                          
                         hs+/-.````   `````. o dN                                     
                    Nho-```                   ``-+hN                                  
            N dhhhho.`                            `.+d                                
          N oooss/`                         ``````````/                               
          hooss/`             ```` ```````````````````o hhd N                         
           ss+.            ``````````````````````````` ssssss  N                      
         N  /        `````````````````````````````````osssssooosN                     
         N /`  `````````````````````````````````````` - sssssoood                     
          o`````````````````````````````````        ```sssssssssN                     
         d`````` //-````````````````` `       ``````` `.sssssssd                      
          ````- h/-s/````````````      ``````. /-.      - sss hN                      
        N`````hd ``od`````./++++++/ .```````+ho +h/`     .s   N                       
          ```- dd  d .``-oo+++++ooooo+ `   odd. ` d.      ` /-                        
        d `  .ddddddd``. o+++++++ooooos/  `ddd osdd+        `                         
        N`    +ddhdd/  .hsooooooooooosso  `dddddddd+      `.-s                        
         o.`   -oso-     ssssssssssssso`   +ddhhdd `  ```.- /                         
         N/-.`.`   .     ` +osssssss+-     ` o h +````.-- //s                         
           + --.`` `         `.--.```````````````-..-   ///+N                         
            o    +--....````.-----````````.. --- +  //// /+                           
            Nh/    //    /++ -----///--        +        /sN                           
              N +////////////////////+/       /+o++/   +d                             
             Ns+sso+oooooos+          /++/  /osoooosoodN                              
             d+oooosoooooooos /    /osoooooohoooooooo+                                
             Nsooooooooooooooo      ooooooooooooooo++/                                
              Nhsssoooooooooo ssooo oooooooooso+oo+/ /                                
      N dhso/-.`. o+++++ooooooooooosooooso/ .`    ` o                                 
 Ns/-.```       `+/   /////++++++++++os+.`          -                                 
                 /             /////o `           `- h                                
 Ns.            /      //o//     /+s-          ``. /sN                                
    hs/ -.````-+     ++   ``````.-+o      ``..- /+ohN                                 
      NNN  ddhs    /o .`+```````././--   ///++++++/+N                                 
              /    s..`.+```````/.....-o/////           NN  dddd NN                   
                   o-..-/.......+......-+          /hNN dhh        d N                
             h      //--+.......+....../+       ///+hdhhhhhhh        hN               
             d////   /// /......+--  /+/    ////++oo hhhhhhhhhh                       
             No+++++////o-...... oo+///////++++ooooohhhhhhhhhhhh  hh N                
              hooooooo++o+/      /s++++++oooooooooosdhhhhhhhhdd  NN                   
              Nhoooooooooooossosssooooooooooooooooodhhdd  NNNN                        
                dsooooooooooooooooooooooooooooooos NNN                                
                 NdsooooooooooooooooooooooooooosdN                                    
                  NNdh soooooooooooooooooooos h NN                                    
                N dhhhhhhhhdh  ssssssss    hhhhhhdNN                                  
              N h hh  h  hd              dhhhh     hN                                 
             N ssh ss  s hN              N   h ss  sshN                               
                d ssh s hN                dsoo  ssshssh                               
                     s                     soo+o+++oss   
"""}

Odd_stats = {'Name': 'Oddush', 'Attack' : 16, 'Defense' : 5, 'Health' : 50,'Type' : "Grass",
              'Exp' : 0, 'MaxHealth' : 50, 'Level' : level, 'Req' : 10,'Specail' : 25, 'Pic' : """
 `.``                                                                                  
  .:////:-.                                                                            
    ./++++/:`                     ```..--                                              
     `:++o+//.              `..-:///++++.                                              
       //+o+//-          `-://+/++++++/.         ``..--:://////-                       
       -+//++/+:`      `:/+///++++//+-`    `.-::////+++++++////+.                      
       `+///++/+/.   `://///+++///+/.``.-///++/++++++++///+/++/+.                      
        +///+osoo+- `/+++oooo+///++:://+///+++++++//////+/-`-+/+                       
        +//+ssyysss/oossssysso++o++++++++++++/////////+/.    +/:                       
       `+//ssssyssssyssssysssssssssssssss+//////////+/.      :+`                       
       .+/+sssssyssssyssyssyssssssssssssss+///////++:`````   `-                        
       .+/+ssssssysssysyssyssssssyssssssss+//////+o+///////::--.``                     
        /+ossssssysssyysysssssssssssssssss+////+ossss++++++++++++/:.`                  
        `/+sssssssysssyysssssyssssssssssso////+ssssyyso++++++++++++++/-`               
          -ossssssysssyssssysssssssssssso+//+oyssooooo++++++++/+////:::/:`             
            -osssssysysssyssssssssssssso+++ossoo++//////////+++/-`                     
             `:osssyyssysssssssssssssssoossssssssso+++++++++//+++//:`                  
        `-:/+ooooooooossssssssssssysyyyssssssssssss///+++++++++++++++:`                
     `:+oooooooooooooooooossssyysssssssssssssssssso//////////////++++/+.               
   `/oooooooooooooooooooooooossssssssssssssssssss+///////////+/-.`  `.-/`              
  :oooooooo:soooooooooooooooooyyyoosssssssssssso+////////+/-.                          
 /oooooooooooooooooooooooooooosyys` .-/+ossoo+///////+/:.`                             
-oooooooooooosysooooooo-oooooooyyys       `.---::::-.`                                 
/oooooooooooosssssoooooooooooooyyyy/                                                   
:ooooooooooooo/+ssoooooooooooosyyyyy                                                   
`ooooooooooooo++ooooooooooooooyyyyyy.                                                  
 -ooooooooooooooooooooooooooosyyyyyy.                                                  
  .syyyyssoooooooooooooooooosyyyyyys                                                   
   `/yyyyyyyysssooooooooossyyyyyyyy:                                                   
     `/syyyyyyyyyyyyyyyyyyyyyyyyyy:                                                    
       `-yyyyyyyyyyyyyyyyyyyyyyy+.                                                     
       -syhyhhyyyyyyyyyyyyyys+:.                                                       
      -yyyyyyyyy.-:/yhhhyhy-`                                                          
     `oossyyyyyy   /yyyyyyyo                                                           
     :oooooyyyy+  .yyyyyyyyy`                                                          
     /ooooooyys`  :ossyyyyyy`                                                          
     :ooooooyo`   /oooosyyyy                                                           
     `+oooo+:`    /ooooooyy/                                                           
       .--.`      .ooooooso                                                            
                   -+++++:                                                             
                     ...   
"""}

Tor_stats = {'Name': 'Torchick', 'Attack' : 15.5, 'Defense' : 3, 'Health' : 30,'Type' : "Fire",
              'Exp' : 0, 'MaxHealth' : 30, 'Level' : level, 'Req' : 10, 'Specail' :'Ember', 'Pic' : """
                                         s+:          
										  
                                      Nh+-..                               
                                     o-.....                               
                                   o-......-                               
                                Ns-........+                               
                               d/-........-y                               
                       s-h    y:---..-...-:N                               
                       --:   o------------h     Ndhyoy                     
                      s---/Ny------------+   ds/--..:                      
                      /----s---://-------hy/:......+                       
                      +---:+-:+:-o-------:-....../h                        
                      y-----/+::o:-------------/yN                         
                NN   dd+:::/+::/y//+-------:/odN                           
           N hs+//:-----://+////++o/--::/oh N                              
       N y+/-------------:://////+o+shdN                                   
     Nh+:----------------:://///////+s                                     
   Ny/:---------------::::///////////:/o                                   
   +:::-------::::::::::///////////////:/h                                 
  ///::--::::::::://////////////////////::                                 
N/+//:::::/::::////////////////////////////y                               
y s///:::::::::///////s+:os/////////////////                               
 h /////++/:::::////+ h` ` d////////////////s                              
 ss///:...:+/:::/:::o  dyh  ////////////////s                              
 s/+-.------://+/////yN soyy////////////////                               
 N+/+//////:////+//////ooo+////////////////y                               
   h/:////:://///////////////////////////+h                                
    Nh+/://////////////////////////////+yN                                 
       Nhs+/:///////////////////////+shN                                   
       ho/-:/:://////://///////+++sdN                                      
    d+-...----::///::-:::::::------:/sd                                    
     /--...--::////:-----------------+                                     
     dd:----+////////.....------------+                                    
      dss/:o////////+-..-.---------:/+oyN                                  
        h/o//////////o-oo:--:----o//ss                                     
         +::://///////o+/+++++//:s+++/+                                    
         N+::://///////////o///+o+///od                                    
          Nh+::///////////////////+odN                                     
            Ndo+/::///////////++sdN                                        
               N hyo//+++++oos++yN N                                       
                   h/+NN+/o::++/:/:                                        
           N dd    :./  s/s:::/yhhN                                        
         s/-....--....+osyd yyd                                            
        -..:os:-...:-..-:::s                                               
       y--h  o`..+s...+dNN d                                               
        hd   /..h s..:                                                     
             Noo  N/-s                                                     
                     +s  
"""}

Cyn_specail = ['Ember', 20, 25, 5]
Cyn_stats = {'Name': 'cyndaquil ', 'Attack' : 16.5, 'Defense' : 2, 'Health' : 32,'Type' : "Fire",
              'Exp' : 0, 'MaxHealth' : 32, 'Level' : level, 'Req' : 10, 'Specail' :Cyn_specail, 'Pic' :"""                                                                                                   
                                           :.                                                       
                                           //.                                                      
                                           ///-                                                     
                                          `////-     .`        `......``                            
                                     .:`  `/////-   .+:   `-:/oooooossssso/-`                       
                                     `/:. `//////-  /++.-+ossooooooooossyyhys/-                     
                                     `///-.//////+..o+osssoooooooooooossyyyyyyyo-`                  
                                      :///+///////++oyyysoooosoooooooosyyyyyyyyyy+`                 
                           `:.      ``-///////:///+ohyo/:--..--:/+osssyyyyyyyyyyyys.                
                            :+:.`   :/://////:-:/+oho-............-:oyyyyyyyyyyyyyyy.               
``` ``                      `/++/.`.-+++//+//:-:++yo................./shyyyyyyyyyyyys               
.-::/::--.```             `:-:o+++/-oo++++++:---++y-..................-shyyyyyyyyyhyh:              
  `.:///////::-.``    `:.``.++++++++o++++/+/----//o........-/+/::-......shyyyyyyyyyyhs`             
     `-://////////::--.-o+/::o+++++++++++/::-----:+.......-+-....-:/....-shyyyyyyyyyhho-`           
        .://////////++++o+++++++++++//+++/--------+......./-.......-+:...-syhyyyyyyyyyyhyo:`        
          `.:///////++++++++++++++///--:/:--------/:......--.........//...-yyyyyyhyyyyyhyyhy+.      
          ````.://////++//////:-:::::---------:---+s................../:...:syyyyyyyyyyyyyyyyyo.    
          .:+++/+o++++++++/::::-.-..--..------:/:+yhs-.................-.......--::/+osyhyyyssss/`  
            `-:+++++++++++++/:--------------//:syyyyhy/.................................:+ossoooos- 
               `.:++++++++//::-------------+oyssyyyyhhyo:...................................-/+ssoy.
               .::/+o++++++/:------------/ssyyyyyyyo/-.-:/::--.........---::/::::::::::--.......::-o
                `.-:/++++++++/---::---::+ooossyyyo-.....-://////+++++//::-.`          ``----:--..:.+
                ``.-:+o+++++/::--::-/osooooosssy/.....::-.--::::::-.:.                       `.-/:-`
         ``..-:///++++++///:-----:/osssoooossyy/........::......-:...:.                             
     `.-:///////////+++++++++//:/+ooysooossyyy/.:........-/.....-:..../                             
     .----:::///++++++++++++++//+yyyyyyssyyy+-..-/-.......-/..../-..../                             
            `````..-:+o++++++//:syyso++++/:-....../:-.....-o....:-.../-                             
                   -:/+o+++++++sy/-........--......-:///:/+/....-o://-                              
                   `.:++++++++os-............:........---:-......:ss.                               
                 .://///:::---+-.................................:o//.                              
                 `````        /................:...............-:/+///`                             
                              :/-............../...........---::/+///+.                             
                              .o::----.........+-....---::::////////++`                             
                               /////:::::--:::/s:::://////+++++++++o+.                              
                               `+///////////+os++++++++ooosoooooooo:`                               
                                .+////////+oo+++////::-sooooooooos.                                 
                                 .+///////o.```        `/+oooooooo+-                                
                                  -+//////+o`             .--:///::.                                
                                   .:/o/:///`                                                       
"""}
Mud_specail = ['Water Gun', 25, 20, 5]
Mud_stats = {'Name': 'Mukdip', 'Attack' : 21, 'Defense' : 8.5, 'Health' : 38,'Type' : "Water",
               'Specail' :Mud_specail, 'Exp' : 0, 'MaxHealth' : 38, 'Level' : 10, 'Req' : 20, 'Pic' : '''                                                                     

                                     .ohysssdsssssssyy                                              
                                   .shssssssdssssssssm                                              
                                 .shsssssssshysssssssm-                                             
                                /dyhssssssssyhsssssssd:                                             
                              `yhsshssssssssyhsssssssd/                                             
                             .hyssshssssssssyhsssssyyd:                                             
                            .dyssssyysssssssyhssssyyym-                                             
                           `hysssssshssssssshysssyyyyN`                                             
                           shsssssssdssssssshsssyyyyym                                              
                          .mssssssssdsssssssdsssyyyyhh                                              
                          ohssssssssdsssssssdssyyyyyhs                                              
                          hyssssssssdssssssshsyyyyyyd:                                              
                          dyssssssssdssssssshsyyyyyym`                                              
                          dysssssssshssssssshyyyyyyhh                                               
                          hhsssssssshssssssyyyyyyyyho                                               
                          odsssssssshssssssyyyyyyyym.                                               
                          :Nssssssssysssssssyyyyyyhd                                                
                          `Nssssssssysssssssyyyyyyh+                                                
                           yhsssssssssssssssyyyyyyd`                                                
                           :msssssssssssssssyyyyyho                                                 
                            dsssssssssssssssyyyyhd`                                                 
                            /dsssssssssssssshhhhd:                                        ``.---.`  
                          `-/msssssssssssssssssyyso+:.`                              ``:+ooo+///+s+ 
                       ./osssyhssssssssssssssssssssssyyo:`                        `:ooo/----------++
                    `+syssssssdsssssssssssssssssssssssssyhs-                   .+oo/---------------h
                  .ohs+//+ossssyssssssssssssssssssssssssssshy:              .+oo:------------------d
                 ods+:::::+ssssysssssssssssssssssssssssssssssyh-         .+o+----------------------d
               -dyo/:::::/ossssssssssssssssssssssssssssssssssssho      :++---------------------:/++h
              :mss/::::/osssssssssssssssssssssssssssssssssssssssyy` `/o:------------------:+ssso/-s/
             :dssso///ossssssssssssssssssssssssssssssssssssssssyyyy++----/+ooo++-----:+ssso/------d`
            `dssssssssssssssssssssssssssssssssssssssssssssssyys+++os:osyyso+++sM:/+ooo/:---------s+ 
            syyssssssssssh+hssssssssssssssssyy-oysssssssssyho+++++oyso+++++++odh+/:----::::::::-:h  
  +yyyso/-``y++yssssssssd+ yysssssssssssssssm: :Nsssssssshy+++++++++++++++++oyh--::://///+++++/:h-  
  y++++++ooyo+++ysssssssNy/NhsssssssssssssssNdsmMssssssshs+++++++++++++++ossyy////+++++++++++++y/   
  :y+++++++y+++++hssssssmMMMysssssssssssssssmMMMNssssssdo+++++++++++++++++++osso++++++++++++++os    
   ss+++++++++++++hssssshMMmssssssssssssssssyMMMhssssshs+++++++++++++++++++++++sys+++++++++++oy`    
   `y+++++++++++++ohysssssysssssssssssssssssssyysssssyh++++++++++++++++++++++++++sh++++++++++y`     
  -o+++++++++++++++hdhhhhhhyyysssssyyyyyyyyyyyyyyyyyydo++++++++++++++++++oooooooosho++++++++y.      
`+o+++++++++++++++++dhhhhdhssssssssssssssssssssssssssd++++++++++++++++ooooooosssso+++++++++y.       
s+++++++++++++s+++++smhhdyo++++++/////////+++++ooossyy++++++++++++++++++osyyso++++++++++++y.        
/ooosoo++++++++so++++dddh/////////////////////////+oyy++++++++++++++++++yyhhssssooooooo+os.         
  ..-/+s++++++oosyo++sssy+//////////////////////+++/:y+++oooyyo+++++++++yysho+++++ooo++ss`          
       .y++++oooys:++oy-:/oo+++/////////////++++/:---+soosshhhhyo+++++++shssh+++++++++s+            
        y+++ooys:   .:so/:-://oosoooooooooo+//:-::///+shhhhyyyyysdyo++++shsssh++++++os-             
        -yosyo:      `syyyyso+//://////:::-:://+oosyhhhhyyyyysssshhhhysohssssys++++s+`              
         -/:.       .yssssyhhhhhhhysssssssyyyssssmhhyyyyyysssssssymyyyysssssssh++oo-                
                   .hssssssyyyyyyhhho++++++++++++hyyyyssssssssssssNyyyssssssssyyo-                  
                  .hsssssssssyyyyhhy.-:oyo+++++++shyysssssssssssssNyyssssssssssh                    
                 .hsssssssssssyyhd+    :ysyyyyysssdhysssssssssssssNyyssssssssssy:                   
                .hsssssssssssyhhs.     /ssssssssssydysssssssssssssmhyysssssssssss                   
               `ysssssssssssyhy-       +ssssssssssshhsssssssssssssdshhssssssssssy.                  
             ./sssssssssssshy-         ssssssssssss`+yssssssssssss+ .+yysssssssssy-                 
            +ysysssssssssyo-          :yysssssssso   /hsssssssssss:    -+sssssssysd`                
            osdyhsssyyo/:             -+oodyyss+:     +hssssssssss+      `:+yhs//.`                 
              `.-::-`                                  +sssshsshssy
                                                         /syydhyy/-
'''}
Tree_specail = ['Leaves', 25, 20, 5]
Tree_stats = {'Name': 'Treepo', 'Attack' : 17, 'Defense' : 5.4, 'Health' : 56,'Type' : "Grass",
              'Specail' : Tree_specail, 'Exp' : 0, 'MaxHealth' : 40, 'Level' : 10, 'Req' : 20,'Pic' :'''


                                                      .::/:`    `.:::-                              
                                                    .::::::/- -:----::/`                            
                                                   ./::::::://:--::::::+`                           
                                                   /:::::::/+:::::::::::+                           
                                                  -:::::::/+::::::::::::/:                          
                                                  /-::::::+::--::-:::::::o                          
                                                 ./::::::o:::::::::::::::+.                         
                     ..`                         :::::::/+::::::::::::::::/                         
                   `:--::. `                    .o::::::o::::::::://///o::o                         
                   :--::/+/://.                 ///:::::::::::://o:----+::o                         
                  .:o/++s--:://-               `+:+::::::::::++::++----+/:o`                        
                 .:-://oo+++o+///.             .+/::::::::::/s-./hs----+/:o`                        
                 -+::/+o+++oo+/:://:`        .:--.--:::::::::o:.+ds---:o::+              .-/:::-`   
                  `--.```.----///:://:.     ::-----::::::::::/+-oho--:/+:/+            .://s:-:/s:-`
                               `.://:://-` ./:---:::::::::::::++:y::://:/o-          .////+s+//++::s
                                  `.///://///::::::::::::::::::/+///////++       ..:////++++oos+//+o
                                     `-//::/o+::::/:::::////:::::///+o+o+`  `.-/////::/+++++++o///+/
                                        .:///o++//+///+++soooooooosyooo+--:////::////:-.``````.::::`
    `.`                                   `-///+oooossosssooooooossosys++/::///::.``                
 `-////+:.      `.-.`                        .://///+oyysooooossysooo++o+//:.``                     
`+/::/++++-   `+oosso:                         `-//:::/oosysohsoo+oo++:-.`                          
+++++++++o+...oyyyyyyhoooooo+/:-.`               .//::/ossoooyo++/-.`                               
s++++ossooo+++oooossyyyyyysoooooo+/-`         `.:/://++++ooooy:.                                    
++++++++++++++++++oooooossyyssoooooo+/.    `.:::://++/+++++o+o                                      
-o++++++++++++++++oooooooooossyysssssss+.`-:/::://:::/+++++++o                                      
 /+++++++++++++++oooooooooooooossyysssssy//:::/:----:/++++++++                                      
  :+++++++++++oooooooooooooooooooosyyssho/::+/----::/++++++++/                                      
   :oo+++ooooooooooooooooooooooooooosyhs+//o/:::://+++++++++o.                                      
    .+oooooooooooooooooooooooooooooooodo++so+///+++++++++++++                                       
      -ooooooooooooooooooooooooooooooohoooyoo+++++++++++++++.````                                   
        -+osoooooooooooooooooooooooooshsoohooooooo+++++++sso//:::+                                  
          ./ossssssooooooooooosssssssyosssyyoooooooooossys++/::::+..-:::--`  ``                     
             -/osssssssssssssssssssyyo+osssyyysoooooosso+//:+:::/o+/+/---/+//::::.                  
                .:/osssssssssssssyyo+++syyssyys:---..`      +:://://s+:::/oo:--::+.                 
                    `-:+osssssyyys+++oyysss+/.              +::://+++so++oos//::/s-                 
                          ``-ssoo+++oo/:-`                 -/:/+++++++++++oooo+++//                 
                           .o++++++s+                      +:/+++++++++o++/::o+///o`                
                          -o++++ooos.                      :///++++o+:-`      .---`                 
                         .o++///+++s                         .-:--.`                                
                        .+/////////o                                                                
                       .+::://////:+                                                                
                      -///+////////s                                                                
                     `o:-::s///+//://-                                                              
                      :/++o+:--:y/::/s                                                              
                          ./++//:://:` ''' }   

f_pok = ""
fpokstats = 0
stats_gained = {'damage_taken' : 0, 'defence_gained' : 0, 'damage_given' : 0, 'defense_earned' : 0, 'health_gained' : 0,
                'Attack' : 0, 'Defense' : 0, 'Health' : 0, 'MaxHealth' : 0, }
own_poke = {}
pokemon = 0
all_poke = []

class main(tk.Tk): #This is required for tkinter if you want to have the windows one behind another
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (Game, battle): #All Pages made must get their name put in here        
            frame = F(container, self)         
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Game)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Game", font=LARGE_FONT)
        label.grid(row = 0,column=1)

        button1 = tk.Button(self, text="Charlizard", font = LARGE_FONT,
                            command=lambda: f_Char())
        button1.grid(row=1, column=0)
        button1.config(height = 3, width = 10) #This won't fit in under anything than 8
        
        button2 = tk.Button(self, text="Squirter", font = LARGE_FONT,
                            command=lambda: f_Squirt())
        button2.grid(row=1, column=1)
        button2.config(height = 3, width = 10)
        
        button3 = tk.Button(self, text="Duldasuar", font = LARGE_FONT,
                            command=lambda: f_Duld())
        button3.grid(row=1, column=2)
        button3.config(height = 3, width = 10)

        def f_Char():#could do \/
            global f_pok, fpokstats, opstats, op, pokemon, own_poke, all_poke
            pokemon = 0
            all_poke = []
            fpokstats = Char_stats
            own_poke[pokemon] = (Char_stats)
            pokemon +1
            all_poke.append(Char_stats['Name'])
            f_pok = "Charlizard"
            print(f_pok,"Health {0}, Attack {1}, Defense {2}, {3} Type".format(fpokstats['Health'], fpokstats['Attack']
                                                                               , fpokstats['Defense'], fpokstats['Type']))
            time.sleep(1)
            print(fpokstats['Pic'])
            time.sleep(2)
            op = "Duldasuar"
            opstats = Duld_stats
            print("Your oppenent is", op)
            time.sleep(1)
            (self, controller.show_frame(battle))
            #input = (show_frame(battle)) doesn't work
    
        def f_Squirt():
            global f_pok, fpokstats, opstats, op, pokemon, own_poke, all_poke
            pokemon = 0
            all_poke = []
            fpokstats = Squit_stats
            own_poke[pokemon] = (Squit_stats)
            pokemon +1
            f_pok = "Squirtale"
            op = "Charlizard"
            all_poke.append(Squit_stats['Name'])
            opstats = Char_stats
            print(f_pok, "Health {0}, Attack {1}, Defense {2}, {3} Type".format(fpokstats['Health'], fpokstats['Attack']
                                                                          , fpokstats['Defense'], fpokstats['Type']))
            time.sleep(1)
            print(fpokstats['Pic'])
            time.sleep(2)
            print("Your oppenent is", op)
            time.sleep(1)
            (self, controller.show_frame(battle))
            
        def f_Duld():
            global f_pok, fpokstats, opstats, op, pokemon, own_poke, all_poke
            pokemon = 0
            all_poke = []
            fpokstats = Duld_stats
            own_poke[pokemon] = (Duld_stats)
            pokemon +1
            all_poke.append(Duld_stats['Name'])
            fpokstats = own_poke[0]
            f_pok = "Duldasuar"
            op = "Squirt"
            opstats = Squit_stats
            print(f_pok , "Health {0}, Attack {1}, Defense {2}, {3} Type".format(fpokstats['Health'], fpokstats['Attack']
                                                                         , fpokstats['Defense'], fpokstats['Type']))
            time.sleep(1)
            print(fpokstats['Pic'])
            time.sleep(2)
            print("Your oppenent is", op)
            time.sleep(1)
            (self, controller.show_frame(battle))
    
class battle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Battle", font=LARGE_FONT)
        label.grid(row = 0,column=1)
        
        button1 = tk.Button(self, text="Attack", font = LARGE_FONT,
                                command=lambda: attack())
        button1.grid(row=1, column=0)
        button1.config(height = 3, width = 10)
        
        button2 = tk.Button(self, text="Defend", font = LARGE_FONT,
                                command=lambda: defend())
        button2.grid(row=1, column=1)
        button2.config(height = 3, width = 10)
        
        button3 = tk.Button(self, text='Specail', font = LARGE_FONT,
                                command=lambda: specail())
        button3.grid(row=2, column=0)
        button3.config(height = 3, width = 10)

        button4 = tk.Button(self, text="Heal", font = LARGE_FONT,
                            command=lambda: heal())
        button4.grid(row=2, column=1)
        button4.config(height = 3, width = 10)

        def attack():
            global opstats, stats_gained
            fpokstats['Attack'] = fpokstats['Attack']/opstats['Defense']
            opstats['Health'] = opstats['Health'] - fpokstats['Attack']
            stats_gained["damage_given"] = stats_gained["damage_given"] + fpokstats['Attack']
            fpokstats['Attack'] = fpokstats['Attack']*opstats['Defense']
            print(opstats['Name'], "now has", round(opstats['Health']), "Hp")
            turn()

        def defend():
            global fpokstats, stats_gained
            fpokstats['Defense'] = fpokstats['Defense'] + 0.5
            stats_gained["defence_gained"] = stats_gained["defence_gained"] +0.5
            print(fpokstats['Defense'], "defense")
            turn()

        def specail():
            global fpokstats, stats_gained, damage_given
            if(fpokstats['Specail'] ['AP'] >=1):
                if(opstats['Type'] == "Fire" and fpokstats['Type'] == "Water" or
                   opstats['Type'] == "Water" and fpokstats['Type'] == "Grass" or
                   opstats['Type'] == "Grass" and fpokstats['Type'] == "Fire"):
                    fpokstats ['Specail'] ['Attack'] = fpokstats['Specail'] ['Attack']/opstats['Defense']
                    opstats['Health'] = opstats['Health'] - fpokstats['Specail'] ['Attack']
                    stats_gained["damage_given"] = stats_gained["damage_given"] + fpokstats['Specail'] ['Attack']
                    print(fpokstats['Specail'] ['Name'], "did", fpokstats["Specail"] ['Attack'], "damage. IT WAS SUPER EFFECTIVE!")
                    fpokstats['Specail'] ['Attack'] = fpokstats['Specail'] ['Attack']*opstats['Defense']
                elif(opstats['Type'] == fpokstats['Type']):
                    fpokstats['Specail']['Attack'] = fpokstats['Specail'] ['Attack']/opstats['Defense']
                    opstats['Health'] = opstats['Health'] - fpokstats['Specail'] ['Attack']
                    stats_gained['damage_given'] = stats_gained['damage_given'] + fpokstats['Attack']
                    print(fpokstats['Specail'] ['Name'], "did", fpokstats['Attack'], "damage. IT WASN'T EFFECTIVE!")
                    fpokstats['Specail']['Attack'] = fpokstats['Specail'] ['Attack']*opstats['Defense']
                else:
                    fpokstats['Specail']['Weak'] = fpokstats['Specail'] ['Weak']/opstats['Defense']
                    opstats['Health'] = opstats['Health'] - fpokstats['Specail']['Weak']
                    stats_gained['damage_given'] = stats_gained['damage_given'] + fpokstats['Specail']['Weak']
                    print(fpokstats['Specail'] ['Name'],"did", fpokstats['Attack'], "damage. IT WASN'T EFFECTIVE!")
                    fpokstats['Specail']['Weak'] = fpokstats['Specail'] ['Weak']*opstats['Defense']
                fpokstats['Specail'] ['AP'] = fpokstats['Specail'] ['AP'] -1
                print(opstats['Name'], "now has", round(opstats['Health']), "HP")
                turn()

            else:
                print("You don't have any specail move points left!")

        def heal():
            global fpokstats
            if(fpokstats['Health'] >= fpokstats['MaxHealth']):
                print("You can't have moret than", fpokstats['MaxHealth'])
            else:
                fpokstats['Health'] = fpokstats['Health'] + random.randint(1,3)
                turn()

        def turn():
            global damage_taken, stats_gained, opstats,fpokstats, level
            
            if(opstats['Health'] <= 0):
                fpokstats['Defense'] = fpokstats['Defense'] - stats_gained['defence_gained']
                opstats['Health'] = opstats['Health'] + stats_gained['damage_given']
                stats_gained['damage_given'] = 0
                stats_gained['defence_gained'] = 0
                fpokstats['Exp'] = fpokstats['Exp'] + opstats['Level']
                opstats['Level'] = opstats['Level'] - level +5
                opstats['MaxHealth'] = opstats['MaxHealth'] - stats_gained['MaxHealth']
                opstats['Health'] = opstats['MaxHealth']
                opstats['Attack'] = opstats['Attack'] - stats_gained['Attack']
                stats_gained['MaxHealth'] = 0
                stats_gained['Attack'] = 0
                fpokstats['Specail'] ['AP'] = fpokstats ['Specail'] ['APMax']
                if(fpokstats['Exp'] >= fpokstats['Req']):
                    if(fpokstats['Type'] == "Fire"):
                        fpokstats['MaxHealth'] = fpokstats['MaxHealth'] +2
                        fpokstats['Level'] = fpokstats['Level'] +1
                        fpokstats['Attack'] = fpokstats['Attack'] +2
                        fpokstats['Defense'] = fpokstats['Defense'] +0.2
                        
                    elif(fpokstats['Type'] == "Water"):
                        fpokstats['MaxHealth'] = fpokstats['MaxHealth'] +1.5
                        fpokstats['Level'] = fpokstats['Level'] +1
                        fpokstats['Attack'] = fpokstats['Attack'] +1.4
                        fpokstats['Defense'] = fpokstats['Defense'] +0.55
                        
                    elif(fpokstats['Type'] == "Grass"):
                        fpokstats['MaxHealth'] = fpokstats['MaxHealth'] +2.5
                        fpokstats['Level'] = fpokstats['Level'] +1
                        fpokstats['Attack'] = fpokstats['Attack'] +0.1
                        fpokstats['Defense'] = fpokstats['Defense'] +0.4
                        
                    fpokstats['Exp'] = 0
                    fpokstats['Req'] = fpokstats['Req'] +10
                    print("------------------------------------------------------------")
                    print(fpokstats['Name'], "Leveled up and is now level", fpokstats['Level'])
                    time.sleep(2)
                    fpokstats['Health'] = fpokstats['MaxHealth']
                    stats_gained['damage_taken'] = 0
                    fpokstats['Specail'] [1] = 25
                    print("------------------------------------------------------------")
                print(fpokstats['Name'], "gained 7 exp and now has", fpokstats['Exp'], "Exp")
                print("You win!")

                
############################################################################################################################################################
                class Player(pygame.sprite.Sprite):
                    """ This class represents the bar at the bottom that the player
                    controls. """
 
                    # Constructor function
                    def __init__(self, x, y):
                        # Call the parent's constructor
                        super().__init__()
     
                        # Set height, width
                        self.image = pygame.Surface([20, 20])
                        self.image.fill(WHITE)
 
                        # Make our top-left corner the passed-in location.
                        self.rect = self.image.get_rect()
                        self.rect.y = y
                        self.rect.x = x
     
                        # Set speed vector
                        self.change_x = 0
                        self.change_y = 0
                        self.walls = None
                        self.enemy = None
                        self.heal = None
 
                    def changespeed(self, x, y):
                        """ Change the speed of the player. """
                        self.change_x += x
                        self.change_y += y
 
                    def update(self):
                        """ Update the player position. """
                        # Move left/right
                        self.rect.x += self.change_x
 
                        # Did this update cause us to hit a wall?
                        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
                        for block in block_hit_list:
                            # If we are moving right, set our right side to the left side of
                            # the item we hit
                            if self.change_x > 0:
                                self.rect.right = block.rect.left
                            else:
                                # Otherwise if we are moving left, do the opposite.
                                self.rect.left = block.rect.right
                                
                        block_hit_list = pygame.sprite.spritecollide(self, self.enemy, False)
                        for block in block_hit_list:
                            chance = random.randint(1,100)
                            if(chance == 1):
                                new_battle()
                                running = False
                                pygame.quit()
                                sys.exit()

                        block_hit_list = pygame.sprite.spritecollide(self, self.heal, False)
                        for block in block_hit_list:
                            for num in own_poke:
                                own_poke[num] ['Health'] = ownpoke [num] ['MaxHealth']
                                print("Healing")
                                time.sleep(1)
                            print("Healed")

                            if self.change_x > 0:
                                self.rect.right = block.rect.left
                            else:
                                # Otherwise if we are moving left, do the opposite.
                                self.rect.left = block.rect.right
                 
                        # Move up/down
                        self.rect.y += self.change_y
                 
                        # Check and see if we hit anything
                        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
                        for block in block_hit_list:
                 
                            # Reset our position based on the top/bottom of the object.
                            if self.change_y > 0:
                                self.rect.bottom = block.rect.top
                            else:
                                self.rect.top = block.rect.bottom
                        
                        block_hit_list = pygame.sprite.spritecollide(self, self.enemy, False)
                        for block in block_hit_list:
                            chance = random.randint(1,100)
                            if(chance == 1):
                                new_battle()
                                running = False
                                pygame.quit()
                                sys.exit()

                        block_hit_list = pygame.sprite.spritecollide(self, self.heal, False)
                            for num in own_poke:
                                own_poke[num] ['Health'] = ownpoke [num] ['MaxHealth']
                                print("Healing")
                                time.sleep(1)
                            print("Healed")

                            if self.change_y > 0:
                                self.rect.bottom = block.rect.top
                            else:
                                self.rect.top = block.rect.bottom
 
 
                class Wall(pygame.sprite.Sprite):
                    """ Wall the player can run into. """
                    def __init__(self, x, y, width, height):
                        """ Constructor for the wall that the player can run into. """
                        # Call the parent's constructor
                        super().__init__()
 
                        # Make a blue wall, of the size specified inpygame.quit() the parameters
                        self.image = pygame.Surface([width, height])
                        self.image.fill(BLUE)
 
                        # Make our top-left corner the passed-in location.
                        self.rect = self.image.get_rect()
                        self.rect.y = y
                        self.rect.x = x

                class Grass_1(pygame.sprite.Sprite):
                    """ Wall the player can run into. """
                    def __init__(self, x, y, width, height):
                        """ Constructor for the wall that the player can run into. """
                        # Call the parent's constructor
                        super().__init__()
 
                        # Make a blue wall, of the size specified inpygame.quit() the parameters
                        self.image = pygame.Surface([width, height])
                        self.image = pygame.image.load("grass.png")
                                               
 
                        # Make our top-left corner the passed-in location.
                        self.rect = self.image.get_rect()
                        self.rect.y = y
                        self.rect.x = x

                

                class PokemonCentre(pygame.sprite.Sprite):
                    #Pokemon centre code
                    def __init__(self, x, y, width, height):
                        #Call initialiser
                        super().__init__()
                        #Get image
                        self.image = pygame.Surface([width, height])
                        self.image = pygame.image.load("pokeCentEXT.png")
                        #Make top left corner passed in location
                        self.rect = self.image.get_rect()
                        self.rect.y = y
                        self.rect.x = x
 
     
                # Call this function so the Pygame library can initialize itself
                pygame.init()
 
                # Create an 800x600 sized screen
                screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
                # Set the title of the window
                pygame.display.set_caption('Pokémon Alpha v0.0.2 by Logan C, Kieran D, Calvin E, Scott W')
 
                # List to hold all the sprites
                all_sprite_list = pygame.sprite.Group()
 
                # Make the walls. (x_pos, y_pos, width, height)
                wall_list = pygame.sprite.Group()
                enemy_list = pygame.sprite.Group()
                heal_list = pygame.sprite.Group()
 
                wall = Wall(0, 0, 10, 600)
                wall_list.add(wall)
                all_sprite_list.add(wall)
 
                wall = Wall(10, 0, 790, 10)
                wall_list.add(wall)
                all_sprite_list.add(wall)
 
                wall = Wall(0, 590, 800, 10)
                wall_list.add(wall)
                all_sprite_list.add(wall)

                wall = Wall(790, 0, 20, 1000)
                wall_list.add(wall)
                all_sprite_list.add(wall)

                # Create the player paddle object
                player = Player(50, 50)
                player.enemy = enemy_list
                player.walls = wall_list
                player.heal = heal_list
 
                all_sprite_list.add(player)

                enemy = Grass_1(100, 100, 10, 10)
                enemy_list.add(enemy)
                all_sprite_list.add(enemy)

                enemy = Grass_1(130, 100, 10, 10)
                enemy_list.add(enemy)
                all_sprite_list.add(enemy)

                enemy = Grass_1(160, 100, 10, 10)
                enemy_list.add(enemy)
                all_sprite_list.add(enemy)

                enemy = Grass_1(190, 100, 10, 10)
                enemy_list.add(enemy)
                all_sprite_list.add(enemy)

                heal = PokemonCentre(200, 200, 60, 53)
                heal_list.add(heal)
                all_sprite_list.add(heal)



                

                clock = pygame.time.Clock()
 
                done = False
 
                while not done:
 
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
 
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                player.changespeed(-3, 0)
                            elif event.key == pygame.K_d:
                                player.changespeed(3, 0)
                            elif event.key == pygame.K_w:
                                player.changespeed(0, -3)
                            elif event.key == pygame.K_s:
                                player.changespeed(0, 3)
 
                        elif event.type == pygame.KEYUP:
                            if event.key == pygame.K_a:
                                player.changespeed(3, 0)
                            elif event.key == pygame.K_d:
                                player.changespeed(-3, 0)
                            elif event.key == pygame.K_w:
                                player.changespeed(0, 3)
                            elif event.key == pygame.K_s:
                                player.changespeed(0, -3)
 
                    all_sprite_list.update()
                    
                    screen.fill(BLACK)
 
                    all_sprite_list.draw(screen)
 
                    pygame.display.flip()
 
                    clock.tick(60)
 
                pygame.quit()
############################################################################################################################################################
                
            elif(fpokstats['Type'] == "Fire" and opstats['Type'] == "Water" and fpokstats['Health'] >= 10 or
                 fpokstats['Type'] == "Water" and opstats['Type'] == "Grass" and fpokstats['Health'] >= 10 or
                 fpokstats['Type'] == "Grass" and opstats['Type'] == "Fire" and fpokstats['Health'] >= 10):		
                opstats['Attack'] = opstats['Attack']/fpokstats['Defense']
                fpokstats['Health'] = fpokstats['Health'] - opstats['Attack']
                stats_gained["damage_taken"] = stats_gained["damage_taken"] + opstats['Attack']
                opstats['Attack'] = opstats['Attack']*fpokstats['Defense']
                print(opstats["Name"] ,"used his specail")
                print("\n\n", fpokstats['Name'], "now has", round(fpokstats['Health']),"Health")
                
            else:
                opstats['Attack'] = opstats['Attack']/fpokstats['Defense']
                fpokstats['Health'] = fpokstats['Health'] - opstats['Attack']
                stats_gained["damage_taken"] = stats_gained["damage_taken"] + opstats['Attack']
                opstats['Attack'] = opstats['Attack']*fpokstats['Defense']
                print(opstats["Name"] ,"attacked")
                print("\n\n", fpokstats['Name'], "now has", round(fpokstats['Health']),"Health")

            if(fpokstats['Health'] <= 0):
                fpokstats['Health'] = fpokstats['Health'] + stats_gained['damage_taken']
                fpokstats['Health'] = fpokstats['Health'] - stats_gained['health_gained']
                fpokstats['Defense'] = fpokstats['Defense'] - stats_gained['defence_gained']
                opstats['Health'] = opstats['Health'] + stats_gained['damage_given']
                stats_gained['damage_given'] = 0
                stats_gained['damage_taken'] = 0
                stats_gained['defence_gained'] = 0
                fpokstats['Specail']['AP'] = fpokstats['Specail'] ['APMax']
                fpokstats['Health'] = fpokstats['MaxHealth']
                print("You lost!")
                print("GAME OVER!")
                self, controller.show_frame(Game)

        def new_battle():
            global opstats, level, fpokstats, own_poke
            if(fpokstats['Level'] >= 15):
                level = random.randint(6,20)
                op_pos = [Tor_stats, Osh_stats, Odd_stats, Cyn_stats, Tree_stats, Mud_stats]
                x = random.randint(0, 5)
            else:
                level = random.randint(2,5)
                op_pos = [Tor_stats, Osh_stats, Odd_stats]
                x = random.randint(0, 2)
            opstats = op_pos[x]
            if(opstats['Type'] == "Fire"):
                opstats['Attack'] = opstats['Attack'] +(opstats['Level']-10)*2
                stats_gained['Attack'] =(opstats['Level']-10)*2
                opstats['MaxHealth'] = opstats['MaxHealth'] +(opstats['Level']-10)*2
                stats_gained['MaxHealth'] = (opstats['Level']-10)*2
                opstats['Health'] = opstats['MaxHealth']
                opstats['Defense'] = opstats['Defense'] +(opstats['Level']-10)*0.2
                                                              
            elif(opstats['Type'] == "Water"):
                opstats['Attack'] = opstats['Attack'] +(opstats['Level']-10)*1.4
                stats_gained['Attack'] =(opstats['Level']-10)*1.5
                opstats['MaxHealth'] = opstats['MaxHealth'] +(opstats['Level']-10)*1.5
                stats_gained['MaxHealth'] = (opstats['Level']-10)*2
                opstats['Health'] = opstats['MaxHealth']
                opstats['Defense'] = opstats['Defense'] +(opstats['Level']- 10)*0.55
                        
            elif(opstats['Type'] == "Grass"):
                opstats['Attack'] = opstats['Attack'] +(opstats['Level']-10)*1
                stats_gained['Attack'] =(opstats['Level']-10)*1
                opstats['MaxHealth'] = opstats['MaxHealth'] +(opstats['Level']-10)*2.5
                stats_gained['MaxHealth'] = (opstats['Level']-10)*2
                opstats['Health'] = opstats['MaxHealth']
                opstats['Defense'] = opstats['Defense'] +(opstats['Level']-10)*0.4
                                                              
            print(opstats['Pic'])
            print("Health", opstats['Health'], "Level",opstats['Level'])
            print("You found a random", opstats['Name'])
            print("\n\n")
            print("What pokemon would you like to use ? ")
            x = 0
            for pokemon in all_poke:
                print(x +1,".", all_poke[x])
                x = x+1
            x = int(input(":"))
            x = x-1
            while(fpokstats != own_poke[x]):
                try:
                    fpokstats = own_poke[x]
                except KeyError:
                    print("That wasn't in range")
                x = int(input(":"))
                x = x-1

app = main() #These loops keep the app running none stop \/
app.mainloop()
