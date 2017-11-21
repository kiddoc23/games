#!/bin/python
#Made by - Kieran Docherty, Logan Chalmers, Scott Whailin, Calvin Earnshaw, Magnus a little, and Joe- 2017
#This is the base for any tkinter programs i write
#Can use console and Gui at same time
import random
import tkinter as tk #Import is required i name it tk for ease of use
import time # \/
from msvcrt import getch
#Not required but here bc I often use them

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



global Char_stats, Squit_stats, Duld_stats, f_pok, fpokstats, duld, char, squirt, damage_taken, defence_gained, damage_given, defense_earned, level
#global all pokemon stats might be able to put all pokemon in on array?
level = 5
Char_specail = ['Ember', 25, 25, 5]
Char_stats = {'Name': 'Charzard', 'Attack' : 10, 'Defense' : 1.5, 'Health' : 25,'Type' : "Fire", 
              'Specail' : Char_specail , 'Exp' : 0, 'MaxHealth' : 25, 'Level' : 10, 'Req' : 20, 'Pic' : """
                                                                                                    
                                                                                                    
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

Squit_specail = ['Water Gun', 25, 20, 5]
Squit_stats = {'Name': 'Squirtale', 'Attack' : 8, 'Defense' : 3.5, 'Health' : 25,'Type' : "Water",
               'Specail' :Squit_specail, 'Exp' : 0, 'MaxHealth' : 25, 'Level' : 10, 'Req' : 20, 'Pic' : """
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

Duld_specail = ['Leaves', 25, 20, 5]
Duld_stats = {'Name': 'Duldasuar', 'Attack' : 8, 'Defense' : 1.5, 'Health' : 35,'Type' : "Grass",
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

Osh_stats = {'Name': 'Oshiwish', 'Attack' : 6, 'Defense' : 1, 'Health' : 25,'Type' : "Water",
              'Exp' : 0, 'MaxHealth' : 25, 'Level' : level, 'Req' : 10,'Specail' :25, 'Pic' : """
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

Odd_stats = {'Name': 'Oddush', 'Attack' : 6, 'Defense' : 1, 'Health' : 20,'Type' : "Grass",
              'Exp' : 0, 'MaxHealth' : 20, 'Level' : level, 'Req' : 10,'Specail' : 25, 'Pic' : """
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

Tor_stats = {'Name': 'Torchick', 'Attack' : 8, 'Defense' : 1, 'Health' : 20,'Type' : "Fire",
              'Exp' : 0, 'MaxHealth' : 20, 'Level' : level, 'Req' : 10, 'Specail' :'Ember', 'Pic' : """
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

f_pok = ""
fpokstats = 0
stats_gained = {'damage_taken' : 0, 'defence_gained' : 0, 'damage_given' : 0, 'defense_earned' : 0, 'health_gained' : 0}

class main(tk.Tk): #This is required for tkinter if you want to have the windows one behind another

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (Start_Page, Help, Game, battle): #All Pages made must get their name put in here
        
            frame = F(container, self)
            
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Game)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class Start_Page(tk.Frame): #Most is copy and paste-able just change names, (Hopme pgae is first page)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Help", font = LARGE_FONT,
                            command=lambda: controller.show_frame(Help))
        button1.pack()
        button1 = tk.Button(self, text="Start", font = LARGE_FONT,
                            command=lambda: controller.show_frame(Game))
        button1.pack()       

class Help(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Help Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Start Page", font = LARGE_FONT,
                            command=lambda: controller.show_frame(Start_Page))
        button1.pack()

        button1 = tk.Button(self, text="Start", font = LARGE_FONT,
                            command=lambda: controller.show_frame(Game))
        button1.pack()  


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
            global f_pok, fpokstats, opstats, op
            fpokstats = Char_stats
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
            global f_pok, fpokstats, opstats, op
            fpokstats = Squit_stats
            f_pok = "Squirtale"
            op = "Charlizard"
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
            global f_pok, fpokstats, opstats, op
            fpokstats = Duld_stats
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

    button_delay = 0.2


    while True:
        char = getch()

        if (char == "q"):
            attack()
            time.sleep(button_delay)
        elif (char == "r"):
            specail()
            time.sleep(button_delay)
        elif (char == "e"):
            defend()
            time.sleep(button_delay)
        elif (char == "f"):
            heal()
            time.sleep(button_delay)
        elif (char == "p"):
            print("Keystrokes Help:\n\nw:     Forward\na:     Left\ns:    Backwards\nd:     Right\n\nq:     Attack\nr:     Specail\ne:     Defend\nf:     Heal\np:     Help")
            time.sleep(button_delay)

            

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
            fpokstats['Attack'] = fpokstats['Attack'] - opstats['Defense']
            opstats['Health'] = opstats['Health'] - fpokstats['Attack']
            stats_gained["damage_given"] = stats_gained["damage_given"] + fpokstats['Attack']
            fpokstats['Attack'] = fpokstats['Attack'] + opstats['Defense']
            print(opstats['Name'], "now has", round(opstats['Health']), "Hp")
            turn()

        def defend():
            global fpokstats, stats_gained
            fpokstats['Defense'] = fpokstats['Defense'] + 1
            stats_gained["defence_gained"] = stats_gained["defence_gained"] +1
            print(fpokstats['Defense'], "defense")
            turn()

        def specail():
            global fpokstats, stats_gained, damage_given
            if(fpokstats['Specail'] [1] >=1):
                if(opstats['Type'] == "Fire" and fpokstats['Type'] == "Water" or
                   opstats['Type'] == "Water" and fpokstats['Type'] == "Grass" or
                   opstats['Type'] == "Grass" and fpokstats['Type'] == "Fire"):
                    fpokstats['Attack'] = fpokstats['Specail'] [2] + 5
                    fpokstats['Attack'] = fpokstats['Specail'] [2]/opstats['Defense']
                    opstats['Health'] = opstats['Health'] - fpokstats['Attack']
                    stats_gained["damage_given"] = stats_gained["damage_given"] + fpokstats['Attack']
                    print(fpokstats['Specail'] [0], "did", fpokstats["Attack"], "damage. IT WAS SUPER EFFECTIVE!")
                    fpokstats['Attack'] = fpokstats['Specail'] [2]*opstats['Defense']
                    fpokstats['Attack'] = fpokstats['Specail'] [2] - 5
                elif(opstats['Type'] == fpokstats['Type']):
                    fpokstats['Attack'] = fpokstats['Specail'] [3]/opstats['Defense']
                    opstats['Health'] = opstats['Health'] - fpokstats['Attack']
                    stats_gained['damage_given'] = stats_gained['damage_given'] + fpokstats['Attack']
                    print(fpokstats['Specail'] [0], "did", fpokstats['Attack'], "damage. IT WASN'T EFFECTIVE!")
                    fpokstats['Attack'] = fpokstats['Specail'] [3]*opstats['Defense']
                else:
                    fpokstats['Attack'] = fpokstats['Specail'] [3] - 5
                    fpokstats['Attack'] = fpokstats['Specail'] [3]/opstats['Defense']
                    opstats['Health'] = opstats['Health'] - fpokstats['Attack']
                    stats_gained['damage_given'] = stats_gained['damage_given'] + fpokstats['Attack']
                    print(fpokstats['Specail'] [0],"did", fpokstats['Attack'], "damage. IT WASN'T EFFECTIVE!")
                    fpokstats['Attack'] = fpokstats['Specail'] [3]*opstats['Defense']
                    fpokstats['Attack'] = fpokstats['Specail'] [3] + 5
                fpokstats['Specail'] [1] = fpokstats['Specail'] [1] -1
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
            global damage_taken, stats_gained, opstats,fpokstats
            
            if(opstats['Health'] <= 0):
                fpokstats['Defense'] = fpokstats['Defense'] - stats_gained['defence_gained']
                opstats['Health'] = opstats['Health'] + stats_gained['damage_given']
                stats_gained['damage_given'] = 0
                stats_gained['defence_gained'] = 0
                fpokstats['Exp'] = fpokstats['Exp'] +7
                if(fpokstats['Exp'] >= fpokstats['Req']):
                    fpokstats['MaxHealth'] = fpokstats['MaxHealth'] +2
                    fpokstats['Level'] = fpokstats['Level'] +1
                    fpokstats['Attack'] = fpokstats['Attack'] +2
                    fpokstats['Defense'] = fpokstats['Defense'] +0.2
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
                new_battle()
            
            elif(fpokstats['Type'] == "Fire" and opstats['Type'] == "Water" and fpokstats['Health'] >= 10):		
                opstats['Attack'] = opstats['Attack'] + 5
                opstats['Attack'] = opstats['Attack']/fpokstats['Defense']
                fpokstats['Health'] = fpokstats['Health'] - opstats['Attack']
                stats_gained["damage_taken"] = stats_gained["damage_taken"] + opstats['Attack']
                opstats['Attack'] = opstats['Attack']*fpokstats['Defense']
                opstats['Attack'] = opstats['Attack'] - 5
                print(opstats["Name"] ,"used his specail")
                print("\n\n", fpokstats['Name'], "now has", round(fpokstats['Health']),"Health")

            elif(fpokstats['Type'] == "Water" and opstats['Type'] == "Grass" and fpokstats['Health'] >= 10):		
                opstats['Attack'] = opstats['Attack'] + 5
                opstats['Attack'] = opstats['Attack']/fpokstats['Defense']
                fpokstats['Health'] = fpokstats['Health'] - opstats['Attack']
                stats_gained["damage_taken"] = stats_gained["damage_taken"] + opstats['Attack']
                opstats['Attack'] = opstats['Attack']*fpokstats['Defense']
                opstats['Attack'] = opstats['Attack'] - 5
                print(opstats["Name"] ,"used his specail")
                print("\n\n", fpokstats['Name'], "now has", round(fpokstats['Health']),"Health")

            elif(fpokstats['Type'] == "Grass" and opstats['Type'] == "Fire" and fpokstats['Health'] >= 10):		
                opstats['Attack'] = opstats['Attack'] + 5
                opstats['Attack'] = opstats['Attack']/fpokstats['Defense']
                fpokstats['Health'] = fpokstats['Health'] - opstats['Attack']
                stats_gained["damage_taken"] = stats_gained["damage_taken"] + opstats['Attack']
                opstats['Attack'] = opstats['Attack']*fpokstats['Defense']
                opstats['Attack'] = opstats['Attack'] - 5
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
                fpokstats['Specail'] = 25
                print("You lost!")
                print("GAME OVER!")
                (self, controller.show_frame(Game))

        def new_battle():
            global opstats, level
            level =random.randint(1, 6)
            if(opstats['Name'] == 'Torchick'):
                op_pos = [Odd_stats, Osh_stats]
                x = random.randint(0, 1)
            elif(opstats['Name'] == 'Oddish'):
                op_pos = [Tor_stats, Osh_stats]
                x = random.randint(0, 1)
            elif(opstats['Name'] == 'Oshiwish'):
                op_pos = [Tor_stats, Odd_stats]
                x = random.randint(0, 1)
            else:
                op_pos = [Tor_stats, Osh_stats, Odd_stats]
                x = random.randint(0, 2)
            opstats = op_pos[x]
            print(opstats['Pic'])
            (self, controller.show_frame(battle))


app = main() #These loops keep the app running none stop \/
app.mainloop()
