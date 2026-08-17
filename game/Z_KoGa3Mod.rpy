#Mod for the game "Family Matters" / KoGa3#

#---------------------general Mod audio settings---------------------#
# define persistent.KoGa3main_menu_music = True
# init 999 python:
    # config.has_music = True

#---------------------setting default audio volumes to 0.5---------------------#
init python:
    config.default_music_volume = 0.5
    config.default_sfx_volume = 0.5
    config.default_voice_volume = 0.5

    # if persistent.KoGa3main_menu_music is True:
        # config.main_menu_music = "/music/XXXX.mp3"
    # else:
        # config.main_menu_music = "<silence 0.5>"
        # renpy.music.stop(channel=u'music', fadeout=None)

    # # needed for jukebox player
    # def convert_float_into_time(t):
        # i, f = divmod(t, 1)
        # i = int(i)
        # m, s = divmod(i, 60)
        # h, m = divmod(m, 60)
        # return "{:02}:{:02}".format(m, s)

    # # new audio channel for the game      #not used for this game
    # renpy.music.register_channel("music1", mixer="voice")
    # renpy.music.register_channel("sound1", mixer="sfx")
    # renpy.music.register_channel("sound2", mixer="sfx")


#---------------------shortcut key for Mod menu screen---------------------#
init python:
    # short key: Shift + k.
    config.keymap['KoGa3GameSettings'] = "shift_K_k"
define config.overlay_screens = ["keymap", "quick_menu"]
screen keymap:
    key "KoGa3GameSettings":
        action [ 
        SetVariable ("KoGa3ModMenuButtonPressed", True),
        Show("KoGa3GameSettings") ] 


#---------------------Textbutton / Colors---------------------#
init python:

    style.KoGa3_text.font = "KoGa3.ttf"     #insensitive
    style.KoGa3_text.color = "#c4aead"      #"#808080" "#ffffff"
    style.KoGa3_text.size = 30
    #style.KoGa3_text.line_spacing = 30
    style.KoGa3_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_1_text.font = "KoGa3.ttf"   #selected 1
    style.KoGa3_1_text.color = "#c4aead"    #"#808080" "#ffffff"
    style.KoGa3_1_text.size = 30
    #style.KoGa3_1_text.line_spacing = 30
    style.KoGa3_1_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]        #Android: 4

    style.KoGa3_1a_text.font = "KoGa3.ttf"   #selected 1
    style.KoGa3_1a_text.color = "#c4aead"    #"#808080" "#ffffff"
    style.KoGa3_1a_text.size = 28
    #style.KoGa3_1a_text.line_spacing = 28
    style.KoGa3_1a_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]       #Android: 4

    style.KoGa3_2_text.font = "KoGa3.ttf"   #selected 2
    style.KoGa3_2_text.color = "#ffffff"    #"#808080" "#ffffff"
    style.KoGa3_2_text.size = 30
    style.KoGa3_2_text.line_spacing = 30
    style.KoGa3_2_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]


    style.KoGa3_button_text.font = "KoGa3.ttf"
    style.KoGa3_button_text.color = "#87cefa"    #"#808080" "#ffffff"
    style.KoGa3_button_text.hover_color = "#c90016"
    style.KoGa3_button_text.selected_color = "#ffff00"
    style.KoGa3_button_text.insensitive_color = "#c4aead"
    style.KoGa3_button_text.size = 30
    style.KoGa3_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_1_button_text.font = "KoGa3.ttf"
    style.KoGa3_1_button_text.color = "#87cefa"
    style.KoGa3_1_button_text.hover_color = "#c90016"
    style.KoGa3_1_button_text.selected_color = "#ffff00"
    style.KoGa3_1_button_text.insensitive_color = "#c4aead"
    style.KoGa3_1_button_text.size = 30
    style.KoGa3_1_button_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]   #Android: 4

    style.KoGa3_1a_button_text.font = "KoGa3.ttf"
    style.KoGa3_1a_button_text.color = "#87cefa"
    style.KoGa3_1a_button_text.hover_color = "#c90016"
    style.KoGa3_1a_button_text.selected_color = "#ffff00"
    style.KoGa3_1a_button_text.insensitive_color = "#c4aead"
    style.KoGa3_1a_button_text.size = 28
    style.KoGa3_1a_button_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]  #Android: 4


    style.KoGa3_QuickMusic1_button_text.font = "KoGa3.ttf"
    style.KoGa3_QuickMusic1_button_text.color = "#87cefa"    #"#808080" "#ffffff"
    style.KoGa3_QuickMusic1_button_text.hover_color = "#c90016"
    style.KoGa3_QuickMusic1_button_text.selected_color = "#ffff00"  #"#ffffff"
    style.KoGa3_QuickMusic1_button_text.insensitive_color = "#c4aead"
    style.KoGa3_QuickMusic1_button_text.size = 25
    style.KoGa3_QuickMusic1_button_text.outlines = [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_QuickMenu1_button_text.font = "KoGa3.ttf"
    style.KoGa3_QuickMenu1_button_text.color = "#ffffff"
    style.KoGa3_QuickMenu1_button_text.hover_color = "#87cefa"
    style.KoGa3_QuickMenu1_button_text.selected_color = "#ffffff"
    style.KoGa3_QuickMenu1_button_text.insensitive_color = "#a9a9a9"
    #style.KoGa3_QuickMenu1_button_text.size = 22
    style.KoGa3_QuickMenu1_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_QuickMenu2_button_text.font = "KoGa3.ttf"
    style.KoGa3_QuickMenu2_button_text.color = "#ffffff"
    style.KoGa3_QuickMenu2_button_text.hover_color = "#87cefa"
    style.KoGa3_QuickMenu2_button_text.selected_color = "#ffffff"
    style.KoGa3_QuickMenu2_button_text.insensitive_color = "#a9a9a9"
    #style.KoGa3_QuickMenu2_button_text.size = 22
    #style.KoGa3_QuickMenu2_button_text.outlines = [ (absolute(1), "#000000", absolute(0), absolute(0)) ]


    #buttons 2-5 for the info screen
    style.KoGa3_2_button_text.font = "KoGa3.ttf"
    style.KoGa3_2_button_text.color = "#ff9999"
    style.KoGa3_2_button_text.hover_color = "#800000"
    style.KoGa3_2_button_text.selected_color = "#ff9999"
    style.KoGa3_2_button_text.size = 25
    style.KoGa3_2_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_3_button_text.font = "KoGa3.ttf"
    style.KoGa3_3_button_text.color = "#98fb98"
    style.KoGa3_3_button_text.hover_color = "#2a8000"
    style.KoGa3_3_button_text.selected_color = "#98fb98"
    style.KoGa3_3_button_text.size = 25
    style.KoGa3_3_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_4_button_text.font = "KoGa3.ttf"
    style.KoGa3_4_button_text.color = "#87cefa"
    style.KoGa3_4_button_text.hover_color = "#0000cd"
    style.KoGa3_4_button_text.selected_color = "#87cefa"
    style.KoGa3_4_button_text.size = 25
    style.KoGa3_4_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_5_button_text.font = "KoGa3.ttf"
    style.KoGa3_5_button_text.color = "#ffffff"
    style.KoGa3_5_button_text.hover_color = "#696969"
    style.KoGa3_5_button_text.selected_color = "#ffffff"
    style.KoGa3_5_button_text.size = 25
    style.KoGa3_5_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

default KoGa3_status_button_text = "KoGa3_5_button_text"
define KoGa3ButtonTextSize01 = 470
define KoGa3ButtonTextSize02 = 95
define KoGa3ButtonTextSize03 = 110

define KoGa3ButtonTextSize04 = 695
define KoGa3ButtonTextSize05 = 195

define KoGa3ButtonTextSize06 = 250
define KoGa3ButtonTextSize07 = 115
define KoGa3ButtonTextSize08 = 100

define KoGa3Color1 = "#c4aead"
define KoGa3Color2 = "#ffff00"
define KoGa3Color3 = "#ffffff"

#---------------------blank screen---------------------#
screen KoGa3ScreenBlank:
    add "/KoGa3MenuBack.png"
    modal True


#---------------------Name change---------------------#
label KoGa3NameChange:
    menu:
        "MC first name: {color=[KoGa3Color2]}[bro]{/color}":
            $ bro = renpy.input("What is your first name?", default=bro)
            $ bro = bro.strip()
            jump KoGa3NameChange
        "Julie (18 years) is your: {color=[KoGa3Color2]}[sis]{/color}":
            $ sis = renpy.input("her relationship to you? (typing {color=#228b22}sis{/color} enables incest)", default=sis)
            $ sis = sis.strip()
            $ sis = sis.lower()
            if (sis == "sis") or (sis == "sister"):
                $ incestEnabled = 2
                $ family = "family"
                $ mom = "mom"
                $ momUpper = "MOM"
                $ sis = "sister"
                $ son = "son"
                $ daughter = "daughter"
                $ brother = "brother"
                $ siblings = "siblings"
                $ children = "children"
                $ father = "father"
            else:
                $ incestEnabled = 0
                $ family = "household"
                $ mom = "landlady"
                $ momUpper = "LANDLADY"
                $ sis = "housemate"
                $ son = "tenant"
                $ daughter = "tenant"
                $ brother = "housemate"
                $ siblings = "roommates"
                $ children = "tenants"
                $ father = "landlord"
            jump KoGa3NameChange
        "Roxanne (44 years) is your: {color=[KoGa3Color2]}[mom]{/color}":
            $ mom = renpy.input("her relationship to you? (typing {color=#228b22}mom{/color} enables incest)", default=mom)
            $ mom = mom.strip()
            $ mom = mom.lower()
            if (mom == "mom") or (mom == "mother"):
                $ incestEnabled = 2
                $ family = "family"
                $ mom = "mom"
                $ momUpper = "MOM"
                $ sis = "sister"
                $ son = "son"
                $ daughter = "daughter"
                $ brother = "brother"
                $ siblings = "siblings"
                $ children = "children"
                $ father = "father"
            else:
                $ incestEnabled = 0
                $ family = "household"
                $ mom = "landlady"
                $ momUpper = "LANDLADY"
                $ sis = "housemate"
                $ son = "tenant"
                $ daughter = "tenant"
                $ brother = "housemate"
                $ siblings = "roommates"
                $ children = "tenants"
                $ father = "landlord"
        "Done":
            hide screen KoGa3ScreenBlank
            show screen KoGa3GameSettings
            pause
            return


#---------------------add. game settings---------------------#
screen KoGa3GameSettings:
    if not main_menu:
        add "/KoGa3MenuBack_settings.png"
    modal True
    vbox:
        xalign 0.5
        spacing -12
        null height (34)

        if _menu:
            if renpy.variant("touch"):
                textbutton _("━━━━━━━━━━━━━ Hardware settings ━━━━━━━━━━━━━━"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()
                hbox:
                    hbox:
                        xsize 350
                        textbutton ("Performance Mode:"):
                            text_style "KoGa3_1a_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize 150
                        textbutton _("ON "):
                            text_style "KoGa3_1a_button_text"
                            action Preference("gl powersave", True)
                    hbox:
                        xsize 150
                        textbutton _("OFF"):
                            text_style "KoGa3_1a_button_text"
                            action Preference("gl powersave", False)
                    hbox:
                        textbutton _("Auto"):
                            text_style "KoGa3_1a_button_text"
                            action Preference("gl powersave", "auto")

                null height (25)

                hbox:
                    hbox:
                        xsize 350
                        textbutton ("Video Mode:"):
                            text_style "KoGa3_1a_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize 235
                        textbutton _("Hardware"):
                            text_style "KoGa3_1a_button_text"
                            action SetVariable("config.hw_video", True)
                    hbox:
                        textbutton _("Software"):
                            text_style "KoGa3_1a_button_text"
                            action SetVariable("config.hw_video", False)

            else:
                textbutton _("━━━━━━━━━━━━━━━ Mod settings ━━━━━━━━━━━━━━━━"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()

            null height (35)


        #################################################################################
        if not _menu:
            textbutton _("━━━━━━━━━━━━━━━━━ Mod menu ━━━━━━━━━━━━━━━━━"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()
            # hbox:
                # hbox:
                    # xsize 245
                    # textbutton ("Music Mod: "):
                        # text_style "KoGa3_1a_button_text"
                        # sensitive False
                        # action NullAction()
                # hbox:
                    # xsize 240
                    # if KoGa3Music == 1:
                        # textbutton _("ON "):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [ 
                            # Stop ("music"), 
                            # Stop ("music1"), 
                            # Play("music", KoGa3CurrentMusic), 
                            # SetVariable("KoGa3Music", 1) ]
                    # if KoGa3Music == 2:
                        # textbutton _("OFF"):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [ 
                            # Stop ("music"), 
                            # Stop ("music1"), 
                            # SetVariable("KoGa3Music", 2) ]

                # textbutton _("Music Jukebox..."):
                    # text_style "KoGa3_1a_button_text"
                    # selected False
                    # sensitive True
                    # action [ 
                    # Hide("KoGa3GameSettings"),
                    # Show("KoGa3ScreenJukebox") ]

            #################################################################################

            hbox:
                textbutton ("Game progress (info):  [KoGa3GameProgress]"):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
            null height (15)

            hbox:
                hbox:
                    xsize 225
                    textbutton ("Choice hints:"):
                        text_style "KoGa3_1a_button_text"
                        sensitive False
                        action NullAction()
                hbox:
                    xsize 260
                    if KoGa3ChoiceOption == 0:
                        textbutton _("OFF"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable ("wty", "\n{color=#0f0}recommended{/color}"),       #old WT
                            SetVariable ("wtn", "\n{color=#f00}not recommended{/color}"),
                            SetVariable ("wtb", "\n{color=#FF0000}bad choice{/color}"),
                            SetVariable ("wtm", "\n{color=#0000FF}mod choice{/color}"),
                            SetVariable ("wtne", "\n{color=#80CBC4}not essential{/color}"),
                            SetVariable ("wt1", "\n{color=#BD95E2}1st{/color}"),
                            SetVariable ("wt2", "\n{color=#BD95E2}2nd{/color}"),
                            SetVariable ("wt3", "\n{color=#BD95E2}3rd{/color}"),
                            SetVariable ("wt4", "\n{color=#BD95E2}4th{/color}"),
                            SetVariable ("wtl", "\n{color=#BD95E2}last{/color}"),
                            SetVariable ("wtr", "\n{color=#995cd1}repeat{/color}"),
                            SetVariable ("wtharem", "\n{color=#FF69B4}harem route{/color}"),
                            SetVariable ("wtromance", "\n{color=#FFA500}romance route{/color}"),
                            SetVariable ("wtntr", "\n{color=#FF125B8D}ntr route{/color}"),
                            SetVariable ("wtswing", "\n{color=#FF125B8D}swinging route{/color}"),
                            SetVariable ("wtshar", "\n{color=#FF125B8D}sharing route{/color}"),
                            SetVariable ("wtymc", "\n{color=#0f0}recommended/more content{/color}"),
                            SetVariable ("KoGa3ChoiceOption", 1),
                            SetVariable ("KoGa3WTChange", "\n{color=#008000}"),
                            SetVariable ("KoGa3WTChange1", "\n{color=#ffdf00}"),
                            SetVariable ("KoGa3WTChange2", "\n{color=#ff0000}") ]
                    else:
                        textbutton _("ON "):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable ("wty", ""),    #old WT
                            SetVariable ("wtn", ""),
                            SetVariable ("wtb", ""),
                            SetVariable ("wtm", ""),
                            SetVariable ("wtne", ""),
                            SetVariable ("wt1", ""),
                            SetVariable ("wt2", ""),
                            SetVariable ("wt3", ""),
                            SetVariable ("wt4", ""),
                            SetVariable ("wtl", ""),
                            SetVariable ("wtr", ""),
                            SetVariable ("wtharem", ""),
                            SetVariable ("wtromance", ""),
                            SetVariable ("wtntr", ""),
                            SetVariable ("wtswing", ""),
                            SetVariable ("wtshar", ""),
                            SetVariable ("wtymc", ""),
                            SetVariable ("KoGa3ChoiceOption", 0),
                            SetVariable ("KoGa3WTChange", "{alt}"),
                            SetVariable ("KoGa3WTChange1", "{alt}"),
                            SetVariable ("KoGa3WTChange2", "{alt}")]

                textbutton _("Change name/rels..."):
                    text_style "KoGa3_1a_button_text"
                    selected False
                    action [
                    Hide("KoGa3GameSettings"),
                    Show("KoGa3ScreenBlank"),
                    Call("KoGa3NameChange") ]

            null height (35)

        #################################################################################

        hbox:
            hbox:
                xsize 50
                if KoGa3DialogOptions == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3DialogOptions", 1),
                        SetVariable("KoGa3ChoiceOptions", 0),
                        SetVariable("KoGa3QuickMenuOptions", 0) ]

                if KoGa3DialogOptions == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action SetVariable("KoGa3DialogOptions", 0)
            hbox:
                #######################################
                $ KoGa3TextboxOpacityPercent = int(persistent.KoGa3TextboxOpacity * 100)
                if persistent.KoGa3TextboxOpacity == KoGa3TextboxOpacitydefault and persistent.pref_text_size == pref_text_sizedefault and persistent.KoGa3xposOffset == KoGa3xposOffsetdefault and persistent.KoGa3yposOffset == KoGa3yposOffsetdefault and persistent.KoGa3TextOutline1 == KoGa3TextOutline1default and persistent.KoGa3TextOutline2 == KoGa3TextOutline2default and persistent.KoGa3TextOutline3 == KoGa3TextOutline3default and persistent.KoGa3DialogCentered == False:
                    textbutton _("{color=[KoGa3Color1]}──────────── Dialog settings ──────────────"):
                        text_style "KoGa3_1_button_text"
                        if KoGa3DialogOptions == 0:
                            action [
                            SetVariable("KoGa3DialogOptions", 1),
                            SetVariable("KoGa3ChoiceOptions", 0),
                            SetVariable("KoGa3QuickMenuOptions", 0) ]
                        if KoGa3DialogOptions == 1:
                            action SetVariable("KoGa3DialogOptions", 0)
                else:
                    hbox:
                        textbutton _("{color=[KoGa3Color1]}──────────── Dialog settings ──────"):
                            text_style "KoGa3_1_button_text"
                            if KoGa3DialogOptions == 0:
                                action [
                                SetVariable("KoGa3DialogOptions", 1),
                                SetVariable("KoGa3ChoiceOptions", 0),
                                SetVariable("KoGa3QuickMenuOptions", 0) ]
                            if KoGa3DialogOptions == 1:
                                action SetVariable("KoGa3DialogOptions", 0)
                        textbutton _("(reset)"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable("persistent.KoGa3TextboxOpacity", KoGa3TextboxOpacitydefault),
                            SetVariable("persistent.pref_text_size", pref_text_sizedefault),
                            SetVariable("persistent.KoGa3xposOffset", KoGa3xposOffsetdefault),
                            SetVariable("persistent.KoGa3yposOffset", KoGa3yposOffsetdefault),
                            SetVariable("persistent.KoGa3TextOutline1", KoGa3TextOutline1default),
                            SetVariable("persistent.KoGa3TextOutline2", KoGa3TextOutline2default),
                            SetVariable("persistent.KoGa3TextOutline3", KoGa3TextOutline3default),
                            SetVariable("persistent.KoGa3DialogCentered", False),
                            SetVariable("persistent.KoGa3DialogOptions", 1),
                            SetVariable("persistent.KoGa3QuickMenuButton", 1),
                            SetVariable("persistent.KoGa3QuickMenuShow", 1)]

        #################################################################################

        if KoGa3DialogOptions == 1:
            hbox:
                hbox:
                    xsize 50
                hbox:
                    vbox:
                        spacing -8
                        hbox:
                            text _("Dialogue box opacity  (current: [KoGa3TextboxOpacityPercent]%)"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(persistent, "KoGa3TextboxOpacity", range=1.0, style="slider")

                        null height (25)

                        hbox:
                            text _("Dialogue box horizontal size offset (current: [persistent.KoGa3xposOffset])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3xposOffset', range=600, max_is_zero=False, style=u'slider', offset=-300, step=1)

                        hbox:
                            text _("Dialogue box vertical offset (current: [persistent.KoGa3yposOffset])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3yposOffset', range=500, max_is_zero=False, style=u'slider', offset=-200, step=1)

                        null height (25)

                        hbox:
                            text _("Dialogue text font size  (current: [persistent.pref_text_size]/75)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='pref_text_size', range=75, max_is_zero=False, style=u'slider', offset=0, step=1)

                        hbox:
                            text _("Dialogue text font outline  (current: [persistent.KoGa3TextOutline1]/10)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(persistent, "KoGa3TextOutline1", range=10, style="slider")

                        hbox:
                            hbox:
                                text _("   offset horizontal ([persistent.KoGa3TextOutline2])       offset vertical ([persistent.KoGa3TextOutline3])"):
                                    style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline2", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline3", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)

                        hbox:
                            text _("Dialog alignment/position:"):
                                style "KoGa3_1a_button_text"
                            if persistent.KoGa3DialogCentered == False:
                                textbutton _("Left"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3DialogCentered", True)
                            else:
                                textbutton _("Center"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3DialogCentered", False)

                        null height (25)

        #################################################################################

        hbox:
            hbox:
                xsize 50
                if KoGa3ChoiceOptions == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3DialogOptions", 0),
                        SetVariable("KoGa3ChoiceOptions", 1),
                        SetVariable("KoGa3QuickMenuOptions", 0) ]
                if KoGa3ChoiceOptions == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action SetVariable("KoGa3ChoiceOptions", 0)
            hbox:
                #######################################
                if persistent.KoGa3ChoiceTextSize == KoGa3ChoiceTextSizedefault and persistent.KoGa3TextOutline7 == KoGa3TextOutline7default and persistent.KoGa3TextOutline8 == KoGa3TextOutline8default and persistent.KoGa3TextOutline9 == KoGa3TextOutline9default and persistent.KoGa3ChoiceYpos == KoGa3ChoiceYposdefault and persistent.KoGa3ChoiceButtonWidth == KoGa3ChoiceButtonWidthdefault and persistent.KoGa3ChoiceBackground == True and persistent.KoGa3ChoiceAlign == "center":
                    textbutton _("{color=[KoGa3Color1]}──────────── Choice settings ──────────────"):
                        text_style "KoGa3_1_button_text"
                        if KoGa3ChoiceOptions == 0:
                            action [
                            SetVariable("KoGa3DialogOptions", 0),
                            SetVariable("KoGa3ChoiceOptions", 1),
                            SetVariable("KoGa3QuickMenuOptions", 0) ]
                        if KoGa3ChoiceOptions == 1:
                            action SetVariable("KoGa3ChoiceOptions", 0)
                else:
                    hbox:
                        textbutton _("{color=[KoGa3Color1]}──────────── Choice settings ──────"):
                            text_style "KoGa3_1_button_text"
                            if KoGa3ChoiceOptions == 0:
                                action [
                                SetVariable("KoGa3DialogOptions", 0),
                                SetVariable("KoGa3ChoiceOptions", 1),
                                SetVariable("KoGa3QuickMenuOptions", 0) ]
                            if KoGa3ChoiceOptions == 1:
                                action SetVariable("KoGa3ChoiceOptions", 0)
                        textbutton _("(reset)"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable("persistent.KoGa3ChoiceTextSize", KoGa3ChoiceTextSizedefault),
                            SetVariable("persistent.KoGa3TextOutline7", KoGa3TextOutline7default),
                            SetVariable("persistent.KoGa3TextOutline8", KoGa3TextOutline8default),
                            SetVariable("persistent.KoGa3TextOutline9", KoGa3TextOutline9default),
                            SetVariable("persistent.KoGa3ChoiceYpos", KoGa3ChoiceYposdefault),
                            SetVariable("persistent.KoGa3ChoiceButtonWidth", KoGa3ChoiceButtonWidthdefault),
                            SetVariable("persistent.KoGa3ChoiceBackground", True),
                            SetVariable("persistent.KoGa3ChoiceAlign", "center") ]

        #################################################################################

        if KoGa3ChoiceOptions == 1:
            hbox:
                hbox:
                    xsize 50
                hbox:
                    vbox:
                        spacing -8

                        hbox:
                            text _("Choice box vertical offset (current: [persistent.KoGa3ChoiceYpos])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3ChoiceYpos', range=1080, max_is_zero=False, style=u'slider', offset=-450, step=1)

                        hbox:
                            text _("Choice box horizontal size (current: [persistent.KoGa3ChoiceButtonWidth])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3ChoiceButtonWidth', range=1800, max_is_zero=False, style=u'slider', offset=0, step=1)

                        null height (25)

                        hbox:
                            text _("Choice text font size  (current: [persistent.KoGa3ChoiceTextSize]/75)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3ChoiceTextSize', range=75, max_is_zero=False, style=u'slider', offset=0, step=1)

                        hbox:
                            text _("Choice text font outline  (current: [persistent.KoGa3TextOutline7]/10)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(persistent, "KoGa3TextOutline7", range=10, style="slider")

                        hbox:
                            hbox:
                                text _("   offset horizontal ([persistent.KoGa3TextOutline8])       offset vertical ([persistent.KoGa3TextOutline9])"):
                                    style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline8", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline9", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)

                        hbox:
                            text _("Choice background:"):
                                style "KoGa3_1a_button_text"
                            if persistent.KoGa3ChoiceBackground == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceBackground", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceBackground", False)

                        hbox:
                            text _("Choice button alignment:"):
                                style "KoGa3_1a_button_text"
                            if persistent.KoGa3ChoiceAlign == "right":
                                textbutton _("Right"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceAlign", "left")
                            if persistent.KoGa3ChoiceAlign == "left":
                                textbutton _("Left"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceAlign", "center")
                            if persistent.KoGa3ChoiceAlign == "center":
                                textbutton _("Center"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceAlign", "right")

                        null height (25)

        #################################################################################

        hbox:
            hbox:
                xsize 50
                if KoGa3QuickMenuOptions == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3DialogOptions", 0),
                        SetVariable("KoGa3ChoiceOptions", 0),
                        SetVariable("KoGa3QuickMenuOptions", 1) ]
                if KoGa3QuickMenuOptions == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3QuickMenuOptions", 0) ]
            hbox:
                if KoGa3QuickMenuOptions == 0:
                    textbutton _("{color=[KoGa3Color1]}────────── Quick menu settings ────────────"):
                        text_style "KoGa3_1_button_text"
                        action [
                        SetVariable("KoGa3DialogOptions", 0),
                        SetVariable("KoGa3ChoiceOptions", 0),
                        SetVariable("KoGa3QuickMenuOptions", 1) ]
                if KoGa3QuickMenuOptions == 1:
                    textbutton _("{color=[KoGa3Color1]}────────── Quick menu settings ────────────"):
                        text_style "KoGa3_1_button_text"
                        action [
                        SetVariable("KoGa3QuickMenuOptions", 0) ]

        #################################################################################

        if KoGa3QuickMenuOptions == 1:
            hbox:
                hbox:
                    xsize 50
                hbox:
                    vbox:
                        spacing -10
                        hbox:
                            hbox:
                                xsize 340
                                textbutton _("Quick menu:"):
                                    text_style "KoGa3_1a_button_text"
                                    sensitive False
                                    action NullAction()
                            hbox:
                                xsize 150
                                if persistent.KoGa3QuickMenuButton == 1:
                                    textbutton _("ON "):
                                        text_style "KoGa3_1a_button_text"
                                        selected True
                                        action NullAction()
                                else:
                                    textbutton _("ON "):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [ 
                                        SetVariable("persistent.KoGa3QuickMenuButton", 1),
                                        SetVariable("persistent.KoGa3QuickMenuShow", 1) ]
                            hbox:
                                xsize 150
                                if persistent.KoGa3QuickMenuButton == 2:
                                    textbutton _("Auto"):
                                        text_style "KoGa3_1a_button_text"
                                        selected True
                                        action NullAction()
                                else:
                                    textbutton _("Auto"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [ 
                                        SetVariable("persistent.KoGa3QuickMenuButton", 2),
                                        SetVariable("persistent.KoGa3QuickMenuShow", 0) ]
                            hbox:
                                if persistent.KoGa3QuickMenuButton == 0:
                                    textbutton _("OFF"):
                                        text_style "KoGa3_1a_button_text"
                                        selected True
                                        action NullAction()
                                else:
                                    textbutton _("OFF"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [ 
                                        SetVariable("persistent.KoGa3QuickMenuButton", 0),
                                        SetVariable("persistent.KoGa3QuickMenuShow", 0) ]
                        null height 10
                        hbox:
                            hbox:
                                xsize 340
                                textbutton _("Quick menu buttons:"):
                                    text_style "KoGa3_1a_button_text"
                                    sensitive False
                                    action NullAction()
                            hbox:
                                #xsize 200
                                if persistent.KoGa3QuickMenuIcons is True:
                                    textbutton _("Icons"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [
                                        SetVariable ("persistent.KoGa3QuickMenuIcons", False)]
                                else:
                                    textbutton _("Text"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [
                                        SetVariable ("persistent.KoGa3QuickMenuIcons", True)]
                        null height 15
                        hbox:
                            hbox:
                                textbutton _("More Quick menu settings..."):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    sensitive True
                                    action [ 
                                    Hide("KoGa3GameSettings"),
                                    Show("KoGa3GameSettingsQuickMenu") ]

        textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()
        if main_menu is True or KoGa3ModMenuButtonPressed is False:
            hbox:
                spacing 30
                textbutton _("Back"):
                    text_style "KoGa3_1_button_text"
                    sensitive True
                    action [
                    Hide("KoGa3GameSettings"), 
                    Hide("KoGa3ScreenBlank") ]
        else:
            hbox:
                spacing 30
                # textbutton _("Back"):
                    # text_style "KoGa3_1_button_text"
                    # sensitive True
                    # action [
                    # Hide("KoGa3GameSettings"), 
                    # Hide("KoGa3ScreenBlank"), 
                    # Show("KoGa3ScreenModMenu") ]
                textbutton _("Close"):
                    text_style "KoGa3_1_button_text"
                    selected False
                    action [
                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                    Hide("KoGa3GameSettings"), 
                    Hide("KoGa3ScreenBlank") ]


#---------------------add. game settings Quick Menu---------------------#
screen KoGa3GameSettingsQuickMenu:
    if not main_menu:
        add "/KoGa3MenuBack_settings.png"
    modal True
    vbox:
        xalign 0.5
        spacing -12
        null height (34)

        if persistent.KoGa3TextOutline4 == KoGa3TextOutline4default and persistent.KoGa3TextOutline5 == KoGa3TextOutline5default and persistent.KoGa3TextOutline6 == KoGa3TextOutline6default and persistent.KoGa3QuickMenuTextSize == KoGa3QuickMenuTextSizedefault:
            textbutton _("━━━━━━━━━━ More Quick menu settings ━━━━━━━━━━"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()
        else:
            hbox:
                textbutton _("━━━━━━━━━━ More Quick menu settings ━━━"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()
                textbutton _("(reset)"):
                    text_style "KoGa3_1_button_text"
                    selected False
                    action [
                    SetVariable("persistent.KoGa3TextOutline4", KoGa3TextOutline4default),
                    SetVariable("persistent.KoGa3TextOutline5", KoGa3TextOutline5default),
                    SetVariable("persistent.KoGa3TextOutline6", KoGa3TextOutline6default),
                    SetVariable("persistent.KoGa3QuickMenuTextSize", KoGa3QuickMenuTextSizedefault) ]

        vbox:
            spacing -12
            hbox:
                hbox:
                    xsize 340
                    textbutton _("Quick menu:"):
                        text_style "KoGa3_1a_button_text"
                        sensitive False
                        action NullAction()
                hbox:
                    xsize 150
                    if persistent.KoGa3QuickMenuButton == 1:
                        textbutton _("ON "):
                            text_style "KoGa3_1a_button_text"
                            selected True
                            action NullAction()
                    else:
                        textbutton _("ON "):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [ 
                            SetVariable("persistent.KoGa3QuickMenuButton", 1),
                            SetVariable("persistent.KoGa3QuickMenuShow", 1) ]
                hbox:
                    xsize 150
                    if persistent.KoGa3QuickMenuButton == 2:
                        textbutton _("Auto"):
                            text_style "KoGa3_1a_button_text"
                            selected True
                            action NullAction()
                    else:
                        textbutton _("Auto"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [ 
                            SetVariable("persistent.KoGa3QuickMenuButton", 2),
                            SetVariable("persistent.KoGa3QuickMenuShow", 0) ]
                hbox:
                    if persistent.KoGa3QuickMenuButton == 0:
                        textbutton _("OFF"):
                            text_style "KoGa3_1a_button_text"
                            selected True
                            action NullAction()
                    else:
                        textbutton _("OFF"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [ 
                            SetVariable("persistent.KoGa3QuickMenuButton", 0),
                            SetVariable("persistent.KoGa3QuickMenuShow", 0) ]
            null height 10
            hbox:
                hbox:
                    xsize 340
                    textbutton _("Quick menu buttons:"):
                        text_style "KoGa3_1a_button_text"
                        sensitive False
                        action NullAction()
                hbox:
                    #xsize 200
                    if persistent.KoGa3QuickMenuIcons is True:
                        textbutton _("Icons"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable ("persistent.KoGa3QuickMenuIcons", False)]
                    else:
                        textbutton _("Text"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable ("persistent.KoGa3QuickMenuIcons", True)]

        textbutton _("───────────────────────────────────────────"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()

        null height (20)

        vbox:
            spacing -8
            hbox:
                xpos 6
                text _("Quick menu font size  (current: [persistent.KoGa3QuickMenuTextSize]/40)"):
                    style "KoGa3_1a_button_text"
            hbox:
                ypos 5
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 750
                    value FieldValue(object=persistent, field='KoGa3QuickMenuTextSize', range=40, max_is_zero=False, style=u'slider', offset=0, step=1)

            hbox:
                xpos 6
                text _("Quick menu font outline  (current: [persistent.KoGa3TextOutline4]/10)"):
                    style "KoGa3_1a_button_text"
            hbox:
                ypos 5
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 750
                    value FieldValue(object=persistent, field='KoGa3TextOutline4', range=10, max_is_zero=False, style=u'slider', offset=0, step=1)

            hbox:
                hbox:
                    text _("   offset horizontal ([persistent.KoGa3TextOutline5])       offset vertical ([persistent.KoGa3TextOutline6])"):
                        style "KoGa3_1a_button_text"
            hbox:
                ypos 5
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 360
                    value FieldValue(object=persistent, field='KoGa3TextOutline5', range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 360
                    value FieldValue(object=persistent, field='KoGa3TextOutline6', range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)

        null height (34)

        hbox:
            hbox:
                xsize 50
                if KoGa3QuickMenuItems == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3QuickMenuItems", 1) ]
                if KoGa3QuickMenuItems == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action SetVariable("KoGa3QuickMenuItems", 0)

            hbox:
                textbutton _("{color=[KoGa3Color1]}────────── Quick menu items ─────────────"):
                    text_style "KoGa3_1_button_text"
                    if KoGa3QuickMenuItems == 0:
                        action [
                        SetVariable("KoGa3QuickMenuItems", 1) ]
                    if KoGa3QuickMenuItems == 1:
                        action [
                        SetVariable("KoGa3QuickMenuItems", 0) ]

        #################################################################################
        if KoGa3QuickMenuItems == 1:
            hbox:
                hbox:
                    xsize 50
                    textbutton _(" "):
                        text_style "KoGa3_1_button_text"
                        sensitive False
                        action NullAction()
                vbox:
                    spacing -13

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Back\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemBack == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemBack", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemBack", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Hist\" (History) is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemHist == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHist", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHist", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Hide\" (hide textbox) is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemHide == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHide", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHide", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Skip\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemSkip == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSkip", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSkip", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Auto\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemAuto == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemAuto", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemAuto", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Save\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemSave == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSave", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSave", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Load\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemLoad == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemLoad", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemLoad", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Q.Save\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemQSave == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQSave", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQSave", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Q.Load\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemQLoad == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQLoad", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQLoad", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Prefs\" (game settings) is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemPrefs == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemPrefs", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemPrefs", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Mod menu\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemModmenu == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemModmenu", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemModmenu", False)

        textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()

        hbox:
            spacing 30
            textbutton _("Back"):
                text_style "KoGa3_1_button_text"
                selected False
                sensitive True
                action [
                Hide("KoGa3GameSettingsQuickMenu"), 
                # Hide("KoGa3ScreenBlank"), 
                Show("KoGa3GameSettings") ]
            textbutton _("Close"):
                text_style "KoGa3_1_button_text"
                selected False
                sensitive True
                action [
                SetVariable ("KoGa3ModMenuButtonPressed", False),
                Hide("KoGa3ScreenBlank"), 
                Hide("KoGa3ScreenCheat"), 
                Hide("KoGa3ScreenCheatMore1"), 
                Hide("KoGa3ScreenModMenu"), 
                Hide("KoGa3ScreenJukebox"), 
                Hide("KoGa3GameSettings"), 
                Hide("KoGa3GameSettingsQuickMenu"), 
                Hide("KoGa3ScreenAudioMenu") ] 



#---------------------set variable game beginning---------------------#

default KoGa3ModMenuButtonPressed = False
default KoGa3MainMenu = 0
default KoGa3DialogOptions = 1
default KoGa3QuickMenuOptions = 0
default KoGa3QuickMenuItems = 1
default KoGa3CheatButton = 1
default KoGa3CheatChapterButton = 1
default KoGa3ScreenStatsFull = 0
default KoGa3GameProgress = "n/a"
default KoGa3ChoiceOptions = 0

# default KoGa3Music = 1                                                        #only for audio Mod
# default KoGa3CurrentMusic = MusicSilence
# default KoGa3JukeboxButton = 1

# default mcname = "MC"                                                         #only for renaming

default KoGa3ChoiceOption = 1                                                   # for WT Mod
default KoGa3WTChange = "\n{color=#008000}"                                     # green
#default KoGa3WTChange1 = "\n{size=32}{color=#0000ff}"                          # blue
default KoGa3WTChange1 = "\n{color=#ffdf00}"                                    # yellow
default KoGa3WTChange2 = "\n{color=#ff0000}"                                    # red
#default KoGa3WTChange = "\n{size=1}{color=#363636}"                            # info: WT Off

default KoGa3AutoWTChange1 = "\n{color=#ffdf00}"                                # yellow, for fergzWT
