from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock
Clock.max_iteration = 20
import time

class Sensor1(Widget):
    colour = ListProperty([0,1,0])

class Sensor2(Widget):
    colour = ListProperty([0,1,0])

class Sensor3(Widget):
    colour = ListProperty([0,1,0])

class Sensor4(Widget):
    colour = ListProperty([0,1,0])

class Sensor5(Widget):
    colour = ListProperty([0,1,0])

class Sensor6(Widget):
    colour = ListProperty([0,1,0])

class Sensor7(Widget):
    colour = ListProperty([0,1,0])

class Sensor8(Widget):
    colour = ListProperty([0,1,0])

class Sensor9(Widget):
    colour = ListProperty([0,1,0])

class Sensor10(Widget):
    colour = ListProperty([0,1,0])

class Sensor11(Widget):
    colour = ListProperty([0,1,0])

class Sensor12(Widget):
    colour = ListProperty([0,1,0])

class Sensor13(Widget):
    colour = ListProperty([0,1,0])

class Sensor14(Widget):
    colour = ListProperty([0,1,0])

class Sensor15(Widget):
    colour = ListProperty([0,1,0])

class Sensor16(Widget):
    colour = ListProperty([0,1,0])

class Sensor17(Widget):
    colour = ListProperty([0,1,0])

class Sensor18(Widget):
    colour = ListProperty([0,1,0])

class Sensor19(Widget):
    colour = ListProperty([0,1,0])


class SensorMonitor(Widget):
    pass
    


class SensorApp(App):
    def build(self):
        self.s1 =   Sensor1()
        self.s2 =   Sensor2()
        self.s3 =   Sensor3()
        self.s4 =   Sensor4()
        self.s5 =   Sensor5()
        self.s6 =   Sensor6()
        self.s7 =   Sensor7()
        self.s8 =   Sensor8()
        self.s9 =   Sensor9()
        self.s10 =  Sensor10()
        self.s11 =  Sensor11()
        self.s12 =  Sensor12()
        self.s13 =  Sensor13()
        self.s14 =  Sensor14()
        self.s15 =  Sensor15()
        self.s16 =  Sensor16()
        self.s17 =  Sensor17()
        self.s18 =  Sensor18()
        self.mp  = SensorMonitor()
        self.root = Widget()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        
        self.sensor_data = []
        with open('anime.csv', 'r') as fh:
            for line in fh:
                line = line[:-1]
                line = list(line.split(','))
                for i in range(0,len(line)):
                    if line[i] == '1':
                        line[i] = [0,1,0]
                    elif line[i] == '2':
                        line[i] =  [1,1,0.6]
                    elif  line[i] == '3':
                        line[i] = [1,0.647,0]
                    elif line[i] == '4':
                        line[i] = [1,0,0]
                self.sensor_data.append(line)
        Clock.schedule_once(self.update,2)
        Clock.schedule_once(self.update2,4)
        Clock.schedule_once(self.update3,6)
        Clock.schedule_once(self.update4,8)
        Clock.schedule_once(self.update5,10)
        Clock.schedule_once(self.update6,12)
        Clock.schedule_once(self.update7,14)
        Clock.schedule_once(self.update8,16)
        Clock.schedule_once(self.update9,18)
        Clock.schedule_once(self.update10,20)
        

    
    def update(self, *args):
        data = self.sensor_data[0]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

    def update2(self, *args):
        data = self.sensor_data[1]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        
    
    def update3(self, *args):
        data = self.sensor_data[2]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        
    
    def update4(self, *args):
        data = self.sensor_data[3]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

    def update5(self, *args):
        data = self.sensor_data[4]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

    def update6(self, *args):
        data = self.sensor_data[5]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

    def update7(self, *args):
        data = self.sensor_data[6]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

    def update8(self, *args):
        data = self.sensor_data[7]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

    def update9(self, *args):
        data = self.sensor_data[8]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

    def update10(self, *args):
        data = self.sensor_data[9]
        self.s1.colour = data[0]
        self.s2.colour = data[1]
        self.s3.colour = data[2]
        self.s4.colour = data[3]
        self.s5.colour = data[4]
        self.s6.colour = data[5]
        self.s7.colour = data[6]
        self.s8.colour = data[7]
        self.s9.colour = data[8]
        self.s10.colour = data[9]
        self.s11.colour = data[10]
        self.s12.colour = data[11]
        self.s13.colour = data[12]
        self.s14.colour = data[13]
        self.s15.colour = data[14]
        self.s16.colour = data[15]
        self.s17.colour = data[16]
        self.s18.colour = data[17]
        self.root.clear_widgets()
        self.root.add_widget(self.mp)
        self.root.add_widget(self.s1)
        self.root.add_widget(self.s2)
        self.root.add_widget(self.s3)
        self.root.add_widget(self.s4)
        self.root.add_widget(self.s5)
        self.root.add_widget(self.s6)
        self.root.add_widget(self.s7)
        self.root.add_widget(self.s8)
        self.root.add_widget(self.s9)
        self.root.add_widget(self.s10)
        self.root.add_widget(self.s11)
        self.root.add_widget(self.s12)
        self.root.add_widget(self.s13)
        self.root.add_widget(self.s14)
        self.root.add_widget(self.s15)
        self.root.add_widget(self.s16)
        self.root.add_widget(self.s17)
        self.root.add_widget(self.s18)
        

if __name__ == '__main__':
    SensorApp().run()