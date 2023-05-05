from graphics import *
import winsound

choose_sound = "sounds/play_settings_exit.wav"
confirm_sound = "sounds/confirm_sound.wav"


def main_menu():
    win = GraphWin("Main Menu", 600, 700)
    win.setBackground("white")

    bg_img = Image(Point(300, 350), "assets/main_menu.png")
    bg_img.draw(win)


    play_button = Rectangle(Point(220, 275), Point(380, 325))
    play_img = Image(Point(300, 300), "assets/btn_play.png") 
    play_button.setFill("light green")
    play_button.setOutline("light green")
    play_button.draw(win)
    play_img.draw(win)

    setting_button = Rectangle(Point(150, 350), Point(450, 400))
    setting_img = Image(Point(300, 375), "assets/btn_settings.png") 
    setting_button.setFill("light green")
    setting_button.setOutline("light green")
    setting_button.draw(win)
    setting_img.draw(win)

    exit_button = Rectangle(Point(220, 425), Point(380, 475))
    exit_img = Image(Point(300, 450), "assets/btn_exit.png")
    exit_button.setFill("light green")
    exit_button.setOutline("light green")
    exit_button.draw(win)
    exit_img.draw(win)

    # Set focus to the play button
    selected = 0
    play_button.setFill("green")
    
    # Set sound effects on initially
    sfx_on = True

    # Add a text object to display the status of sound effects

    while True:
        # Listen for key presses
        key = win.checkKey()

        if key == "Down":
            # Move focus down to the next button
            if selected == 0:
                if sfx_on:
                    winsound.PlaySound(choose_sound, winsound.SND_ASYNC)
                play_button.setFill("light green")
                setting_button.setFill("green")
                selected = 1
                
            elif selected == 1:
                if sfx_on:
                    winsound.PlaySound(choose_sound, winsound.SND_ASYNC)
                setting_button.setFill("light green")
                exit_button.setFill("green")
                selected = 2

        elif key == "Up":
            # Move focus up to the previous button
            if selected == 2:
                if sfx_on:
                    winsound.PlaySound(choose_sound, winsound.SND_ASYNC)
                exit_button.setFill("light green")
                setting_button.setFill("green")
                selected = 1
                
            elif selected == 1:
                if sfx_on:
                    winsound.PlaySound(choose_sound, winsound.SND_ASYNC)
                setting_button.setFill("light green")
                play_button.setFill("green")
                selected = 0
                
        elif key == "Return":
            # Select the currently focused button
            if selected == 0:
                if sfx_on:
                    winsound.PlaySound(confirm_sound, winsound.SND_ASYNC)
                win.close()
                loading_screen()
                break
            elif selected == 1:
                if sfx_on:
                    winsound.PlaySound(confirm_sound, winsound.SND_ASYNC)
                win.close()
                sfx_on = settings(sfx_on)
                break
            
            elif selected == 2:
                win.close()
                break

    win.close()

def loading_screen():
    win = GraphWin("Loading", 600, 700)
    win.setBackground("white")

    load = Text(Point(300, 250), "LOADING...")
    load.setFace('courier')
    load.setSize(25)
    load.setStyle('bold')
    load.draw(win)

    bar = Rectangle(Point(100, 300), Point(500, 330))
    bar.setFill("dark green")
    bar.draw(win)
    pt = Point(150, 330)
    progress = Rectangle(Point(100, 300), pt)
    progress.setFill("light green")
    progress.setWidth(0)
    progress.draw(win)

    # Update the progress bar
    while pt.getX() < 500:
        progress.move(10, 0)
        pt = progress.getP2()
        update(30) # wait for 50 milliseconds

    # Simulate loading time
    import time
    time.sleep(1)

    win.close()

    # Start the main game
    import os
    os.system("python main.py")

def settings(sfx_on):
    win = GraphWin('Settings', 600, 300)
    win.setBackground('white')

    sfx_on = True
    sfx_text = Text(Point(300, 100), "Press 'm' to mute and unmute sfx.")
    sfx_status = Text(Point(300, 150), "Sound Effects: ON")
    back_button = Text(Point(300, 200), "Press 'escape' to go back to main menu.")
    
    sfx_status.setTextColor("green")
    sfx_status.draw(win)
    sfx_text.draw(win)
    back_button.draw(win)

    disclaimer1 = Text(Point(300, 250), "Disclaimer: Sound ON/OFF is only for decal.")
    disclaimer2 = Text(Point(300, 275), "It has no effect on the main game. This is only a prototype.")
    disclaimer1.draw(win)
    disclaimer2.draw(win)

    while True:
        key = win.checkKey()
        if key == "m":
            sfx_on = not sfx_on
            if sfx_on:
                sfx_status.setText("Sound Effects: ON")
                sfx_status.setTextColor("green")
                sfx_on = True
            else:
                sfx_status.setText("Sound Effects: OFF")
                sfx_status.setTextColor("red")
                sfx_on = False
        if key == "Escape":
            win.close()
            main_menu()
            return sfx_on
    
main_menu()
