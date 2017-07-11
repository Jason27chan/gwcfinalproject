### GWC Final Project by Seok Hee Hong, Brynn Jones, Star Riley, Kenyetta Akowa
# The script of the game goes in this file.
#-------------------------------------------------------------------------------
##CHARACTERS
#define  = Character(_(''), color="#FFFFFF")

#MAIN -----need to change the color for each character
define z = Character(_('Z'), color="#c8ffc8")
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
define USA = Character(_('Jaime Black'), color="#c8ffc8")
define Vietnam = Character(_('Kim-ly Mai'), color="#c8ffc8")
define Singapore = Character(_('Mengyao Shen'), color="#c8ffc8")
define Philippines = Character(_('Mahalia Andrada'), color="#c8ffc8")
define Germany = Character(_('Dieck Berhtram'), color="#c8ffc8")
define NewZealand = Character(_('Georgia Reid'), color="#c8ffc8")

#SECONDARY
define note = Character(_('Note:'), color="#FFFFFF")

#EXTRA
define mm = Character(_('Mystery Man'), color="#FFFFFF")
define mmc = Character(_('Mystery Man\'s Child'), color="#FFFFFF")
define emp = Character(_('Employee'), color="#FFFFFF")
define com = Character(_('Intercom'), color="#FFFFFF")
define mk = Character(_('Ms. Karen'), color="#FFFFFF")

#-------------------------------------------------------------------------------
##IMAGES
#CHARACTERS

#BACKGROUNDS

#-------------------------------------------------------------------------------
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    
    # This ends the game.

    return
