################################################################################
## Инициализация
################################################################################

init offset = -1


################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language 

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize 11
    # bottom_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    # thumb Frame("gui/history_log/vertical_[prefix_]thumb.png", tile=gui.scrollbar_tile) ###

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/history_log/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/history_log/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Если есть боковое изображение ("голова"), показывает её поверх текста.
    ## По стандарту не показывается на варианте для мобильных устройств — мало
    ## места.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## Когда этот параметр True, заголовки меню будут проговариваться рассказчиком.
## Когда False, заголовки меню будут показаны как пустые кнопки.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

transform show_hide_navigation:
    on show:
        xalign 0.5
        linear 1.0 xalign 0.0 
        
    on hide:
        xalign 0.0
        linear 1.0 xalign 0.5

screen quick_menu():

    ## Гарантирует, что оно появляется поверх других экранов.
    zorder 100
    
    if quick_menu:
            
        imagemap:
            style_prefix "quick" 
            xalign 0.5
                 
            ground "gui/textbox0.png"
            auto "gui/navigation_buttons_%s.png"

            hotspot (274, 695, 92, 25) action [Rollback()] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (366, 695, 91, 25) action [ShowMenu('history')] hovered [Play("sound", "audio/sounds/hover.mp3")]
            #hotspot () голоса возможно не будет, заменим на что-то
            #hotspot () скорость голоса
            hotspot (639, 695, 91, 25) action [Play("sound", "audio/sounds/button_on.mp3"), Preference("auto-forward", "toggle")] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (730, 695, 91, 25) action [Skip()] alternate Skip(fast=True, confirm=True) hovered [Play("sound", "audio/sounds/hover.mp3")]
            #hotspot (821, 695, 91, 25) action [Skip("seen")] hovered [Play("sound", "audio/sounds/hover.mp3")] пропуск увиденных сцен
            hotspot (911, 695, 93, 25) action [HideInterface()] hovered [Play("sound", "audio/sounds/hover.mp3")]

            hotspot (1183, 574, 85, 29) action [Play("sound", "audio/sounds/button_on.mp3"), QuickLoad()] hovered [Play("sound", "audio/sounds/hover.mp3")]#tooltip (" ")
            hotspot (1098, 574, 85, 29) action [Play("sound", "audio/sounds/button_on.mp3"), QuickSave()] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1098, 610, 85, 29) action [Play("sound", "audio/sounds/button_on.mp3"), ShowMenu("save")] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1183, 610, 85, 29) action [Play("sound", "audio/sounds/button_on.mp3"), ShowMenu("load")] hovered [Play("sound", "audio/sounds/hover.mp3")] 
            hotspot (1098, 644, 85, 29) action [Play("sound", "audio/sounds/button_on.mp3"), MainMenu()] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1183, 644, 85, 29) action [Play("sound", "audio/sounds/button_on.mp3"), Quit (confirm=True)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            # hotspot (1099, 679, 85, 29) заметки
            hotspot (1183, 679, 85, 29) action [Play("sound", "audio/sounds/button_on.mp3"), ShowMenu('preferences')] hovered [Play("sound", "audio/sounds/hover.mp3")]

## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Начать") action Start()

        else:

            textbutton _("История") action ShowMenu("history")

            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")

        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Завершить повтор") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Помощь не необходима и не относится к мобильным устройствам.
            textbutton _("Помощь") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Кнопка выхода блокирована в iOS и не нужна на Android и в веб-
            ## версии.
            textbutton _("Выход") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu

    add gui.main_menu_background

    ## Эта пустая рамка затеняет главное меню.
    frame:
        style "main_menu_frame"

    ## Оператор use включает отображение другого экрана в данном. Актуальное
    ## содержание главного меню находится на экране навигации.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None, или "viewport", или "vpgrid", когда этот
## экран предназначается для использования с более чем одним дочерним экраном,
## включённым в него.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude                

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

screen about():

    tag menu

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Версия [config.version!t]\n")

            ## gui.about обычно установлено в options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            key "K_ESCAPE" action Return()


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save():

    tag menu

    use save_file_slots()


screen load():

    tag menu

    use load_file_slots()

## Кнопка слота сохранения.
define saveload_slot_button_borders = Borders(10, 10, 10, 10)
define saveload_slot_button_text_size = 12
define saveload_slot_button_text_xalign = 0.5
define saveload_slot_button_text_idle_color = "#3F0000"
define saveload_slot_button_text_selected_idle_color = "#3F0000"
define saveload_slot_button_text_selected_hover_color = "#3F0000"
define saveload_slot_button_text_hover_color = "#3F0000"

## Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = 128
define config.thumbnail_height = 72

##########################

style saveload_slot_button is gui_button
style saveload_slot_button_text is gui_button_text
style saveload_slot_time_text is saveload_slot_button_text
style saveload_slot_name_text is saveload_slot_button_text

style saveload_page_label:
    xpadding 50
    ypadding 3

style saveload_page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style saveload_page_button:
    properties gui.button_properties("page_button")

style saveload_page_button_text:
    properties gui.button_text_properties("page_button")

style saveload_slot_button:
    properties gui.button_properties("slot_button")
    xpos 153 ypos 64

style saveload_slot_button_text:
    properties gui.button_text_properties("slot_button")

style saveload_slot_time_text_position:
    xpos 163 ypos 50
    size 12
    xalign 0.5
    idle_color "#3F0000"
    selected_idle_color "#3F0000"
    selected_hover_color "#3F0000"
    hover_color "#3F0000"

#########################

screen load_file_slots():
    tag menu

    window:
        xsize 1280 ysize 720
        
        ##### Задний план
        hbox:
            add "gui/load_screen/background.png" xpos 10 ypos 72

        ##### Название экрана Сохранения
        hbox:
            add "gui/load_screen/title_download.png" xpos 15 ypos 6
        
        ##### Навигация по страницам
        hbox:
            add "gui/load_screen/low_navigation.png" xpos 193 ypos 607

        ### Номер страницы, который может быть изменён посредством клика на кнопку.
        text FilePageName(auto='a', quick='q') xpos 445 ypos 607 font "font/constan.ttf" size 24 color "#ffffff"

        ##### Таблица слотов.
        vbox:
            xpos 80 ypos 109
            grid saveload_file_slot_cols saveload_file_slot_rows:
                xspacing 109 yspacing -2 
                for i in range(saveload_file_slot_cols * saveload_file_slot_rows):
                        
                    $ slot = i + 1

                    button:
                        
                        action FileAction(slot)
                        has vbox
                        ###### Пустой и заполненный слот с разным описанием
                        
                        if FileLoadable(slot, page=None, slot=False):
                                imagebutton:
                                    idle "gui/load_screen/loadable_file.png" xsize 470 ysize 92 
                                    hover "gui/load_screen/loadable_file_hover.png"
                                    action FileLoad(slot, confirm=True, page=None, cycle=False, slot=False)
                        else:
                            imagebutton:
                                    idle "gui/load_screen/empty slot.png" xsize 470 ysize 92 
                                    action NullAction()
                     
        vbox:
            xpos 154 ypos 119
            ## Это гарантирует, что ввод будет принимать enter перед остальными кнопками.
            order_reverse True
            grid saveload_file_slot_cols saveload_file_slot_rows:
                yspacing -18 xspacing 451
                for i in range(saveload_file_slot_cols * saveload_file_slot_rows):
                    
                    $ slot = i + 1

                    button: 
                        action FileAction(slot)
                        
                        has vbox
                        ##### Скриншот сохранения
                        add FileScreenshot(slot, empty="gui/load_screen/no_data.png") xsize 128 ysize 72
                        
                        ##### Время
                        text FileTime(slot, format=_("{#file_time}%Y/%m/%d (%H:%M)"), empty=_(" ")) xpos 185 ypos -73:
                            style "saveload_slot_time_text_position"

                        ##### Номер слота
                        text FileSlotName(slot, slots_per_page=10, format="%s%d", quick='', auto='') xpos -35 ypos -91: 
                            font "font/constan.ttf"

        vbox:
            xpos 154 ypos 119
            order_reverse True
            grid saveload_file_slot_cols saveload_file_slot_rows:
                xspacing 500 yspacing 70
                for i in range(saveload_file_slot_cols * saveload_file_slot_rows):
                    
                    $ slot = i + 1

                    button: 
                        action FileAction(slot)
                        
                        has vbox
                        ##### Новый файл
                        if FileNewest(slot):
                            add "gui/load_screen/new_file.png" xpos -92 ypos -20

        ##### Кнопки для доступа к другим страницам.
        imagemap:
                    
            auto "gui/load_screen/pages_%s.png" ypos 17
                
            hotspot (285, 0, 40, 40) action [FilePage(1)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (330, 0, 40, 40) action [FilePage(2)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (375, 0, 40, 40) action [FilePage(3)] hovered [Play("sound", "audio/sounds/hover.mp3")] 
            hotspot (420, 0, 40, 40) action [FilePage(4)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (465, 0, 40, 40) action [FilePage(5)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (510, 0, 40, 40) action [FilePage(6)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (555, 0, 40, 40) action [FilePage(7)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (600, 0, 40, 40) action [FilePage(8)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (645, 0, 40, 40) action [FilePage(9)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (690, 0, 40, 40) action [FilePage(10)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (735, 0, 40, 40) action [FilePage(11)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (780, 0, 40, 40) action [FilePage(12)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (825, 0, 40, 40) action [FilePage(13)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (870, 0, 40, 40) action [FilePage(14)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (915, 0, 40, 40) action [FilePage(15)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (960, 0, 40, 40) action [FilePage(16)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1005, 0, 40, 40) action [FilePage(17)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1050, 0, 40, 40) action [FilePage(18)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1095, 0, 40, 40) action [FilePage(19)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1140, 0, 40, 40) action [FilePage(20)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1185, 0, 40, 40) action [FilePage("auto")] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1230, 0, 40, 40) action [FilePage("quick")] hovered [Play("sound", "audio/sounds/hover.mp3")]
        # Кнопки быстрого доступа
        key "1" action [FilePage(1)]
        key "2" action [FilePage(2)]
        key "3" action [FilePage(3)]
        key "4" action [FilePage(4)]
        key "5" action [FilePage(5)]
        key "6" action [FilePage(6)]
        key "7" action [FilePage(7)]
        key "8" action [FilePage(8)]
        key "9" action [FilePage(9)]
        key "K_a" action [FilePage("auto")]
        key "K_q" action [FilePage("quick")]
        # Назад
        key "K_ESCAPE" action Return()
        # Удалить сохранение
        key "K_DELETE" action FileDelete(slot, confirm=True)


screen save_file_slots():
    tag menu

    window:
        xsize 1280 ysize 720
        
        ##### Задний план
        hbox:
            add "gui/save_screen/background.png" xpos 10 ypos 72

        ##### Название экрана Загрузки
        hbox:
            add "gui/save_screen/savescreen_title.png" xpos 15 ypos 6

        ##### Навигация по страницам
        hbox:
            add "gui/save_screen/low_navigation.png" xpos 193 ypos 607

        ### Номер страницы, который может быть изменён посредством клика на кнопку.
        text FilePageName(auto='a', quick='q') xpos 445 ypos 607 font "font/constan.ttf" size 24 color "#ffffff"

        ##### Таблица слотов.
        vbox:
            xpos 80 ypos 109
            grid saveload_file_slot_cols saveload_file_slot_rows:
                xspacing 109 yspacing -2 
                for i in range(saveload_file_slot_cols * saveload_file_slot_rows):
                        
                    $ slot = i + 1

                    button:
                        
                        action FileAction(slot)
                        has vbox
                        ###### Пустой и заполненный слот с разным описанием
                        
                        if FileLoadable(slot, page=None, slot=False):
                                imagebutton:
                                    idle "gui/save_screen/saveable_file_ground.png" xsize 470 ysize 92 
                                    hover "gui/save_screen/saveable_file_hover.png"
                                    action FileSave(slot, confirm=True, page=None, cycle=False, slot=False)
                        else:
                            imagebutton:
                                    idle "gui/save_screen/empty_slot.png" xsize 470 ysize 92 
                                    action NullAction()

        ### Информация слотов
        vbox:
            xpos 154 ypos 119
            ## Это гарантирует, что ввод будет принимать enter перед остальными кнопками.
            order_reverse True
            grid saveload_file_slot_cols saveload_file_slot_rows:
                yspacing -18 xspacing 451
                for i in range(saveload_file_slot_cols * saveload_file_slot_rows):
                    
                    $ slot = i + 1

                    button: 
                        action FileAction(slot)
                        
                        has vbox
                        ##### Скриншот сохранения
                        add FileScreenshot(slot, empty="gui/save_screen/no_data.png") xsize 128 ysize 72
                        
                        ##### Время
                        text FileTime(slot, format=_("{#file_time}%Y/%m/%d (%H:%M)"), empty=_(" ")) xpos 185 ypos -73:
                            style "saveload_slot_time_text_position"

                        ##### Номер слота
                        text FileSlotName(slot, slots_per_page=10, format="%s%d", quick='', auto='') xpos -35 ypos -91: 
                            font "font/constan.ttf"
        
        ### Дополнительная информация
        vbox:
            xpos 154 ypos 119
            order_reverse True
            grid saveload_file_slot_cols saveload_file_slot_rows:
                xspacing 500 yspacing 70
                for i in range(saveload_file_slot_cols * saveload_file_slot_rows):
                    
                    $ slot = i + 1

                    button: 
                        action FileAction(slot)
                        
                        has vbox
                        ##### Новый файл
                        if FileNewest(slot):
                            add "gui/load_screen/new_file.png" xpos -92 ypos -20

        ##### Кнопки для доступа к другим страницам.
        imagemap:
                    
            auto "gui/save_screen/pages_%s.png" ypos 17
                
            hotspot (285, 0, 40, 40) action [FilePage(1)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (330, 0, 40, 40) action [FilePage(2)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (375, 0, 40, 40) action [FilePage(3)] hovered [Play("sound", "audio/sounds/hover.mp3")] 
            hotspot (420, 0, 40, 40) action [FilePage(4)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (465, 0, 40, 40) action [FilePage(5)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (510, 0, 40, 40) action [FilePage(6)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (555, 0, 40, 40) action [FilePage(7)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (600, 0, 40, 40) action [FilePage(8)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (645, 0, 40, 40) action [FilePage(9)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (690, 0, 40, 40) action [FilePage(10)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (735, 0, 40, 40) action [FilePage(11)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (780, 0, 40, 40) action [FilePage(12)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (825, 0, 40, 40) action [FilePage(13)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (870, 0, 40, 40) action [FilePage(14)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (915, 0, 40, 40) action [FilePage(15)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (960, 0, 40, 40) action [FilePage(16)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1005, 0, 40, 40) action [FilePage(17)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1050, 0, 40, 40) action [FilePage(18)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1095, 0, 40, 40) action [FilePage(19)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1140, 0, 40, 40) action [FilePage(20)] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1185, 0, 40, 40) action [FilePage("auto")] hovered [Play("sound", "audio/sounds/hover.mp3")]
            hotspot (1230, 0, 40, 40) action [FilePage("quick")] hovered [Play("sound", "audio/sounds/hover.mp3")]
        # Кнопки быстрого доступа
        key "1" action [FilePage(1)]
        key "2" action [FilePage(2)]
        key "3" action [FilePage(3)]
        key "4" action [FilePage(4)]
        key "5" action [FilePage(5)]
        key "6" action [FilePage(6)]
        key "7" action [FilePage(7)]
        key "8" action [FilePage(8)]
        key "9" action [FilePage(9)]
        key "K_a" action [FilePage("auto")]
        key "K_q" action [FilePage("quick")]
        # Назад
        key "K_ESCAPE" action Return()
        # Удалить сохранение
        key "K_DELETE" action FileDelete(slot, confirm=True)



## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Сторона отката")
                    textbutton _("Отключено") action Preference("rollback side", "disable")
                    textbutton _("Левая") action Preference("rollback side", "left")
                    textbutton _("Правая") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Пропуск")
                    textbutton _("Всего текста") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")
                    textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))

                ## Дополнительные vbox'ы типа "radio_pref" или "check_pref"
                ## могут быть добавлены сюда для добавления новых настроек.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")

                    bar value Preference("text speed")

                    label _("Скорость авточтения")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
            key "K_ESCAPE" action Return()


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen historyy(title, scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
    style_prefix "historyy"
    tag menu

    modal True
    zorder 50

    if scroll == "viewport":

        viewport id "vp":
            yinitial yinitial
            xinitial 0.7

            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True       
            transclude
            
            vbar value YScrollValue("vp")

    elif scroll == "vpgrid":

        vpgrid id "vp":
            cols 1
            yinitial yinitial
            xinitial 0.7

            scrollbars "vertical"
            mousewheel True
            pagekeys True
            side_yfill True
            
            transclude

    else:
        transclude

    fixed:

        vbox:

            vbar:
                xpos 1078 ypos 68
                ysize 490 xsize 26
                top_bar "gui/history_log/scroll_idle_bar2.png" ############ посмотреть видео по vbar
                bottom_bar "gui/history_log/scroll_idle_bar2.png" 
                thumb "gui/history_log/vertical_[prefix_]thumb.png"
                value YScrollValue("vp")
                # hover_sound "audio/sounds/hover.mp3"

        button:
            xpos 1071 ypos 30
            xsize 30 ysize 30
            idle_background "gui/history_log/return_idle.png"
            hover_foreground "gui/history_log/return_hover.png"
            hover_sound "audio/sounds/hover.mp3"
            focus_mask True
            action Return()

        button:
            xpos 1064 ypos 605
            xsize 44 ysize 44
            idle_background "gui/history_log/scroll_up_idle.png"
            hover_foreground "gui/history_log/scroll_up_hover.png"
            hover_sound "audio/sounds/hover.mp3"
            focus_mask True
            action Scroll ("vp", "vertical decrease", "step")
            keysym ("K_UP", "repeat_K_UP", "mousedown_4") 

        button:
            xpos 1064 ypos 654
            xsize 44 ysize 44
            idle_background "gui/history_log/scroll_down_idle.png"
            hover_foreground "gui/history_log/scroll_down_hover.png"
            hover_sound "audio/sounds/hover.mp3"
            focus_mask True
            action Scroll ("vp", "vertical increase", "step")
            keysym ("K_DOWN", "repeat_K_DOWN", "mousedown_5") 

screen history():

    style_prefix "history"
    tag menu
    zorder 25

    frame:
        xsize 1280 ysize 720
        background "gui/history_log/history.png" align (0.5, 0.5)

    ## Избегайте предсказывания этого экрана, так как он может быть очень    
    ## массивным.
    predict False

    use historyy(_("История")): #game_menu(_("История"), 

        for h in _history_list:
            
            window:
                
                ## Это всё правильно уравняет, если history_height будет
                ## установлен на None.
                has fixed:
                    yfit None
                    xsize 720

                if h.who:

                    label h.who:
                        
                        xpos 332
                        style "history_name"
                        substitute False

                        ## Берёт цвет из who параметра персонажа, если он
                        ## установлен.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")

## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt" }

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xsize 1280
    ysize gui.history_height 

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos spacing 10
    xanchor gui.history_text_xalign
    xsize 1280
    ysize 720
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Пробел")
        text _("Прохождение диалогов без возможности делать выбор.")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Esc")
        text _("Вход в игровое меню.")

    hbox:
        label _("Ctrl")
        text _("Пропускает диалоги, пока зажат.")

    hbox:
        label _("Tab")
        text _("Включает режим пропуска.")

    hbox:
        label _("Page Up")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Page Down")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label "H"
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label "S"
        text _("Делает снимок экрана.")

    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")

    hbox:
        label "Shift+A"
        text _("Открывает меню специальных возможностей.")


screen mouse_help():

    hbox:
        label _("Левый клик")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label _("Правый клик")
        text _("Вход в игровое меню.")

    hbox:
        label _("Колёсико вверх\nКлик на сторону отката")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Колёсико вниз")
        text _("Откатывает предыдущее действие вперёд.")


screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")


    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Start, Guide")
        text _("Вход в игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")

    textbutton _("Калибровка") action GamepadCalibrate()



style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Пропускаю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
