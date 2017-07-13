### GWC Final Project by Seok Hee Hong, Brynn Jones, Star Riley, Kenyetta Akowa
# The script of the game goes in this file.
#-------------------------------------------------------------------------------
##CHARACTERS
#define  = Character(_(''), color="#FFFFFF")

#MAIN -----need to change the color for each character
define z = Character(_('Z'), color="#c8ffc8")  #AKA PROTAG-KUN
define Brazil = Character(_('Natalia Perez'), color="#c8ffc8")
define China = Character(_('Liling Wong'), color="#c8ffc8")
define England = Character(_('James Williams'), color="#c8ffc8")
define France = Character(_('Lucas Henry'), color="#c8ffc8")
define Japan = Character(_('Yuno Akizawa'), color="#c8ffc8")
define Russia = Character(_('Isidor Mikhailov'), color="#c8ffc8")
define NKorea = Character(_('Jinsoo'), color="#c8ffc8")
define SKorea = Character(_('Jisoo'), color="#c8ffc8")
define Italy = Character(_('Antonio Amadi'), color="#c8ffc8")
define Spain = Character(_('Ximena Hernandez '), color="#c8ffc8")
define Canada = Character(_('Lola Wright'), color="#c8ffc8")
define USA = Character(_('Jaime Black'), color="#c8ffc8")   #FALSE MASTERMIND
define Vietnam = Character(_('Kim-ly Mai'), color="#c8ffc8")   #TINY MASTERMIND
define Singapore = Character(_('Mengyao Shen'), color="#c8ffc8")   #ACTUAL MASTERMIND
define Philippines = Character(_('Mahalia Andrada'), color="#c8ffc8")   #NPC
define Germany = Character(_('Dieck Berhtram'), color="#c8ffc8")   #NPC
define NewZealand = Character(_('Georgia Reid'), color="#c8ffc8")   #NPC

#SECONDARY
define unknown = Character(_('???'), color="#FFFFFF")  #IF THE CHARACTER IS UNKNOWN OR HIDDEN IDENTITY
define note = Character(_('Note:'), color="#FFFFFF")

#EXTRA
define mb = Character(_('Mr. Black'), color="#FFFFFF")
define mbc = Character(_('Mr. Black\'s Child'), color="#FFFFFF")
define emp = Character(_('Employee'), color="#FFFFFF")
define com = Character(_('Intercom'), color="#FFFFFF")
define mk = Character(_('Ms. Karen'), color="#FFFFFF")
define gm = Character(_('Grown Man'), color="#FFFFFF")
define ym = Character(_('Young Man'), color="#FFFFFF")
define jj = Character(_('James Jefferson'), color="#FFFFFF")


define narration = nvl_narrator
#define narration = Character(kind=nvl)

#-------------------------------------------------------------------------------
###IMAGES
##CHARACTERS
#-------------------Mengyao Shen-------------------------------------
image MB = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mr_Black.png'
image MB_0 = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_angry.png'
image MB_1 = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_whin.png'
image MB_2 = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_surpried.png'
image MB_3 = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_looking.png'
image MB_4 = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_happy.png'
<<<<<<< HEAD
#------------------------Kim-ly Mai-----------------------------------
=======
>>>>>>> ffbae62276bcf8f54b2cd6b7ca4955801fe81f76
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_happy.png'
image Kim_0 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_angry.png'
image Kim_1 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_Teeth-smile.png'
image Kim_2 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_calm.png'
image Kim_3 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_cry.png'
image Kim_4 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_oh.png'
image Kim_5 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_sad.png'
image Kim_6 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_smile.png'
image Kim_7 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_surprised.png'
image Kim_8 = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_upset.png'
image Jaime = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_happy.png'
image Jaime_0 = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_neutral.png'
image Jaime_1 = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_mad.png'
image Jaime_2 = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_sad.png'
image Jaime_3 = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_scared.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_happy.png'
image Dieck_0 = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_wink.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_surprise.png'
image Dieck-1 = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_pokerface.png'
image Dieck_2 = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_mad.png'
image Dieck_3 = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_dissapointed.png'
image Georgia = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_happy.png'
image Georgia_0 = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_mad.png'
image Georgia_1 = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_shy.png'
image Georgia_2 = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_surprised.png'
image Georgia_3 = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_surprised2.png'
image Georgia_4 = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/pokerface.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_angry.png'
image Mahalia_0 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_angry2.png'
image Mahalia_1 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_closeeye.png'
image Mahalia_2 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_halfclose.png'
image Mahalia_3 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_mad.png'
image Mahalia_4 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_pokerface.png'
image Mahalia_5 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_shout.png'
image Mahalia_6 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_smile.png'
image Mahalia_7 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_smile2.png'
image Mahalia_8 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_surprised.png'
image Mahalia_9 = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_sympathy.png'
image Antonio = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Annoyed.png'
image Antonio_0 = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Nuetral.png'
image Antonio_1 = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Psyched.png'
image Antonio_2 = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Shooketh.png'
image Antonio_3 = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Worried.png'
image Isidor = 'sprites/Participants/Participants/Isidor Mikhailov (Russia)/Isidor_Happy.png'
image Isidor_0 = 'sprites/Participants/Participants/Isidor Mikhailov (Russia)/Isidor_Kre.png'
image Isidor_1 = 'sprites/Participants/Participants/Isidor Mikhailov (Russia)/Isidor_Mad.png'
image Isidor_2 = 'sprites/Participants/Participants/Isidor Mikhailov (Russia)/Isidor_Neutral.png'
image Isidor_3 = 'sprites/Participants/Participants/Isidor Mikhailov (Russia)/Isidor_Regretful.png'
image Isidor_4 = 'sprites/Participants/Participants/Isidor Mikhailov (Russia)/Isidor_Shooketh.png'
image James = 'sprites/Participants/Participants/James Williams (England)/James_Neutral.png'
image James_0 = 'sprites/Participants/Participants/James Williams (England)/James_Regular.png'
image James_1 = 'sprites/Participants/Participants/James Williams (England)/James_Shooketh.png'
image James_2 = 'sprites/Participants/Participants/James Williams (England)/James_Smile.png'
image James_3 = 'sprites/Participants/Participants/James Williams (England)/James_Worried.png'
image Ji = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_.png'
image Ji_0 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Angry.png'
image Ji_1 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Concerned.png'
image Ji_2 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Frustrated.png'
image Ji_3 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Happy.png'
image Ji_4 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Neutral.png'
image Ji_5 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Reprimand.png'
image Ji_6 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Smile.png'
image Ji_7 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Surprised.png'
image Ji_8 = 'sprites/Participants/Participants/Ji su (Korean)/Jisoo_Sympathetic.png'
image Jin = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_Angry.png'
image Jin_0 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_AngryTalk.png'
image Jin_1 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_Embarrassed.png'
image Jin_2 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_Happy.png'
image Jin_3 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_HappyTalk.png'
image Jin_4 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_HellaSad.png'
image Jin_5 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_Neutral.png'
image Jin_6 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_Precious.png'
image Jin_7 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_Sad.png'
image Jin_8 = 'sprites/Participants/Participants/Jin soo (North Korea)/Jinsoo_Smile.png'
image Liling = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Blush.png'
image Liling_0 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Concerned.png'
image Liling_1 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Embarrassed.png'
image Liling_2 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Neutral.png'
image Liling_3 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Reg.png'
image Liling_4 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_RegTalk.png'
image Liling_5 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Shooketh.png'
image Liling_6 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Shy.png'
image Liling_7 = 'sprites/Participants/Participants/Liling Wong (China)/Liling_Smile.png'
image Lola = 'sprites/Participants/Participants/Lola Wright (Canada)/Lola_Concerned.png'
image Lola_0 = 'sprites/Participants/Participants/Lola Wright (Canada)/Lola_Frustrated.png'
image Lola_1 = 'sprites/Participants/Participants/Lola Wright (Canada)/Lola_Happy.png'
image Lola_2 = 'sprites/Participants/Participants/Lola Wright (Canada)/Lola_Neutral.png'
image Lola_3 = 'sprites/Participants/Participants/Lola Wright (Canada)/Lola_Perv.png'
image Lola_4 = 'sprites/Participants/Participants/Lola Wright (Canada)/Lola_Shooketh.png'
image Lucas = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Bored.png'
image Lucas_0 = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Chill.png'
image Lucas_1 = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Exhausted.png'
image Lucas_2 = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Frustrated.png'
image Lucas_3 = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Happy.png'
image Lucas_4 = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Neutral.png'
image Lucas_5 = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Sad.png' 
image Lucas_6 = 'sprites/Participants/Participants/Lucas Henry (France)/Lucas_Surprised.png'
image Natalia = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Crying.png'
image Natalia_0 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Embarrassed.png'
image Natalia_1 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Frustrated.png'
image Natalia_2 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Happy.png'
image Natalia_3 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Neutral.png'
image Natalia_4 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_sad.png'
image Natalia_5 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Scared.png'
image Natalia_6 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Shooketh.png'
image Natalia_7 = 'sprites/Participants/Participants/Natalia Perez (Brazil)/Natalia_Smile.png'
image Ximena = 'sprites/Participants/Participants/Ximena Hernandez (Spain)/Ximena_Concerned.png'
image Ximena_0 = 'sprites/Participants/Participants/Ximena Hernandez (Spain)/Ximena_Deadass.png'
image Ximena_1 = 'sprites/Participants/Participants/Ximena Hernandez (Spain)/Ximena_Happy.png' 
image Ximena_2 = 'sprites/Participants/Participants/Ximena Hernandez (Spain)/Ximena_Neutral.png'
image Ximena_3 = 'sprites/Participants/Participants/Ximena Hernandez (Spain)/Ximena_Poker.png'
image Ximena_4 = 'sprites/Participants/Participants/Ximena Hernandez (Spain)/Ximena_Shooketh.png'
image Yuno = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Cocky.png'
image Yuno_0 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Enraged.png'
image Yuno_1 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Exhausted.png'
image Yuno_2 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Neutral.png'
image Yuno_3 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Reprimand.png'
image Yuno_4 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Sad.png'
image Yuno_5 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Shooketh.png'
image Yuno_6 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Sly.png'
image Yuno_7 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_SuckHerCockiness.png'
image Yuno_8 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_Sympathy.png'
image Yuno_9 = 'sprites/Participants/Participants/Yuno Akizawa (Japan)/Yuno_yIKES.png'
<<<<<<< HEAD
>>>>>>> ffbae62276bcf8f54b2cd6b7ca4955801fe81f76
=======
>>>>>>> ffbae62276bcf8f54b2cd6b7ca4955801fe81f76


#BACKGROUNDS
image 0_outside = 'backgrounds/0_outside.jpg'
image 0_office = 'backgrounds/0_office.jpg'
image 1_clearbluesky = 'backgrounds/1_clearbluesky.jpg'
image 1_Dormroom = 'backgrounds/1_Dormroom.jpg'
image 1_Flower = 'backgrounds/1_Flower.jpg'
image 1_Warehouse.jpg = 'backgrounds/1_Flower.jpg'
image Library_Day = 'backgrounds/f_tool.jpg'
image Flower_Night = 'backgrounds/flower_night.jpg'
image Forest_Night = 'backgrounds/forest_night.jpg'
image Library_Night = 'backgrounds/Library_Night.jpg'
image Dormroom_OpenDrawer = 'backgrounds/room.jpg'
image Room_Night = 'backgrounds/Room_Night.jpg'
image SunsetSky = 'backgrounds/Subsetsky.jpg'

#-------------------------------------------------------------------------------
# The game starts here.

label start:

label prologue:
    scene 0_outside with fade

    mb "Do you have the ship ready?"
    emp "Sir, yes sir!"
    
    mbc "Are you {i}sure{/i} that you’re going to layout this plan?"

    mb "Are you questioning my decisions? Please tell me that one of my bright children is not telling me if my plan is good or not."
    mbc "No, Father. I’m just saying that this plan is rather… immoral… for the goal that you want to achieve."
    mbc "I will always respect your authority, but if this ends up in flames,  I would prefer to not go down with you."
    mb "We’re playing an innocent role now, hm? When you have a plan, you always follow it till the end; no matter the cost."
    com "Mr. Black-"
    mb "Unless, of course, you are deemed unworthy for it?"
    mbc "..."
    com "{i}Mr. Black.{/i} The conference meeting has already started in room CS4. I repeat-" 
    mb "Let’s carry on with this conversation some other time."
    mbc "I would prefer not to, but later." 

    scene 0_office with fade
    
    mk "Mr. Black. You're late. Had too many drinks last night that you couldn't get your head straight?"
    mb "You’re not far off from wrong, Ms. Karen. I’m also not far off from wrong when I say that I saw your wife with another woman."
    mk "You little-"
    gm "Hey! The president, James Jefferson, is walking in!"
    #Mr. Black looks at the door and sees a man
    "Hmmm...James Jefferson... So that's the president retiring today… My, my, he surely is making the right decision."
    jj "Hello everyone. I'm sorry that I am late, but let’s cut to the chase. I’m very certain that you have more things to do outside of this room."
    jj "As you three have might figured out, I see you as potential candidates for running our first program, Central Organization Decoded Environment of Teens With Ability (CODETWA)."
    ym "Well…"
    jj "Yes?"
    ym "I might be young, but that only proves of how much I can emotionally connect with the students. Because of this, I believe that I can be the leader for this arrangement."
    mk "Wait! I think that I can handle with running this program. I know how kids act, so I'm used to teaching-"
    ym "Just because you can get pregnant and have kids doesn't mean that you can run a facility while looking after them! President, I would be your wisest choice."
    "A small smirk grew on my lips. I couldn’t help but to admire his confidence, but that wouldn’t last too long with me in the room."
    mb "And what if you weren’t his wisest choice?"
    ym "Huh…?"
    mb "What if he deemed all of your contributions to be meaningless, therefore compared to us two, you weren’t even a thought that slipped into his mind?"
    ym "Eh, well...I’m not so-"
    mb "Hm, if you really were confident in this role that you oh-so desire, you would already know how to handle not getting it if someone else snatches it away from your tight grasp."
    mb "After all, how can your sympathetic asset compete against someone who has that and more…?"
    narration "And when he noticed Jefferson’s irises focusing now on him, Mr. Black knew for certain that the crown was now in his hands, and no one can snatch it away from him."
    narration "Not even in death."
<<<<<<< HEAD
    
    # This Ends Prologue
#--------------------------------------------------------------------
# Beginning of Chapter One
    nvl clear

label chapterOne: 
=======
    nvl clear
   
label chapterOne:
>>>>>>> ffbae62276bcf8f54b2cd6b7ca4955801fe81f76
    scene 0_outside with fade
    #Protag-kun opens eyes 
    z "Hmmm….ugh. Where am I?"
    #Protag-kun sees a flower with a note next to it
    z "What’s this? A sparkling flower?"
    z "Let me actually see what this is." 
    #Protag-kun opens the note
    note "Greetings,  Z. You probably don’t know anything right about now. Heh, well, of course, you don’t! Unless I used the wrong drug on you…"
    note "Anyways, you are about to enter a world filled with mystery. It is important that you set your mind only on the truth and to not let despair seep into your soul."
    note "You are everyone’s hope and everyone is counting on you. Don’t ever forget that."
    z "...kre"
    note "You may still be confused and utterly baffled Z, but trust me; everything will unfold itself soon." 
    "I’m confused and baffled at the very fact that I received a note from a flower"
    z "Great, all that I learned about myself is my name, Z. Well, that’s better than Bob or something-"
    #Protag-kun hears the bushes around xhem, and xhe stands up and turns around
    z "I ain’t playing these games. Show yourself!"
    #Protag-kun gets into defense mode
    unknown "Hey! It’s just me."
    z "The only “me” I know is myself, so-"
    unknown "Alright. Alright I was going to step out in the first place. Don’t get ahead of yourself buddy."
    #Protag-kun sees a girl step out of the bushes with a green bow and some unique clothes that Protag-kun never seen before)(She looks at the ground with her hand next to her mouth contemplating about something)
    "Maybe she’s worried because she doesn’t know where we are either. I should to console her!"

    
<<<<<<< HEAD

    # This Ends Chapter One
#--------------------------------------------------------------------
# Beginning of Chapter Two

label chapterTwo: 
    
    # This Ends Chapter Two

    # This ends the game
=======
    # This ends the game.
>>>>>>> ffbae62276bcf8f54b2cd6b7ca4955801fe81f76

    return
