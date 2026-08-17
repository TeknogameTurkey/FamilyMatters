#---------------------adds/enhancements for screens.rpy---------------------#


#---------------------dialog/choice options---------------------#
# define gui.name_xpos = 360
# define gui.dialogue_xpos = 402
# define gui.dialogue_width = 1116

define gui.text_outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ]

init 1001:
    define centered = Character("CenteredKoGa3", what_text_align=0.5)  #"CenteredKoGa3" is a dummy char. and not shown

    define perv = Character('Perv2k16', color="#FFFFFF")
    ###CHARACTERS###
    define bro = ""
    define b = Character ("[bro]", color="#808080")
    define v = Character("Vicky", color="#da70d6")
    define vSide = Character("Vicky", color="#da70d6", image = "vicky", window_left_padding=25)
    define n = Character("Nicole", color="#1e90ff")
    define nSide = Character("Nicole", color="#1e90ff", image = "nicole", window_left_padding=25)
    define j = Character("Julie", color="#228b22")
    define jSide = Character("Julie", color="#228b22", image = "julie", window_left_padding=25)
    define s = Character("Scarlett", color="#DC143C")
    define m = Character("[momUpper]", color="#DAA520")
    define c = Character("Coordinator", color="#2f4f4f")
    define rocco = Character("?????", color="#201345")
    define nacho = Character("?????", color="#ff6e00")

define KoGa3xpos2default = 570
define KoGa3xpos1default = 612
define KoGa3xsize1default = 744
define KoGa3ypos1default = 195
define KoGa3ypos2default = 210
define KoGa3ypos3default = 240
define KoGa3ypos4default = 240
screen say(who, what):
    style_prefix "say"

    if who == "CenteredKoGa3":  #for centered text
        $ persistent.pref_text_size2 = persistent.pref_text_size + 10
        $ KoGa3xpos2 = KoGa3xpos2default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
        $ KoGa3xpos1 = KoGa3xpos1default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
        $ KoGa3xsize1 = KoGa3xsize1default + (12 * persistent.pref_text_size) + (2 * persistent.KoGa3xposOffset)
        if persistent.pref_text_size > 20:
            $ KoGa3ypos1 = KoGa3ypos1default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            $ KoGa3ypos2 = KoGa3ypos2default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            $ KoGa3ypos3 = KoGa3ypos3default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            $ KoGa3ypos4 = KoGa3ypos4default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
        else:
            $ KoGa3ypos1 = KoGa3ypos1default - (6 * 20 + persistent.KoGa3yposOffset)
            $ KoGa3ypos2 = KoGa3ypos2default - (6 * 20 + persistent.KoGa3yposOffset)
            $ KoGa3ypos3 = KoGa3ypos3default - (5 * 20 + persistent.KoGa3yposOffset)
            $ KoGa3ypos4 = KoGa3ypos4default - (5 * 20 + persistent.KoGa3yposOffset)
        text what id "what" xalign 0.5 yalign 0.5 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]

    else:
        window:
            id "window"
            $ persistent.pref_text_size2 = persistent.pref_text_size + 10
            $ KoGa3xpos2 = KoGa3xpos2default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
            $ KoGa3xpos1 = KoGa3xpos1default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
            $ KoGa3xsize1 = KoGa3xsize1default + (12 * persistent.pref_text_size) + (2 * persistent.KoGa3xposOffset)
            if persistent.pref_text_size > 20:
                $ KoGa3ypos1 = KoGa3ypos1default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
                $ KoGa3ypos2 = KoGa3ypos2default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
                $ KoGa3ypos3 = KoGa3ypos3default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
                $ KoGa3ypos4 = KoGa3ypos4default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            else:
                $ KoGa3ypos1 = KoGa3ypos1default - (6 * 20 + persistent.KoGa3yposOffset)
                $ KoGa3ypos2 = KoGa3ypos2default - (6 * 20 + persistent.KoGa3yposOffset)
                $ KoGa3ypos3 = KoGa3ypos3default - (5 * 20 + persistent.KoGa3yposOffset)
                $ KoGa3ypos4 = KoGa3ypos4default - (5 * 20 + persistent.KoGa3yposOffset)

            if who is not None:
                if what != "" and what != None:
                    if KoGa3xpos1 >= 320:
                        window background Transform(Image("textboxHigh.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                    else:
                        window background Transform(Image("textboxHighWide.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                window:
                    id "namebox"
                    style "namebox"
                    if persistent.KoGa3DialogCentered == False:
                        xpos KoGa3xpos2
                    else:
                        xalign 0.5
                    ypos KoGa3ypos2
                    text who id "who" size persistent.pref_text_size2 outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
                if persistent.KoGa3DialogCentered == False:
                    text what id "what" xpos KoGa3xpos1 xsize KoGa3xsize1 ypos KoGa3ypos3 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
                else:
                    text what id "what" xalign 0.5 xsize KoGa3xsize1 ypos KoGa3ypos3 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
            else:
                if what != "" and what != None:
                    if KoGa3xpos1 >= 320:
                        window background Transform(Image("textboxHigh.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                    else:
                        window background Transform(Image("textboxHighWide.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                if persistent.KoGa3DialogCentered == False:
                    text what id "what" xpos KoGa3xpos1 xsize KoGa3xsize1 ypos KoGa3ypos4 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
                else:
                    text what id "what" xalign 0.5 xsize KoGa3xsize1 ypos KoGa3ypos4 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if persistent.KoGa3SideImage is True and KoGa3xpos1 >= 320:
        add SideImage() xalign 0.0 yalign 1.00

define KoGa3TextboxOpacitydefault = 0.0
define KoGa3TextOutline1default = 3                         #Android: 4
define KoGa3TextOutline2default = 0
define KoGa3TextOutline3default = 0
define pref_text_sizedefault = 38                           #Android: 44
define KoGa3xposOffsetdefault = 0
define KoGa3yposOffsetdefault = 0

define persistent.KoGa3TextboxOpacity = KoGa3TextboxOpacitydefault
define persistent.KoGa3TextOutline1 = KoGa3TextOutline1default
define persistent.KoGa3TextOutline2 = KoGa3TextOutline2default
define persistent.KoGa3TextOutline3 = KoGa3TextOutline3default
define persistent.pref_text_size = pref_text_sizedefault
define persistent.KoGa3xposOffset = KoGa3xposOffsetdefault
define persistent.KoGa3yposOffset = KoGa3yposOffsetdefault
define persistent.KoGa3SideImage = True
define persistent.KoGa3OriginalInfoScreen = True
define persistent.KoGa3DialogCentered = False


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background (None)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.0
    xpos 0
    yalign 1.0

style say_dialogue:
    properties gui.text_properties("dialogue")
    xalign 0.0
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    yalign 0.0
    ypos gui.dialogue_ypos


style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt") outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    properties gui.text_properties("input") outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

# screen input(prompt): #only if needed
    # style_prefix "input"
    # window:
        # if renpy.android==True:
            # yalign 0.0
        # vbox:
            # xalign gui.dialogue_text_xalign
            # xpos gui.dialogue_xpos
            # xsize gui.dialogue_width
            # ypos gui.dialogue_ypos
            # text prompt style "input_prompt"
            # input id "input"



#---------------------Choices---------------------#
define KoGa3ChoiceTextSizedefault = 32                      #Android: 36
define KoGa3TextOutline7default = 2
define KoGa3TextOutline8default = 0
define KoGa3TextOutline9default = 0
define KoGa3ChoiceYposdefault = 0
define KoGa3ChoiceButtonWidthdefault = 1100                 #Android: 1300
define persistent.KoGa3ChoiceBackground = True
define persistent.KoGa3ChoiceAlign = "center"
define persistent.KoGa3ChoiceTextSize = KoGa3ChoiceTextSizedefault
define persistent.KoGa3TextOutline7 = KoGa3TextOutline7default
define persistent.KoGa3TextOutline8 = KoGa3TextOutline8default
define persistent.KoGa3TextOutline9 = KoGa3TextOutline9default
define persistent.KoGa3ChoiceYpos = KoGa3ChoiceYposdefault
define persistent.KoGa3ChoiceButtonWidth = KoGa3ChoiceButtonWidthdefault

define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(30, 15, 30, 15)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"

style choice_left is choice
style choice_right is choice
style choice_left_vbox is choice_vbox
style choice_left_button is choice_button
style choice_left_button_text is choice_button_text
style choice_right_vbox is choice_vbox
style choice_right_button is choice_button
style choice_right_button_text is choice_button_text
style choice_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_left_vbox:
    xalign 0.0
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_right_vbox:
    xalign 1.0
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

init 999:
    screen choice(items):

        if persistent.KoGa3ChoiceAlign == "left":
            style_prefix "choice_left"
        elif persistent.KoGa3ChoiceAlign == "right":
            style_prefix "choice_right"
        else:
            style_prefix "choice"
        vbox:
            ypos 1080 - persistent.KoGa3ChoiceYpos - 450                      #550 for ~middle position
            $ gui.choice_button_text_xalign = 0.0
            $ gui.choice_text_xalign = 0.0
            for i in items:
                if persistent.KoGa3ChoiceAlign == "left":
                    $ gui.choice_button_text_xalign = 0.0
                    $ text_xalign_koga3 = 0.0
                elif persistent.KoGa3ChoiceAlign == "right":
                    $ gui.choice_button_text_xalign = 1.0
                    $ text_xalign_koga3 = 1.0
                else:
                    $ gui.choice_button_text_xalign = 0.5
                    $ text_xalign_koga3 = 0.5
                textbutton i.caption:
                    action i.action
                    if persistent.KoGa3ChoiceBackground == False:
                        background None
                    # idle_background "gui/button/choice_idle_background.png"
                    # hover_background "gui/button/choice_hover_background.png"
                    text_outlines [ ( persistent.KoGa3TextOutline7, "#000",  persistent.KoGa3TextOutline8,  persistent.KoGa3TextOutline9) ]
                    text_size persistent.KoGa3ChoiceTextSize
                    xsize persistent.KoGa3ChoiceButtonWidth
                    text_xalign text_xalign_koga3
                    # text_textalign text_xalign_koga3    #works only on newer RenPy versions



#---------------------Quick menu---------------------#
define persistent.KoGa3QuickMenuButton = 1
define persistent.KoGa3QuickMenuShow = 1
define persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
define KoGa3QuickMenuTextSizedefault = 20                   #Android: 25
define KoGa3TextOutline4default = 2
define KoGa3TextOutline5default = 0
define KoGa3TextOutline6default = 0
define persistent.KoGa3QuickMenuTextSize = KoGa3QuickMenuTextSizedefault
define persistent.KoGa3TextOutline4 = KoGa3TextOutline4default
define persistent.KoGa3TextOutline5 = KoGa3TextOutline5default
define persistent.KoGa3TextOutline6 = KoGa3TextOutline6default

define persistent.KoGa3QuickMenuItemBack = True
define persistent.KoGa3QuickMenuItemHist = False
define persistent.KoGa3QuickMenuItemHide = False
define persistent.KoGa3QuickMenuItemSkip = True
define persistent.KoGa3QuickMenuItemAuto = True
define persistent.KoGa3QuickMenuItemSave = True
define persistent.KoGa3QuickMenuItemLoad = True
define persistent.KoGa3QuickMenuItemQSave = True
define persistent.KoGa3QuickMenuItemQLoad = True
define persistent.KoGa3QuickMenuItemPrefs = True
define persistent.KoGa3QuickMenuItemModmenu = True
define persistent.KoGa3QuickMenuIcons = True

define quick_menu = True
init 999:
    screen quick_menu():
        variant ("small", "medium", "large")
        ## Ensure this appears on top of other screens.
        zorder 100
        default p_qm = None #for music addons
        if persistent.KoGa3QuickMenuButton == 2:
            if persistent.KoGa3QuickMenuTextSize >= 28:
                mousearea:
                    area (0, 1000, 1920, 80)
                    hovered SetVariable("persistent.KoGa3QuickMenuShow", 1)
                    unhovered SetVariable("persistent.KoGa3QuickMenuShow", 0)
            else:
                mousearea:
                    area (0, 1040, 1920, 40)
                    hovered SetVariable("persistent.KoGa3QuickMenuShow", 1)
                    unhovered SetVariable("persistent.KoGa3QuickMenuShow", 0)

        if persistent.KoGa3QuickMenuShow == 1:

            if persistent.KoGa3QuickMenuIcons is True:
                hbox:
                    style_prefix "quick"
                    $ persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
                    $ persistent.KoGa3_QuickMenu2_button_font = "KoGa3_QuickMenu2_button_text"
                    xalign 0.5
                    yalign 1.0
                    spacing 0
                    if persistent.KoGa3QuickMenuItemBack:
                        textbutton _("⟲"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Rollback()
                    if persistent.KoGa3QuickMenuItemHist:
                        textbutton _("≡"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('history')
                    if persistent.KoGa3QuickMenuItemHide:
                        textbutton _("▼"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action HideInterface()
                    if persistent.KoGa3QuickMenuItemSkip:
                        textbutton _("►►"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Skip() alternate Skip(fast=True, confirm=True)
                    if persistent.KoGa3QuickMenuItemAuto:
                        if preferences.afm_enable:
                            textbutton _("■"):
                                selected False
                                text_style persistent.KoGa3_QuickMenu1_button_font
                                text_size persistent.KoGa3QuickMenuTextSize
                                text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                action Preference("auto-forward", "toggle")
                        else:
                            textbutton _("►"):
                                text_style persistent.KoGa3_QuickMenu1_button_font
                                text_size persistent.KoGa3QuickMenuTextSize
                                text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                action Preference("auto-forward", "toggle")

                    if persistent.KoGa3QuickMenuItemSave:
                        # textbutton _("➘{size=-2}💾{/size}"): 
                        textbutton _("➘◰"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('save')
                    if persistent.KoGa3QuickMenuItemLoad:
                        # textbutton _("{size=-2}💾{/size}➚"): 
                        textbutton _("◰➚"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('load')
                    if persistent.KoGa3QuickMenuItemQSave:
                        textbutton _("➘Q"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickSave()
                    if persistent.KoGa3QuickMenuItemQLoad:
                        textbutton _("Q➚"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickLoad()
                    if persistent.KoGa3QuickMenuItemPrefs:
                        textbutton _("⇲"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('preferences')
                    if persistent.KoGa3QuickMenuItemModmenu:
                        hbox:
                            spacing 10
                            if KoGa3ModMenuButtonPressed == False:
                                textbutton _("{k=-1.2}Mod{/k}"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [ 
                                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                                    Show("KoGa3GameSettings") ] 

                            if KoGa3ModMenuButtonPressed == True:
                                textbutton _("↓{k=-1.2}Mod{/k}"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [
                                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                                    Hide("KoGa3ScreenCheat"), 
                                    Hide("KoGa3ScreenModMenu"), 
                                    Hide("KoGa3ScreenCheatMore1"), 
                                    Hide("KoGa3ScreenJukebox"), 
                                    Hide("KoGa3QuickMusicMenu"), 
                                    Hide("KoGa3ScreenBlank"), 
                                    Hide("KoGa3ScreenAudioMenu"), 
                                    Hide("KoGa3GameSettingsQuickMenu"), 
                                    Hide("KoGa3GameSettings") ] 

                    if _in_replay:
                        textbutton _("■ {k=-1.2}Replay{/k}"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action EndReplay(confirm=True)
            else:
                hbox:
                    style_prefix "quick"
                    $ persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
                    $ persistent.KoGa3_QuickMenu2_button_font = "KoGa3_QuickMenu2_button_text"
                    xalign 0.5
                    yalign 1.0
                    if persistent.KoGa3QuickMenuItemBack:
                        textbutton _("Back"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Rollback()
                    if persistent.KoGa3QuickMenuItemHist:
                        textbutton _("Hist"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('history')
                    if persistent.KoGa3QuickMenuItemHide:
                        textbutton _("Hide"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action HideInterface()
                    if persistent.KoGa3QuickMenuItemSkip:
                        textbutton _("Skip"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Skip() alternate Skip(fast=True, confirm=True)
                    if persistent.KoGa3QuickMenuItemAuto:
                        textbutton _("Auto"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Preference("auto-forward", "toggle")
                    if persistent.KoGa3QuickMenuItemSave:
                        textbutton _("Save"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('save')
                    if persistent.KoGa3QuickMenuItemLoad:
                        textbutton _("Load"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('load')
                    if persistent.KoGa3QuickMenuItemQSave:
                        textbutton _("Q.Save"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickSave()
                    if persistent.KoGa3QuickMenuItemQLoad:
                        textbutton _("Q.Load"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickLoad()
                    if persistent.KoGa3QuickMenuItemPrefs:
                        textbutton _("Prefs"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('preferences')
                    if persistent.KoGa3QuickMenuItemModmenu:
                        hbox:
                            spacing 10
                            if KoGa3ModMenuButtonPressed == False:
                                textbutton _("Mod menu"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [ 
                                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                                    Show("KoGa3GameSettings") ] 

                            if KoGa3ModMenuButtonPressed == True:
                                textbutton _("Close Mod menu"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [
                                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                                    Hide("KoGa3ScreenCheat"), 
                                    Hide("KoGa3ScreenModMenu"), 
                                    Hide("KoGa3ScreenCheatMore1"), 
                                    Hide("KoGa3ScreenJukebox"), 
                                    Hide("KoGa3QuickMusicMenu"), 
                                    Hide("KoGa3ScreenBlank"), 
                                    Hide("KoGa3ScreenAudioMenu"), 
                                    Hide("KoGa3GameSettingsQuickMenu"), 
                                    Hide("KoGa3GameSettings") ] 

                    if _in_replay:
                        textbutton _("End Replay"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action EndReplay(confirm=True)



#---------------------Named saves---------------------#
define persistent.KoGa3NamedSaves = 1                       #(0 or 2 for Android)
define KoGa3Saveyoffset = -285                              #not used anymore
image KoGa3MenuBack_save = "KoGa3MenuBack_save.png"
label KoGa3NamedSaveInput:                                  #old name input
    show KoGa3MenuBack_save
    $ save_name = renpy.input("Save name: ", default=save_name)
    hide KoGa3MenuBack_save
    return
screen KoGa3Save_Name_Input(slot):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        yalign 0.35                                         #Android: 0.25
        vbox:
            spacing 20
            xsize 600
            if FileLoadable(slot):
                label _("Save name (overwrite):") style "confirm_prompt"
            else:
                label _("Save name (new):") style "confirm_prompt"
            input:
                value VariableInputValue('save_name')
                default save_name
                length 30
                xalign 0.5
            hbox:
                xfill True
                textbutton _("Save") action FileAction(slot, confirm=False), Hide("KoGa3Save_Name_Input") xalign 0.5
                textbutton _("Cancel") action Hide("KoGa3Save_Name_Input") xalign 0.5
    key "game_menu" action Hide("KoGa3Save_Name_Input")
    ## Right-click and escape answer "no".
    ## Return of Enter answer "yes".
    key "K_RETURN" action FileAction(slot, confirm=False), Hide("KoGa3Save_Name_Input")
    key "K_KP_ENTER" action FileAction(slot, confirm=False), Hide("KoGa3Save_Name_Input")

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:


            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                ypos -175
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    if persistent.KoGa3NamedSaves == 2 and title == "Save":
                        button:
                            action Show("KoGa3Save_Name_Input", slot=slot)

                            add FileScreenshot(slot) xalign 0.5

                            vbox:
                                xalign 0.5
                                yalign 1.0
                                text FileTime(slot, format=_("{#file_time}%a, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"
                                    size 23

                                text FileSaveName(slot):
                                    style "slot_name_text"
                                    size 23

                            if FileLoadable(slot):
                                imagebutton:
                                    idle "button_delete_idle.png"
                                    hover "button_delete_hover.png"

                                    action FileDelete(slot)

                                    xalign 1.0
                                    xoffset 10
                                    yalign -0.02

                            key "save_delete" action FileDelete(slot)

                    else:
                        button:
                            action FileAction(slot)

                            add FileScreenshot(slot) xalign 0.5

                            vbox:
                                xalign 0.5
                                yalign 1.0
                                text FileTime(slot, format=_("{#file_time}%a, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"
                                    size 23

                                text FileSaveName(slot):
                                    style "slot_name_text"
                                    size 23

                            if FileLoadable(slot):
                                imagebutton:
                                    idle "button_delete_idle.png"
                                    hover "button_delete_hover.png"

                                    action FileDelete(slot)

                                    xalign 1.0
                                    xoffset 10
                                    yalign -0.02

                            key "save_delete" action FileDelete(slot)

            if title == "Save":
                vbox:
                    xpos 70
                    ypos -10
                    hbox:
                        textbutton _("Named saves: "):
                            text_size 32
                            sensitive False
                            action NullAction()
                        if persistent.KoGa3NamedSaves == 1:
                            textbutton _("ON - input field (best for PC)"):
                                text_size 32
                                selected False
                                action [ 
                                SetVariable("persistent.KoGa3NamedSaves", 2) ]
                        if persistent.KoGa3NamedSaves == 2:
                            textbutton _("ON - get asked (best for Android)"):
                                text_size 32
                                selected False
                                action [ 
                                SetVariable("persistent.KoGa3NamedSaves", 0),
                                SetVariable("save_name","") ]
                        if persistent.KoGa3NamedSaves == 0:
                            textbutton _("OFF"):
                                text_size 32
                                selected False
                                action [ 
                                SetVariable("persistent.KoGa3NamedSaves", 1)]

                    if persistent.KoGa3NamedSaves > 0:
                        hbox:
                            textbutton _("current: "):
                                ypos 0
                                text_size 32
                                sensitive False
                                action NullAction()
                            if persistent.KoGa3NamedSaves == 1:
                                button:
                                    key_events True
                                    ypos -2

                                    input:
                                        font "KoGa3.ttf"
                                        size 32
                                        value VariableInputValue('save_name')
                                        color "#8e6439"
                            if persistent.KoGa3NamedSaves == 2:
                                textbutton _("[save_name]"):
                                    text_size 32
                                    sensitive False
                                    action NullAction()

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()



#---------------------Preferences adds---------------------#
screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                    #=====================================KoGa3 additions====================================#
                    null height (4 * gui.pref_spacing)
                    label _("Mod KoGa3")
                    textbutton _("Settings..."):
                        sensitive True
                        action [
                        Show("KoGa3ScreenBlank"),
                        Show("KoGa3GameSettings") ]
                    #=====================================KoGa3 additions====================================#

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"