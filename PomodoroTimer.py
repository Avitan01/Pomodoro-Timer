import datetime
from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk, Image
import pygame


def init_timer(root):
    """Initilaize programs settings"""
    pygame.mixer.init()
    top_frame = Frame(root)
    top_frame.pack()
    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)
    style = Style()
    style.configure('W.TButton', font =('Times', 14, 'bold'),  height = 20, width = 5, foreground = 'black', background= "white")
    countdown = Countdown(root)
    countdown.pack()
    learn = Button(top_frame, text='Learn', style='W.TButton', command=countdown.learn)
    rest = Button(top_frame, text='Rest', style='W.TButton', command=countdown.rest)
    learn.pack(side=RIGHT, padx=20, pady=15)
    rest.pack(side=LEFT, padx=20, pady=15)


class Countdown(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.seconds_left = 0
        self._timer_on = False
        self.pause = False
        self.is_countdown = False
        
    def learn(self):
        """Create settings to learn"""
        if self.is_countdown:
            self.seconds_left = 25 * 60
        self.time_set = 25
        self.clear()
        self.create_widgets()
        self.show_widgets()
        
    def rest(self):
        """Create settings to rest"""
        if self.is_countdown:
            self.seconds_left = 5 * 60
        self.time_set = 5
        self.clear()
        self.create_widgets()
        self.show_widgets()
        
    def clear(self):
        """Remove current widgets"""
        try:
            self.start.pack_forget()
            self.stop.pack_forget()
            self.label.pack_forget()
            self.pause = False
        except AttributeError:
            pass

    def create_widgets(self):
        """Create widgets for the timer"""
        style = Style()
        style.configure('T.TButton', font =('Ariel', 20, 'bold'),  height = 20, width = 20, foreground = 'black', background= "white")
        style.configure("S.TButton", font=('Times', 10, 'bold'), foreground = 'green')
        style.configure("A.TButton", font=('Times', 10, 'bold'), foreground = 'red')
        if self.time_set == 25:
            self.label = Label(self, text="25:00", style='T.TButton')
        else:
            self.label = Label(self, text="05:00", style='T.TButton')
        self.start = Button(self, text='Start', style="S.TButton", command=self.start_button)
        self.stop = Button(self, text="Stop", style="A.TButton", command=self.stop_button)
    
    def show_widgets(self):
        """Display widgets"""
        self.label.pack(pady=15)
        self.start.pack(pady=10, padx=5, side=RIGHT)
        self.stop.pack(padx=5, side=LEFT)
    
    def start_button(self):
        """Control the timer using the Start button"""
        if not self.pause:
            if self.time_set == 25:
                self.seconds_left = 60 * 25
            else:
                self.seconds_left = 60 * 5
        self.pause = False
        self.stop_timer()
        self.countdown()
    
    def stop_button(self):
        """Control the timer using the Stop button"""
        self.pause = True
        self._timer_on = False
        self.is_countdown = False
    
    def stop_timer(self):
        """Stop timer after the set time has passed"""
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False
            self.is_countdown = False

    def countdown(self):
        """Create a countdown and display it"""
        self.is_countdown = True
        if not self.pause:
            self.label['text'] = self.convert_seconds_left_to_time()
            if self.seconds_left <= 5:
                self.sound()
            if self.seconds_left:
                self.seconds_left -= 1
                self._timer_on = self.after(1000, self.countdown)
            else:
                self._timer_on = False
    
    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)

    def sound(self):
        """Create sound"""
        pygame.mixer.music.load("C:\\Users\\Shahar Avitan\\VScode\\Projects\\beep.mp3")
        pygame.mixer.music.play(loops=0)
    

if __name__ == "__main__":
    root = Tk()
    root.title("PT")
    root.iconbitmap("C:\\Users\\Shahar Avitan\\VScode\\Projects\\Pomodoro\\pomo.ico")
    root.resizable(False, False)
    root.geometry("200x190")
    init_timer(root)
    root.mainloop()


 