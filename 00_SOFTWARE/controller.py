# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Dirk Ziegenbalg
# Copyright   : Copyright 2021, Institute of Chemical Engineering, Prof. Dr. Dirk Ziegenbalg, Ulm University'
# License     : GNU LGPL
# =============================================================================

import threading


class Controller:
    import configparser
    import modules
    import re
    import threading
    import csv
    from itertools import zip_longest
    import time

    def __init__(self):
        self.tinkerforge_config = {}
        self.modules_list = {}
        self.modules_config = {}
        self.modules_instances = {}
        self.tk_attributes = {}
        self.tk_attributes["initialized_UID"] = {}
        self.gui = {}
        self.gui["button_number"] = -1
        # self.gui["tab_number"] = -1
        self.gui["buttons"] = {}
        self.gui["tabs"] = {}
        self.start_time = self.time.strftime('%Y_%m_%d_%H_%M_%S')

    def read_configs(self):
        # global config: tinkerforge + installed modules
        config = self.configparser.ConfigParser()
        config.optionxform = lambda option: option
        config.read("conf/global.conf")

        for i in config['TINKERFORGE']:
            self.tinkerforge_config[i] = config['TINKERFORGE'][i]

        for i in config['MODULES']:
            self.modules_list[i] = config['MODULES'][i]

        # modules: specific config files
        for i in config['MODULES'].keys():
            config_tmp = self.configparser.ConfigParser()
            config_tmp.optionxform = lambda option: option
            config_tmp.read("conf/"+config['MODULES'][i].lower()+".conf")
            self.modules_config[i] = {self.re.sub(r'_[0-9]*',r'',self.modules_list[i]) : config_tmp}
            # self.modules_config[i] = {self.re.sub(r'_[0-9]*',r'',self.modules_list[i]) : config_tmp.sections()}

    
    def initialize_tk(self):
        from tinkerforge.ip_connection import IPConnection
        from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

        HOST = self.tinkerforge_config['HOST']
        PORT = int(self.tinkerforge_config['PORT'])
        UID_LCD = self.tinkerforge_config['UID_LCD_0']

        self.tk_attributes["ipcon"] = IPConnection()
        self.tk_attributes["lcd"] = BrickletLCD128x64(UID_LCD, self.tk_attributes["ipcon"])

        self.tk_attributes["ipcon"].connect(HOST, PORT)

        self.tk_attributes["lcd"].set_gui_tab_configuration(self.tk_attributes["lcd"].CHANGE_TAB_ON_CLICK_AND_SWIPE, True)
        self.tk_attributes["lcd"].clear_display()

    def disconnect_tk(self):
        self.tk_attributes["lcd"].clear_display()
        self.tk_attributes["lcd"].reset()
        self.tk_attributes["ipcon"].disconnect()


    def initialize_modules(self):
        counter = 0
        for i in self.modules_list:
            self.tk_attributes["lcd"].clear_display()
            module = self.re.sub(r'_[0-9]*',r'',self.modules_list[i])
            call = getattr(self.modules, self.re.sub(r'_[0-9]*',r'',module))
            # self.gui[counter] = []
            self.gui["tab_number"] = counter
            if self.re.sub(r'_[0-9]*',r'',module) == "LED":
                if self.modules_config[i][module][module]["LED_Module"] == self.modules_config[i][module][module]["Total_Number_of_LED_Modules"]:
                    self.modules_config[i][module][module]["Tab_Number"] = str(counter)
                    self.tk_attributes["lcd"].set_gui_tab_text(counter, self.modules_config[i][module][module]["Tab_Text"])
                    counter += 1
                self.modules_instances[i] = call(i, self.tk_attributes, self.modules_config, self.gui)
                self.modules_instances[i].set_instances(self.modules_instances)
                UID_list = self.modules_instances[i].connect()
                self.tk_attributes["initialized_UID"][i] = UID_list
                self.modules_instances[i].set_instances(self.modules_instances)
            
            elif self.modules_config[i][module][module]["Joint_Use"] == str(1):
                for ii in self.tk_attributes["initialized_UID"]:
                    if self.modules_config[i][module][module]["UID"] in self.tk_attributes["initialized_UID"][ii]:
                        if self.modules_config[i][module][module]["Tab_Text"] != "---":
                            self.modules_config[i][module][module]["Tab_Number"] = str(counter)
                            self.tk_attributes["lcd"].set_gui_tab_text(counter,
                                                                       self.modules_config[i][module][module]["Tab_Text"])
                            counter += 1
                        self.modules_instances[i] = call(i, self.tk_attributes, self.modules_config, self.gui)
                        self.modules_instances[i].set_instances(self.modules_instances)
                        self.modules_instances[i].connect(self.modules_instances[ii])

            else:
                if self.modules_config[i][module][module]["Tab_Text"] != "---":
                    self.modules_config[i][module][module]["Tab_Number"] = str(counter)
                    self.tk_attributes["lcd"].set_gui_tab_text(counter, self.modules_config[i][module][module]["Tab_Text"])
                    counter += 1
                self.modules_instances[i] = call(i,self.tk_attributes,self.modules_config,self.gui)
                self.modules_instances[i].connect()


        self.tk_attributes["lcd"].register_callback(self.tk_attributes["lcd"].CALLBACK_GUI_BUTTON_PRESSED, self.cb_global_button_handling)
        self.tk_attributes["lcd"].register_callback(self.tk_attributes["lcd"].CALLBACK_GUI_TAB_SELECTED, self.cb_global_tab_handling)

        # Set period for GUI button pressed callback to 0.1s (100ms)
        self.tk_attributes["lcd"].set_gui_button_pressed_callback_configuration(100, True)

        # Set period for GUI slider value callback to 0.1s (100ms)
        self.tk_attributes["lcd"].set_gui_slider_value_callback_configuration(100, True)

        # Set period for GUI tab selected callback to 0.1s (100ms)
        self.tk_attributes["lcd"].set_gui_tab_selected_callback_configuration(100, True)


    def cb_global_button_handling(self,index,pressed):
        module = self.gui["buttons"][index][0]
        if pressed == True:
            call = self.modules_instances[module]
            call.button_handling(index)

    def cb_global_tab_handling(self,index):
        module = self.gui["tabs"][index][0]
        call = self.modules_instances[module]
        call.draw_tab()


    def make_logs(self):
        for i in self.modules_instances:
            self.modules_instances[i].log

        self.threading.Timer(1, self.make_logs).start()

    def save_logs(self):
        filename = self.start_time + '_Experiment.csv'
        all_logs = [[]]
        for i in self.modules_instances:
            all_logs = self.zip_longest(*all_logs,*self.modules_instances[i].log,fillvalue='')
        with open(filename, 'w', encoding="utf-8",
                  newline='') as myfile:
            wr = self.csv.writer(myfile)
            for row in all_logs:
                wr.writerow(list(row))
            myfile.close()
        self.threading.Timer(5, self.save_logs).start()

if __name__ == "__main__":
    cont_0 = Controller()
    cont_0.read_configs()
    cont_0.initialize_tk()
    cont_0.initialize_modules()
    # cont_0.threading.Timer(1,cont_0.make_logs).start()
    # cont_0.threading.Timer(5,cont_0.save_logs).start()


    input("Press key to exit\n")
    cont_0.disconnect_tk()


# todo update of config files after experiment to current values
# todo add exception for interrupt or other issues and ensure safe state

__author__ = "Dirk Ziegenbalg"
__copyright__ = 'Copyright 2021, Institute of Chemical Engineering, Ulm University'
__license__ = "GNU LGPL"