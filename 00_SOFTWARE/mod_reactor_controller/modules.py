#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    General functions and specific functions for different extension modules of the modular photoreactor.

    `modules` implements the classes:

    - `General_functions`
    - `Pump`
    - `Pressure`
    - `LED`
    - `Stirrer`
    - `Fan`
    - `Tempering`

    The classes of this module handle generation of the instances for different hardware modules of the mod_reactor_controller.
    All classed implement the following functionalities:

    - import necessary tinkerforge modules and general modules
    - setup tinkerforge IP connection
    - module specific definitions
    - initialize module specific functions, i.e. set or get values
    - initialize LCD GUI tab generation
    - draw/update LCD GUI tab
    - define input buttons and their functions if needed
    - data logging

    The class `General_functions` provides functions that are used in a general context.
"""

import copy
import time
from simple_pid import PID


class General_functions:
    """
    A class used to ensure general functionality
    """



    def initialize_tab(self, buttons, tab_number):
        """
        Parameters
        ----------
        buttons : list
            Used buttons.

        tab_number : int
            Number of active tab.

        Returns
        ------
        int : Number of the active tab.
        """
        lcd = self.tk_attributes["lcd"]
        # self.gui["tab_number"] += 1
        lcd.set_gui_tab_selected(tab_number)
        lcd.clear_display()

        # self.gui["tab_number"] += 1
        # lcd.set_gui_tab_selected(self.gui["tab_number"])
        self.gui["tabs"][tab_number] = [self.module_number]
        self.attributes["Tab"] = [tab_number]

        if buttons != []:
            for i in buttons:
                self.gui["button_number"] += 1
                self.attributes[i] = self.gui["button_number"]
                self.gui["buttons"][self.gui["button_number"]] = [self.module_number]

        self.draw_tab()
        return tab_number

    # def get_tab_number(self):
    #     for i in self.gui["tabs"].values():
    #         for ii in i:
    #             try:
    #                 index = ii.index(self.module_number)
    #                 tab_number = self.gui.
    #     self.gui["tab_number"]


class Pump:
    """
    A class used to ensure the functions of the `Pump Module`.

    Attributes
    ----------
    module_number : str
        Number of the module.
    tk_attributes : dict
        Tinkerforge bricklet specific information.
    modules_conf : dict
        Configurations of the connected modules.
    gui : dict
        Gui specific key value pairs.
    name : str
        Name of the module.
    attributes : dict
        Pump module specific attributes.
    logs : list
        Logged data.
    """
    from tinkerforge.bricklet_industrial_analog_out_v2 import BrickletIndustrialAnalogOutV2



    def __init__(self, module_number, tk_attributes, modules_conf, gui):
        self.name = "Pump"
        self.tk_attributes = tk_attributes
        self.modules_conf = modules_conf
        self.attributes = {}
        self.attributes["FlowRate"] = int(self.modules_conf[module_number]["Pump"]["Pump"]["Flow_Rate"])
        self.set_current_flowrate(self.attributes["FlowRate"])
        self.module_number = module_number
        self.logs = []
        self.gui = gui
        self.initialize_tab()

    def connect(self):
        """
        Builds up the IP connection for the used tinkerforge bricklets.

        Returns
        ------
        list
            Tinkerforge bricklet UIDs.
        """
        UID = self.modules_conf[self.module_number]["Pump"]["Pump"]["UID"]
        self.attributes["brick"] = self.BrickletIndustrialAnalogOutV2(UID, self.tk_attributes["ipcon"])
        self.attributes["brick"].set_enabled(False)
        UID_list = []
        UID_list.append(UID)
        return UID_list

    def initialize_tab(self):
        """
        Initializes GUI tab.
        """
        self.gui["tab_number"] = General_functions.initialize_tab(self, ["+-button", "--button"],
                                                                  copy.deepcopy(self.gui["tab_number"]))

    def draw_tab(self):
        """
        Draws GUI tab.
        """
        lcd = self.tk_attributes["lcd"]
        if lcd.get_gui_tab_selected() == self.attributes["Tab"][0]:
            lcd.clear_display()
            # lcd.set_gui_tab_selected(self.gui["tab_number"])
            lcd.draw_text(0, 0, lcd.FONT_6X8, lcd.COLOR_BLACK,
                          'Flow rate: ' + str(self.attributes["FlowRate"]) + ' ml/min')
            lcd.set_gui_button(self.attributes["+-button"], 52, 10, 10, 10, "+")
            lcd.set_gui_button(self.attributes["--button"], 67, 10, 10, 10, "-")

    def set_current_flowrate(self, flowrate):
        """
        Calculates a control current for the pump in dependence to the set flow rate. Results are stored
        in `attributes["FlowRate"]`and `attributes["current"]`.

        Parameters
        ----------
        flowrate : int
            Flowrate values. Valid range depends on used pump.
        """
        self.attributes["FlowRate"] = flowrate
        if flowrate < 30:
            c = 3.6622  # Parameters for the control current calculation. Valid for a maximum stroke volume of 0.52 mL
            # and a flowrate of 10 to less than 30 mL per min.
            m = 0.1468
        if flowrate >= 30:
            c = 3.6184  # Parameters for the control current calculation. Valid for a maximum stroke volume of 0.52 mL
            # and a flowrate of more than 30 mL per min.
            m = 0.1508

        self.attributes[
            "current"] = flowrate * m + c  # Here the set flowrate is converted into a control current (in mA).

    def start_pump(self):
        """
        Sets the calculated control current to start the pump.

        """
        self.attributes["brick"].set_voltage(0)
        self.attributes["brick"].set_current(self.attributes["current"] * 1000)
        self.attributes["brick"].set_enabled(True)

    def button_handling(self, button):
        """
        Assigns functions to GUI buttons.

        Parameters
        ----------
        button : boolean
            State of the pressed button.
        """

        if button == self.attributes["+-button"] and self.attributes["FlowRate"] < 106:
            self.attributes[
                "FlowRate"] += 1  # LCD button "+" set flow rate of pump increases by 1 mL/min if flow rate is beneath 106 mL/min.
        if button == self.attributes["--button"] and self.attributes["FlowRate"] > 10:
            self.attributes[
                "FlowRate"] -= 1  # LCD button "-" set flow rate of pump decreases by 1 mL/min if flow rate is above 10 mL/min.
        self.set_current_flowrate(self.attributes["FlowRate"])
        self.start_pump()
        self.draw_tab()

    @property
    def log(self):
        """
        Logs flow rates in a log list.

        Returns
        ------
        list
            A list with header and logged flow rates.
        """
        header = ["Timestamp",
                  "Flow Rate/(ml/min)",
                  ]
        log_data = [time.asctime(time.localtime()),
                    self.attributes["FlowRate"]]
        if self.logs == []:
            self.logs.append(header)
        self.logs.append(log_data)
        return self.logs


class Pressure:
    """
    A class used to ensure the functions of the `Pressure Module`.

    Attributes
    ----------
    module_number : str
        Number of the module.
    tk_attributes : dict
        Tinkerforge bricklet specific information.
    modules_conf : dict
        Configurations of the connected modules.
    gui : dict
        Gui specific key value pairs.
    name : str
        Name of the module.
    attributes : dict
        Pressure module specific attributes.
    logs : list
        Logged data.
    """
    from tinkerforge.bricklet_industrial_dual_analog_in_v2 import BrickletIndustrialDualAnalogInV2
    from tinkerforge.bricklet_industrial_analog_out_v2 import BrickletIndustrialAnalogOutV2



    def __init__(self, module_number, tk_attributes, modules_conf, gui):
        self.name = "Pressure"
        self.tk_attributes = tk_attributes
        self.modules_conf = modules_conf
        self.attributes = {}
        self.attributes["pressure"] = 0
        self.module_number = module_number
        self.logs = []
        self.gui = gui
        self.initialize_tab()

    def connect(self):
        """
        Builds up the IP connection for the used tinkerforge bricklets.

        Returns
        ------
        list
            Tinkerforge bricklet UIDs.
        """
        UID = self.modules_conf[self.module_number]["Pressure"]["Pressure"]["UID"]
        UID_2 = self.modules_conf[self.module_number]["Pressure"]["Pressure"]["UID_2"]
        self.attributes["brick"] = self.BrickletIndustrialDualAnalogInV2(UID, self.tk_attributes["ipcon"])
        self.attributes["brick"].register_callback(self.attributes["brick"].CALLBACK_VOLTAGE, self.cb_pressure_readout)
        self.attributes["brick"].set_voltage_callback_configuration(
            int(self.modules_conf[self.module_number]["Pressure"]["Pressure"]["Channel"]), 1000, True, "x", 0, 0)
        self.attributes["brick2"] = self.BrickletIndustrialAnalogOutV2(UID_2, self.tk_attributes["ipcon"])
        self.attributes["brick2"].set_voltage(10000)
        self.attributes["brick2"].set_enabled(True)
        UID_list = []
        UID_list.append(UID)
        return UID_list

    def initialize_tab(self):
        """
        Initializes GUI tab.
        """
        self.gui["tab_number"] = General_functions.initialize_tab(self, [], copy.deepcopy(self.gui["tab_number"]))

    def draw_tab(self):
        """
        Draws GUI tab.
        """
        lcd = self.tk_attributes["lcd"]
        if lcd.get_gui_tab_selected() == self.attributes["Tab"][0]:
            lcd.clear_display()
            lcd.draw_text(0, 0, lcd.FONT_6X8, lcd.COLOR_BLACK,
                          'Pressure: ' + str(round(self.attributes["pressure"], 2)) + ' bar')

    def cb_pressure_readout(self, channel, voltage):
        """
        Callback that reads voltage signal of the pressure sensor and converts it to pressure in bar. Result is stored
        in `attributes["pressure"]`.

        """
        if channel == int(self.modules_conf[self.module_number]["Pressure"]["Pressure"]["Channel"]):
            self.attributes["pressure"] = 0.0019 * voltage + 0.9593
            if self.tk_attributes["lcd"].get_gui_tab_selected() == self.attributes["Tab"][0]:
                self.draw_tab()

    @property
    def log(self):
        """
        Logs pressure in a log list.

        Returns
        ------
        list
            A list with header and logged flow rates.
        """
        header = ["Timestamp",
                  "Pressure/bar",
                  ]
        log_data = [time.asctime(time.localtime()),
                    self.attributes["pressure"]]
        if self.logs == []:
            self.logs.append(header)
        self.logs.append(log_data)
        return self.logs


class LED:
    """
    A class used to ensure the functions of the LED Module

    Attributes
    ----------
    module_number : str
        Number of the module.
    tk_attributes : dict
        Tinkerforge bricklet specific information.
    modules_conf : dict
        Configurations of the connected modules.
    gui : dict
        Gui specific key value pairs.
    name : str
        Name of the module.
    attributes : dict
        LED module specific attributes.
    logs : list
        Logged data.

    """
    from tinkerforge.bricklet_io4_v2 import BrickletIO4V2



    def __init__(self, module_number, tk_attributes, modules_conf, gui):

        self.name = "LED"
        self.tk_attributes = tk_attributes
        self.modules_conf = modules_conf
        self.attributes = {}
        self.attributes["freq_LED"] = 10
        self.attributes["Duty_Cycle_LED"] = 5000
        self.module_number = module_number
        self.logs = []
        self.gui = gui
        if self.modules_conf[self.module_number]["LED"]["LED"]["LED_Module"] == \
                self.modules_conf[self.module_number]["LED"]["LED"]["Total_Number_of_LED_Modules"]:
            self.initialize_tab()

    def set_instances(self, modules_instances):
        """
        Set the required instances of installed LED modules to enable use of more than 1 module. The instances are
        stored in `attributes["Installed_Modules"]`

        Parameters
        ----------
        modules_instances : dict
            Key value pairs of connected modules.
        """
        if self.modules_conf[self.module_number]["LED"]["LED"]["LED_Module"] == \
                self.modules_conf[self.module_number]["LED"]["LED"][
                    "Total_Number_of_LED_Modules"]:
            self.attributes["Installed_Modules"] = []
            tk_instances = modules_instances
            for i in self.modules_conf:
                if i in tk_instances:
                    if tk_instances[i].name == "LED":
                        self.attributes["Installed_Modules"].append(tk_instances[i])

    def connect(self):
        """
        Builds up the IP connection for the used tinkerforge bricklets.

        Returns
        ------
        list
            Tinkerforge bricklet UIDs.
        """
        UID_list = []
        if self.modules_conf[self.module_number]["LED"]["LED"]["LED_Module"] == \
                self.modules_conf[self.module_number]["LED"]["LED"][
                    "Total_Number_of_LED_Modules"]:
            self.attributes["brick"] = {}
            for i in self.attributes["Installed_Modules"]:
                UID = self.modules_conf[i.module_number]["LED"]["LED"]["UID"]
                self.attributes["brick"][i.module_number] = self.BrickletIO4V2(UID, self.tk_attributes["ipcon"])
                UID_list.append(UID)
        return UID_list

    def set_parameters(self):
        """
        Sets bricklets to the desired parameters, i.e. channel of I/O bricklet, frequency of PWM signal and the duty
        cycle.
        """
        if self.modules_conf[self.module_number]["LED"]["LED"]["LED_Module"] == \
                self.modules_conf[self.module_number]["LED"]["LED"][
                    "Total_Number_of_LED_Modules"]:
            for i in self.attributes["brick"]:
                channels = list(self.modules_conf[i]["LED"]["LED"]["Channels"].split(","))
                for ii in channels:
                    self.attributes["brick"][i].get_configuration(ii)
                    self.attributes["brick"][i].set_configuration(ii, 'o', False)
                    self.attributes["brick"][i].set_pwm_configuration(ii, self.attributes["freq_LED"],
                                                                      self.attributes["Duty_Cycle_LED"])

    def initialize_tab(self):
        """
        Initializes GUI tab.

        """
        if self.modules_conf[self.module_number]["LED"]["LED"]["LED_Module"] == \
                self.modules_conf[self.module_number]["LED"]["LED"]["Total_Number_of_LED_Modules"]:
            self.gui["tab_number"] = General_functions.initialize_tab(self, ["+-Frq", "--Frq", "+-Hz", "--Hz"],
                                                                      copy.deepcopy(self.gui["tab_number"]))
        else:
            pass

    def draw_tab(self):
        """
        Draws GUI tab.
        """
        if self.modules_conf[self.module_number]["LED"]["LED"]["LED_Module"] == \
                self.modules_conf[self.module_number]["LED"]["LED"][
                    "Total_Number_of_LED_Modules"]:
            lcd = self.tk_attributes["lcd"]
            if lcd.get_gui_tab_selected() == self.attributes["Tab"][0]:
                lcd.clear_display()
                # lcd.set_gui_tab_selected(self.gui["tab_number"])
                LED_modules = []
                for i in self.modules_conf:
                    if 'LED' in self.modules_conf[i]:
                        LED_modules.append(i)
                counter = 0
                for i in LED_modules:
                    for ii in list(self.modules_conf[i]["LED"]["LED"]["Channel_Names"].split(",")):
                        lcd.draw_text(0, 8 * counter, lcd.FONT_6X8, lcd.COLOR_BLACK, ii)
                        counter += 1
                lcd.draw_text(55, 0, lcd.FONT_6X8, lcd.COLOR_BLACK,
                              'Frq.:' + str(self.attributes["freq_LED"] / 10) + 'Hz')
                lcd.draw_text(55, 24, lcd.FONT_6X8, lcd.COLOR_BLACK,
                              'ON/OFF:' + str(self.attributes["Duty_Cycle_LED"] / 100) + '%')

                lcd.set_gui_button(self.attributes["+-Frq"], 75, 10, 10, 10, "+")  # Tune pulse frequnecy of LED
                lcd.set_gui_button(self.attributes["--Frq"], 100, 10, 10, 10, "-")  # Tune pulse frequnecy of LED
                lcd.set_gui_button(self.attributes["+-Hz"], 75, 34, 10, 10, "+")  # Tune duty cycle of LED
                lcd.set_gui_button(self.attributes["--Hz"], 100, 34, 10, 10, "-")  # Tune duty cycle of LED

    def button_handling(self, button):
        """
        Assigns functions to GUI buttons.

        Parameters
        ----------
        button : boolean
            State of the pressed button.
        """
        if button == self.attributes["+-Frq"]:
            self.attributes[
                "freq_LED"] += 10  # LCD button "+" at position (75, 10) set LED pulse frequency increases by 1 Hz
        if button == self.attributes["--Frq"] and self.attributes["freq_LED"] > 10:
            self.attributes[
                "freq_LED"] -= 10  # LCD button "-" at position (100, 10) set LED pulse frequency decreases by 1 Hz if frequency is above 1 Hz
        if button == self.attributes["+-Hz"]:
            self.attributes[
                "Duty_Cycle_LED"] += 500  # LCD button "+" at position (75, 34) set duty cycle increases by 5 %
        if button == self.attributes["--Hz"] and self.attributes["Duty_Cycle_LED"] > 0:
            self.attributes[
                "Duty_Cycle_LED"] -= 500  # LCD button "-" at position (100, 34) set duty cycle decreases by 5 % if duty cycle is above 0 %
        self.draw_tab()
        self.set_parameters()

    @property
    def log(self):
        """
        Logs frequency and duty cycle in a log list.

        Returns
        ------
        list
            A list with header and logged frequency and duty cycle.
        """

        header = ["Timestamp",
                  "LED freq./Hz",
                  "Duty Cycle/%"
                  ]
        log_data = [time.asctime(time.localtime()),
                    self.attributes["freq_LED"],
                    self.attributes["Duty_Cycle_LED"]]
        if self.logs == []:
            self.logs.append(header)
        self.logs.append(log_data)
        return self.logs


class Stirrer:
    """
    A class used to ensure the functions of the Stirring Module

    ...

    Attributes
    ----------
    module_number : str
        Number of the module "module_5".
    tk_attributes : dict
        Dictionary with with tinkerforge bricklet specific information.
    modules_conf : dict
        Configurations of the connected modules e.g. Stirrer Module corresponds to key "module_5".
    gui : dict
        Dictionary with gui specific key value pairs.
    name : str
        Name of the module "Stirrer".
    attributes : dict
        Dictionary with Stirrer specific key value pairs.
    used_module : str
        "module_2" is the key in dict initialized_UID to get to the ID of the tinkerforge I/O bricklet.
    logs : list
        A list with the logged data.

    """
    from tinkerforge.bricklet_io4_v2 import BrickletIO4V2




    def __init__(self, module_number, tk_attributes, modules_conf, gui):
        self.name = "Stirrer"
        self.tk_attributes = tk_attributes
        self.modules_conf = modules_conf
        self.attributes = {}
        self.attributes["RPM"] = 1000
        self.attributes["Duty_Cycle"] = self.conv_duty_cycle(self.attributes["RPM"])
        self.module_number = module_number
        self.used_module = ""
        self.logs = []
        self.gui = gui
        self.initialize_tab()

    def conv_duty_cycle(self, RPM):
        """
        Converts RPM GUI input to corresponding duty cycle value.

        Parameters
        ----------
        RPM : int
            Set value for stirrer RPM.

        Returns
        ------
        float
            Calculated value for duty cycle corresponding to stirrer RPM.
        """
        PWM = 1.3191 * RPM - 562.85
        return PWM

    def set_instances(self, modules_instances):
        """
        Set the required instances of installed stirring module to enable joint use of I/O Bricklet with other modules.

        Parameters
        ----------
        modules_instances : dict
            Key value pairs of connected modules.
        """
        # check how the correct instance can be transfered -> use conf file
        self.attributes["Installed_Modules"] = []
        tk_instances = modules_instances
        for i in self.modules_conf:
            try:
                self.attributes["Installed_Modules"].append(tk_instances[i])
            except:
                pass

    def connect(self, instance=None):
        """
        Builds up the IP connection for the used tinkerforge bricklets.

        Returns
        ------
        list
            Tinkerforge bricklet UIDs.
        """
        UID_list = []
        self.attributes["brick"] = {}
        UID = self.modules_conf[self.module_number][list(self.modules_conf[self.module_number].keys())[0]][self.name][
            "UID"]
        if instance:
            for i in self.attributes["Installed_Modules"]:
                if i.module_number != self.module_number:
                    try:
                        if instance.attributes['brick'][i.module_number].uid_string == UID:
                            self.attributes["brick"][i.module_number] = instance.attributes['brick'][i.module_number]
                            self.used_module = i.module_number
                    except:
                        pass
        else:
            self.attributes["brick"][self.module_number] = self.BrickletIO4V2(UID, self.tk_attributes["ipcon"])
        UID_list.append(UID)
        self.set_parameters()
        return UID_list

    def set_parameters(self):
        """
        Sets channel of I/O bricklet, frequency of pwm signal and the duty cycle.
        """
        channels = list(self.modules_conf[self.module_number]["Stirrer"]["Stirrer"]["Channels"].split(","))
        for ii in channels:
            self.attributes["brick"][self.used_module].set_configuration(ii, 'o', True)
            self.attributes["brick"][self.used_module].set_pwm_configuration(ii, 250000, self.attributes["Duty_Cycle"])

    def initialize_tab(self):
        """
        Initializes GUI tab.
        """
        self.gui["tab_number"] = General_functions.initialize_tab(self, ["+", "-"],
                                                                  copy.deepcopy(self.gui["tab_number"]))

    def draw_tab(self):
        """
        Draws GUI tab.
        """
        lcd = self.tk_attributes["lcd"]
        if lcd.get_gui_tab_selected() == self.attributes["Tab"][0]:
            lcd.clear_display()
            # lcd.set_gui_tab_selected(self.gui["tab_number"])
            LED_modules = []
            lcd.draw_text(0, 10, lcd.FONT_6X8, lcd.COLOR_BLACK, 'velocity: ' + str(self.attributes["RPM"]) + ' rpm')
            lcd.set_gui_button(self.attributes["+"], 52, 30, 10, 10, "+")
            lcd.set_gui_button(self.attributes["-"], 67, 30, 10, 10, "-")

    def button_handling(self, button):
        """
        Assigns functions to GUI buttons.

        Parameters
        ----------
        button : boolean
            State of the pressed button.
        """
        if button == self.attributes["+"] and self.attributes["RPM"] < 2300:
            self.attributes["RPM"] += 50  # LCD button "+" set RPM increases by 50 if RPM is beneath 2300
        if button == self.attributes["-"] and self.attributes["RPM"] > 650:
            self.attributes["RPM"] -= 50  # LCD button "-" set RPM decreases by 50 if RPM is above 650
        self.attributes["Duty_Cycle"] = self.conv_duty_cycle(self.attributes["RPM"])
        self.draw_tab()
        self.set_parameters()

    @property
    def log(self):
        """
        Logs stirrer RPM in a log list.

        Returns
        ------
        list
            A list with header and logged stirrer RPM.
        """
        header = ["Timestamp",
                  "Stirrer RPM/(1/min)",
                  ]
        log_data = [time.asctime(time.localtime()),
                    self.attributes["RPM"]]
        if self.logs == []:
            self.logs.append(header)
        self.logs.append(log_data)
        return self.logs


class Fan:
    """
    A class used to ensure the functions of the Fan Module

    ...

    Attributes
    ----------
    module_number : str
        Number of the module "module_3".
    tk_attributes : dict
        Dictionary with with tinkerforge bricklet specific information.
    modules_conf : dict
        Configurations of the connected modules e.g. Fan Module corresponds to key "module_3".
    gui : dict
        Dictionary with gui specific key value pairs.
    name : str
        Name of the module "Fan".
    attributes : dict
        Dictionary with Fan specific key value pairs.
    used_module : str
        "module_2" is the key in dict initialized_UID to get to the ID of the tinkerforge I/O bricklet.
    logs : list
        A list with the logged data.

    """
    from tinkerforge.bricklet_io4_v2 import BrickletIO4V2



    def __init__(self, module_number, tk_attributes, modules_conf, gui):
        self.name = "Fan"
        self.tk_attributes = tk_attributes
        self.modules_conf = modules_conf
        self.attributes = {}
        self.attributes["RPM"] = 100  # Percent
        self.attributes["Duty_Cycle"] = self.conv_duty_cycle(self.attributes["RPM"])
        self.module_number = module_number
        self.used_module = ""
        self.logs = []
        self.gui = gui
        if self.modules_conf[self.module_number][self.name][self.name]["Tab_Text"] != "---":
            self.initialize_tab()

    def conv_duty_cycle(self, RPM):
        """
        Converts RPM GUI input to corresponding duty cycle value.

        Parameters
        ----------
        RPM : int
            Set value for stirrer RPM.

        Returns
        ------
        float
            Calculated value for duty cycle corresponding to stirrer RPM.
        """
        PWM = RPM * 100
        return PWM

    def set_instances(self, modules_instances):
        """
        Set the required instances of installed fan module to enable joint use of I/O Bricklet with other modules.
        Parameters
        ----------
        modules_instances : dict
            Key value pairs of connected modules.
        """
        # check how the correct instance can be transfered -> use conf file
        self.attributes["Installed_Modules"] = []
        tk_instances = modules_instances
        for i in self.modules_conf:
            try:
                self.attributes["Installed_Modules"].append(tk_instances[i])
            except:
                pass

    def connect(self, instance=None):
        """
        Builds up the IP connection for the used tinkerforge bricklets.

        Returns
        ------
        list
            Tinkerforge bricklet UIDs.
        """
        UID_list = []
        self.attributes["brick"] = {}
        UID = self.modules_conf[self.module_number][list(self.modules_conf[self.module_number].keys())[0]][self.name][
            "UID"]
        if instance:
            for i in self.attributes["Installed_Modules"]:
                if i.module_number != self.module_number:
                    try:
                        if instance.attributes['brick'][i.module_number].uid_string == UID:
                            self.attributes["brick"][i.module_number] = instance.attributes['brick'][i.module_number]
                            self.used_module = i.module_number
                    except:
                        pass
        else:
            self.attributes["brick"][self.module_number] = self.BrickletIO4V2(UID, self.tk_attributes["ipcon"])
        UID_list.append(UID)
        self.set_parameters()
        return UID_list

    def set_parameters(self):
        """
        Sets channel of I/O bricklet, frequency of pwm signal and the duty cycle.
        """
        channels = list(self.modules_conf[self.module_number][self.name][self.name]["Channels"].split(","))
        for ii in channels:
            self.attributes["brick"][self.used_module].set_configuration(ii, 'o', True)
            self.attributes["brick"][self.used_module].set_pwm_configuration(ii, 250000, self.attributes["Duty_Cycle"])

    def initialize_tab(self):
        """
        Initializes GUI tab.

        """
        self.gui["tab_number"] = General_functions.initialize_tab(self, ["+", "-"],
                                                                  copy.deepcopy(self.gui["tab_number"]))

    def draw_tab(self):
        """
        Draws GUI tab.
        """
        lcd = self.tk_attributes["lcd"]
        if lcd.get_gui_tab_selected() == self.attributes["Tab"][0]:
            lcd.clear_display()
            # lcd.set_gui_tab_selected(self.gui["tab_number"])
            LED_modules = []
            lcd.draw_text(0, 10, lcd.FONT_6X8, lcd.COLOR_BLACK, 'speed: ' + str(self.attributes["RPM"]) + ' %')
            lcd.set_gui_button(self.attributes["+"], 52, 30, 10, 10, "+")
            lcd.set_gui_button(self.attributes["-"], 67, 30, 10, 10, "-")

    def button_handling(self, button):
        """
        Assigns functions to GUI buttons.

        Parameters
        ----------
        button : boolean
            State of the pressed button.
        """
        if button == self.attributes["+"] and self.attributes["RPM"] < 100:
            self.attributes["RPM"] += 5  # LCD button "+" set RPM increases by 5 if RPM is beneath 100
        if button == self.attributes["-"] and self.attributes["RPM"] > 5:
            self.attributes["RPM"] -= 5  # LCD button "-" set RPM decreases by 5 if RPM is above 5
        self.attributes["Duty_Cycle"] = self.conv_duty_cycle(self.attributes["RPM"])
        self.draw_tab()
        self.set_parameters()

    @property
    def log(self):
        """
        Logs fan RPM in a log list.

        Returns
        ------
        list
            A list with header and logged fan RPM.
        """
        header = ["Timestamp",
                  "Fan RPM/(1/min)",
                  ]
        log_data = [time.asctime(time.localtime()),
                    self.attributes["RPM"]]
        if self.logs == []:
            self.logs.append(header)
        self.logs.append(log_data)
        return self.logs


class Tempering:
    """
    A class used to ensure the functions of the Tempering Module

    ...

    Attributes
    ----------
    module_number : str
        Number of the module "module_0".
    tk_attributes : dict
        Dictionary with with tinkerforge bricklet specific information.
    modules_conf : dict
        Configurations of the connected modules e.g. Tempering Module corresponds to key "module_0".
    gui : dict
        Dictionary with gui specific key value pairs.
    name : str
        Name of the module "Tempering".
    attributes : dict
        Dictionary with pid specific key value pairs.
    logs : list
        A list with the logged data.
    pid : class
        Class simple_pid.

    """
    from tinkerforge.bricklet_industrial_dual_relay import BrickletIndustrialDualRelay
    from tinkerforge.bricklet_thermocouple_v2 import BrickletThermocoupleV2
    from tinkerforge.bricklet_temperature_v2 import BrickletTemperatureV2
    from simple_pid import PID
    import threading


    def __init__(self,module_number,tk_attributes,modules_conf,gui):
        self.name = "Tempering"
        self.tk_attributes = tk_attributes
        self.modules_conf = modules_conf
        self.module_number = module_number
        self.attributes = {}
        self.attributes["P"] = 3
        self.attributes["I"] = 0.0001
        self.attributes["D"] = 0.01
        self.attributes["ambTemp"] = 25
        self.attributes["SetTemp"] = 25
        self.attributes["temperature_irrad"] = 25
        self.attributes["temperature_reactor"] = 25
        self.attributes["PID_tune"] = False
        self.attributes["Target_Temp"] = self.modules_conf[self.module_number][self.name][self.name]["Target_temp"]
        self.attributes["PID_sample_time"] = int(self.modules_conf[self.module_number][self.name][self.name]["PID_sample_time"])
        self.attributes["PID_output_limit"] = self.modules_conf[self.module_number][self.name][self.name]["PID_output_limit"]
        self.attributes["Offset"] = float(self.modules_conf[self.module_number][self.name][self.name]["Offset"])
        self.logs = []
        self.gui = gui
        self.attributes["Installed_Modules"] = self.modules_conf[self.module_number][self.name].sections()
        self.attributes["Installed_Modules"].remove(self.name)
        self.initialize_tab()
        self.pid = self.PID()
        self.pid.tunings = (self.attributes["P"],self.attributes["I"],self.attributes["D"])
        self.pid.setpoint = self.attributes["SetTemp"]
        self.pid.auto_mode = self.attributes["PID_tune"]
        self.pid.sample_time = int(self.attributes["PID_sample_time"])/1000
        self.pid.output_limits = tuple([int(number)/1000 for number in self.attributes["PID_output_limit"].split(",")])

    def connect(self):
        """
        Builds up the IP connection for the used tinkerforge bricklets.

        Returns
        ------
        list
            Tinkerforge bricklet UIDs.
        """
        UID_list = []
        self.attributes["brick"] = {}
        self.attributes["brick"][self.module_number] = {}
        for i in self.attributes["Installed_Modules"]:
            UID = self.modules_conf[self.module_number][self.name][i]["UID"]
            bricktype = self.modules_conf[self.module_number][self.name][i]["Bricklet_Type"]
            call = "self."+ bricktype + '(UID, self.tk_attributes["ipcon"])'
            self.attributes["brick"][self.module_number][i] = eval(call)
            brick = "self.attributes['brick'][self.module_number][i]"
            callback = self.modules_conf[self.module_number][self.name][i]['Callback']
            callback_target = self.modules_conf[self.module_number][self.name][i]['Callback_target']
            if callback_target != "---":
                call = brick + ".register_callback(" + "self."+ bricktype + "." + callback + ", " + callback_target + ")"
                eval(call)
            callback_conf = self.modules_conf[self.module_number][self.name][i]['Callback_conf']
            if callback_conf != "---":
                call = brick + "." + callback_conf
                eval(call)
            UID_list.append(UID)
        self.init_tempering()
        return UID_list

    def cb_amb_temperature(self,temp):
        """
        Divides initial temperature readout value by 100 to get to a output value in °C.

        Parameters
        ----------
        temp : int
            Temperature value output (2500 = 25°C).
        """
        self.attributes["ambTemp"] = temp/100
        self.draw_tab()

    def cb_react_temperature(self,temp):
        """
        Divides initial temperature readout value by 100 to get to a output value in °C.

        Parameters
        ----------
        temp : int
            Temperature value output (2500 = 25°C).
        """
        self.attributes["temperature_reactor"] = temp/100
        self.draw_tab()

    def cb_irrad_temperature(self,temp):
        """
        Divides initial temperature readout value by 100 to get to a output value in °C.

        Parameters
        ----------
        temp : int
            Temperature value output (2500 = 25°C).
        """
        self.attributes["temperature_irrad"] = temp/100
        self.draw_tab()

    def init_tempering(self):
        """
        Assigns dual relay bricklet for cooling and heating and closes all relays.
        """
        cooling_brick = self.attributes["brick"][self.module_number]["Cooling"]
        heating_brick = self.attributes["brick"][self.module_number]["Heating"]
        heating_brick.set_value(False, False)
        cooling_brick.set_value(False, False)

    def cb_tempering(self,channel,value):
        """
        Switches relays of dual relay bricklets on and off to enable cooling or heating and assigns monoflop time for bricklets.

        """
        cooling_brick = self.attributes["brick"][self.module_number]["Cooling"]
        heating_brick = self.attributes["brick"][self.module_number]["Heating"]
        self.pid.auto_mode = self.attributes["PID_tune"]
        if self.attributes["PID_tune"] == True:
            self.attributes["PID_sample_time"] = self.pid(self.attributes["temperature_irrad"])
            monoflop_time = self.attributes["PID_sample_time"] * 1000
            # print(self.pid.setpoint," ",monoflop_time)
            threshold = 500
            if monoflop_time >= threshold:
                #print('turn on heater')
                heating_brick.set_monoflop(0, True, monoflop_time)
                cooling_brick.set_monoflop(1, True, monoflop_time)
            elif monoflop_time > threshold*-1 and monoflop_time < threshold:
                #print('turn on heater')
                self.threading.Timer(0.5, self.cb_tempering,(0,True)).start()
                # heating_brick.set_monoflop(0, False, 500)
                # heating_brick.set_monoflop(1, False, 500)
                # cooling_brick.set_monoflop(0, False, 500)
                # cooling_brick.set_monoflop(1, False, 500)
            elif monoflop_time < threshold*-1:
                #print('turn on cooler')
                heating_brick.set_monoflop(1, True, monoflop_time*-1)
                cooling_brick.set_monoflop(0, True, monoflop_time*-1)


    def initialize_tab(self):
        """
        Initializes GUI tab.
        """
        self.gui["tab_number"] =  General_functions.initialize_tab(self,["+-SetTemp","--SetTemp","PID_on","PID_off"],copy.deepcopy(self.gui["tab_number"]))

    def draw_tab(self):
        """
        Draws GUI tab.
        """
        lcd = self.tk_attributes["lcd"]
        if lcd.get_gui_tab_selected() == self.attributes["Tab"][0]:# todo find tab number from dict value
            lcd.clear_display()

            lcd.draw_text(0, 0, lcd.FONT_6X8, lcd.COLOR_BLACK,'AmbTemp:' + str(self.attributes["ambTemp"])+ ' \xF8C')
            lcd.draw_text(0, 10, lcd.FONT_6X8, lcd.COLOR_BLACK,'SetTemp:' + "{:.1f}".format(self.attributes["SetTemp"] + self.attributes["Offset"])+ ' \xF8C')
            lcd.draw_text(0, 20, lcd.FONT_6X8, lcd.COLOR_BLACK,'ChambTemp:' + str(self.attributes["temperature_irrad"]) + ' \xF8C')
            lcd.draw_text(0, 30, lcd.FONT_6X8, lcd.COLOR_BLACK,'RctTemp:' + str(self.attributes["temperature_reactor"]) + ' \xF8C')
            lcd.draw_text(0, 40, lcd.FONT_6X8, lcd.COLOR_BLACK,'PID_on:' + str(self.attributes["PID_tune"]))

            lcd.set_gui_button(self.attributes["+-SetTemp"], 100, 10, 10, 10, "+")
            lcd.set_gui_button(self.attributes["--SetTemp"], 115, 10, 10, 10, "-")
            lcd.set_gui_button(self.attributes["PID_on"], 80, 40, 20, 10, "on")
            lcd.set_gui_button(self.attributes["PID_off"], 105, 40, 22, 10, "off")

    def button_handling(self,button):
        """
        Assigns functions to GUI buttons.

        Parameters
        ----------
        button : boolean
            State of the pressed button.
        """
        if button == self.attributes["+-SetTemp"]:
            self.attributes["SetTemp"] += 0.1
        if button == self.attributes["--SetTemp"]:
            self.attributes["SetTemp"] -= 0.1
        if button == self.attributes["PID_on"]:
            self.attributes["PID_tune"] = True
        if button == self.attributes["PID_off"]:
            self.attributes["PID_tune"] = False
        self.pid.setpoint = self.attributes["SetTemp"]
        self.draw_tab()
        self.cb_tempering(0,True)

    @property
    def log(self):
        """
        Logs desired- , irradiation chamber- , reactor- and ambient temperature together with the PID state in a log list.

        Returns
        ------
        list
            A list with header and logged desired- , irradiation chamber- , reactor- and ambient temperature together with the PID state.
        """
        header = ["Timestamp",
                  "Desired Temp./°C",
                  "Ambient Temp./°C",
                  "Irrad. Chamber Temp./°C",
                  "Reactor Temp./°C",
                  "PID On"]
        log_data = [time.asctime(time.localtime()),
                    self.attributes["SetTemp"],
                    self.attributes["ambTemp"],
                    self.attributes["temperature_irrad"],
                    self.attributes["temperature_reactor"],
                    self.attributes["PID_tune"]]
        if self.logs == []:
            self.logs.append(header)
        self.logs.append(log_data)
        return self.logs
