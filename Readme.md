# modularPhotoreactor

A modular and characterized open source photoreactor and the mutli-batch screening phototreactor extension

## Documentation

The assembly of the devices is documented in the [CAD section](./01_CAD/).

See also the 3D-pdfs for detailed assembly instructions in the [assembly section](./03_ASSEMBLY_INSTRUCTIONS/).

The Python modules for the operation of the reactor controller are documented in the repository [Py4ModPhotoreactor](https://github.com/photonZfeed/Py4ModPhotoreactor). See also the fairly detailed docstrings in the code. 



## Folder Structure

```
📦HARDWARE_Modular_Photoreactor
 ┣ 📂01_CAD
 ┃ ┣ 📂00_Corpus
 ┃ ┃ ┣ 📂00_Corpus_90x90x100mm
 ┃ ┃ ┃ ┣ 📂00_corpus
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90x100mm_back_wall.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90x100mm_front_wall.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90x100mm_side_walls.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90x100mm_side_walls_LED_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_cover.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_stand.stl
 ┃ ┃ ┃ ┣ 📂01_irradiation_module
 ┃ ┃ ┃ ┃ ┣ 📜20210104_Thorlabsl_modul.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Max350.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Max350_adapter.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_starcool.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Thorlabs.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Thorlabs_adapter.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_90x90mm_irrad_Thorlabs_collimator.stl
 ┃ ┃ ┃ ┣ 📂02_stirring_module
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_stirring_module.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_stirring_module_holder_electric_motor.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_stirring_module_magnet_holder.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_90x90mm_stirring_module_magnet_holder_blind_plug.stl
 ┃ ┃ ┃ ┗ 📂03_sample_holders
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_10S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_10S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_1S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_1S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_4S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_4S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_6S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_6S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_8S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_8S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_8mL_GCvial_ND13_10S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_90x90mm_8mL_GCvial_ND13_1S_alignment_holder.stl
 ┃ ┃ ┣ 📂01_Corpus_90x90x140mm
 ┃ ┃ ┃ ┣ 📂00_corpus
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90x140mm_back_wall.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90x140mm_front_wall.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90x140mm_side_walls.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_cover.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_stand.stl
 ┃ ┃ ┃ ┣ 📂01_irradiation_module
 ┃ ┃ ┃ ┃ ┣ 📜20210104_Thorlabsl_modul.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Max350.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Max350_adapter.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_starcool.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Thorlabs.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_irrad_Thorlabs_adapter.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_90x90mm_irrad_Thorlabs_collimator.stl
 ┃ ┃ ┃ ┣ 📂02_stirring_module
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_stirring_module.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_stirring_module_holder_electric_motor.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_stirring_module_magnet_holder.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_90x90mm_stirring_module_magnet_holder_blind_plug.stl
 ┃ ┃ ┃ ┗ 📂03_sample_holders
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_10S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_10S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_1S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_1S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_4S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_4S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_6S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_6S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_8S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_4mL_GCvial_ND13_8S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_90x90mm_8mL_GCvial_ND13_10S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_90x90mm_8mL_GCvial_ND13_1S_alignment_holder.stl
 ┃ ┃ ┗ 📂02_Corpus_130x130x130mm
 ┃ ┃ ┃ ┣ 📂00_corpus
 ┃ ┃ ┃ ┃ ┣ 📜corpus130x130mm_side_walls.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_back_wall.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_cover.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_front_wall_monting_thermal_hose.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_side_wall_left.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_side_wall_right.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_stand_20mm.stl
 ┃ ┃ ┃ ┃ ┣ 📜fin_back_wall.stl
 ┃ ┃ ┃ ┃ ┣ 📜fin_front_wall.stl
 ┃ ┃ ┃ ┃ ┣ 📜spacer_side_walls_5mm.stl
 ┃ ┃ ┃ ┃ ┗ 📜spacer_stand_5mm.stl
 ┃ ┃ ┃ ┣ 📂01_irradiation_module
 ┃ ┃ ┃ ┃ ┗ 📜irrad_module.stl
 ┃ ┃ ┃ ┣ 📂02_sample_holders
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_GCvial_ND13_18S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_GCvial_ND13_18S_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜corpus_130x130mm_GCvial_ND13_1S_alignment_holder.stl
 ┃ ┃ ┃ ┃ ┗ 📜corpus_130x130mm_GCvial_ND13_1S_holder.stl
 ┃ ┃ ┃ ┗ 📂03_tempering_module
 ┃ ┃ ┃ ┃ ┣ 📜back_mounting_thermo_hose.stl
 ┃ ┃ ┃ ┃ ┣ 📜fan_holder.stl
 ┃ ┃ ┃ ┃ ┣ 📜holder_tempering_module.stl
 ┃ ┃ ┃ ┃ ┣ 📜mounting_alu_water_cooler.stl
 ┃ ┃ ┃ ┃ ┗ 📜spacer_holder_tempering_module.stl
 ┃ ┣ 📂01_Controller
 ┃ ┃ ┣ 📜controller_case.stl
 ┃ ┃ ┣ 📜controller_case_LCD_holder.stl
 ┃ ┃ ┗ 📜controller_electronic_board_holder.stl
 ┃ ┣ 📂02_Peripheral_Modules
 ┃ ┃ ┣ 📂00_ambient_temperature
 ┃ ┃ ┃ ┣ 📜base_plate_ambient_temperature_extension.stl
 ┃ ┃ ┃ ┗ 📜case_ambient_temperature_extension.stl
 ┃ ┃ ┣ 📂01_tempering_extension
 ┃ ┃ ┃ ┣ 📜base_plate.stl
 ┃ ┃ ┃ ┗ 📜case_tempering_extension.stl
 ┃ ┃ ┣ 📂02_master_extension
 ┃ ┃ ┃ ┣ 📜base_plate.stl
 ┃ ┃ ┃ ┗ 📜case_master_extension.stl
 ┃ ┃ ┣ 📂03_membrane_pump_extension
 ┃ ┃ ┃ ┣ 📜base_plate_membrane_pump.stl
 ┃ ┃ ┃ ┣ 📜base_plate_membrane_pump_exension.stl
 ┃ ┃ ┃ ┣ 📜case_membrane_pump.stl
 ┃ ┃ ┃ ┗ 📜case_membrane_pump_extension.stl
 ┃ ┃ ┗ 📂04_pressure_sensor_extension
 ┃ ┃ ┃ ┣ 📜base_plate.stl
 ┃ ┃ ┃ ┣ 📜base_plate_updated.stl
 ┃ ┃ ┃ ┣ 📜case_pressure_extension.stl
 ┃ ┃ ┃ ┗ 📜case_pressure_extension_updated.stl
 ┃ ┗ 📂03_Multi_Batch_Screening_Photoreactor
 ┃ ┃ ┣ 📂00_Base_Module
 ┃ ┃ ┃ ┗ 📜Base_Module.stl
 ┃ ┃ ┣ 📂01_Irradiation_Module
 ┃ ┃ ┃ ┣ 📜300mm_alu_heatsink.stl
 ┃ ┃ ┃ ┣ 📜heatsink_holder_left.stl
 ┃ ┃ ┃ ┣ 📜heatsink_holder_right.stl
 ┃ ┃ ┃ ┗ 📜stand_irradiation_module.stl
 ┃ ┃ ┣ 📂02_Reflector_Module
 ┃ ┃ ┃ ┣ 📜PTFE_Side_Wall.stl
 ┃ ┃ ┃ ┣ 📜Reflector_Holder_Nut.stl
 ┃ ┃ ┃ ┗ 📜Reflector_Holder_Screw.stl
 ┃ ┃ ┣ 📂03_Mobile_Cover
 ┃ ┃ ┃ ┣ 📜back.stl
 ┃ ┃ ┃ ┣ 📜connector.stl
 ┃ ┃ ┃ ┣ 📜front.stl
 ┃ ┃ ┃ ┣ 📜sides.stl
 ┃ ┃ ┃ ┗ 📜top.stl
 ┃ ┃ ┗ 📂04_Accesories
 ┃ ┃ ┃ ┗ 📂00_UV_Vis_Cell_4mL_GC_Vial
 ┃ ┃ ┃ ┃ ┣ 📜UV_vis_cell_4mL_GC_vial_SLA.png
 ┃ ┃ ┃ ┃ ┗ 📜UV_vis_cell_4mL_GC_vial_SLA.stl
 ┣ 📂02_MATERIALS
 ┃ ┣ 📂00_electronics
 ┃ ┃ ┣ 📂00_Tinkerforge
 ┃ ┃ ┃ ┗ 📜Tinkerforge.txt
 ┃ ┃ ┣ 📂01_LEDs
 ┃ ┃ ┃ ┣ 📂blue
 ┃ ┃ ┃ ┃ ┣ 📂453nm
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LZ4-00B208-0000.txt
 ┃ ┃ ┃ ┃ ┣ 📂455nm
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LST1-01F06-RYL1-00.txt
 ┃ ┃ ┃ ┃ ┗ 📂460nm
 ┃ ┃ ┃ ┃ ┃ ┣ 📜5412869-LED_2520Engin_Datasheet_LuxiGen_LZ1-00DB00-1532005.pdf
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LZ1-00DB00.txt
 ┃ ┃ ┃ ┣ 📂green
 ┃ ┃ ┃ ┃ ┗ 📂530nm
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LST1-01F06-GRN1-00.txt
 ┃ ┃ ┃ ┣ 📂RGBA
 ┃ ┃ ┃ ┃ ┗ 📜LZ4-20MA00-0000.txt
 ┃ ┃ ┃ ┗ 📂UV
 ┃ ┃ ┃ ┃ ┣ 📂365nm
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LST1-01G01-UV01-00.txt
 ┃ ┃ ┃ ┃ ┣ 📂385nm
 ┃ ┃ ┃ ┃ ┃ ┗ 📜LZ1-10UB00-01U4.txt
 ┃ ┃ ┃ ┃ ┗ 📂405nm
 ┃ ┃ ┃ ┃ ┃ ┣ 📂onecore
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜LZ1-10UB00-01U7.txt
 ┃ ┃ ┃ ┃ ┃ ┗ 📂quadcore
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜LZ4-V0UB0R-00U8.txt
 ┃ ┃ ┣ 📂02_raspberry_pi
 ┃ ┃ ┃ ┗ 📜raspberry_pi_4_8GB.txt
 ┃ ┃ ┣ 📂03_sd_card
 ┃ ┃ ┃ ┗ 📜SD_card.txt
 ┃ ┃ ┣ 📂04_peltier_element
 ┃ ┃ ┃ ┣ 📜datenblatt-189115-tru-components-tec1-12706-peltier-element-15-v-64-a-65-w-l-x-b-x-h-40-x-40-x-38-mm.pdf
 ┃ ┃ ┃ ┗ 📜peltier.txt
 ┃ ┃ ┣ 📂05_power_supplies
 ┃ ┃ ┃ ┣ 📂00_12V_5A
 ┃ ┃ ┃ ┃ ┗ 📜12V_5A.txt
 ┃ ┃ ┃ ┗ 📂00_24V_6A
 ┃ ┃ ┃ ┃ ┗ 📜24V_6A.txt
 ┃ ┃ ┣ 📂06_small_parts
 ┃ ┃ ┃ ┣ 📂00_stripboard
 ┃ ┃ ┃ ┃ ┗ 📜stripboard_WR_914-HP.txt
 ┃ ┃ ┃ ┣ 📂01_connection_jacks
 ┃ ┃ ┃ ┃ ┣ 📜2Pin_PCB_Mount_2.5mm_Pitch.txt
 ┃ ┃ ┃ ┃ ┣ 📜2Pin_PCB_Mount_5mm_Pitch.txt
 ┃ ┃ ┃ ┃ ┣ 📜banana_plug_female.txt
 ┃ ┃ ┃ ┃ ┣ 📜banana_plug_male.txt
 ┃ ┃ ┃ ┃ ┣ 📜Cable_extension_PWM_4-Pin_Moltex.txt
 ┃ ┃ ┃ ┃ ┣ 📜DC_Jack.txt
 ┃ ┃ ┃ ┃ ┗ 📜wago_2Conductur_clamp.txt
 ┃ ┃ ┃ ┣ 📂02_Stacking_Header_Raspberry_Pi
 ┃ ┃ ┃ ┃ ┗ 📜Stacking_Header_Raspberry_Pi.txt
 ┃ ┃ ┃ ┣ 📂03_two_position_switch
 ┃ ┃ ┃ ┃ ┗ 📜two_position_switch.txt
 ┃ ┃ ┃ ┗ 📂04_silicone_wire
 ┃ ┃ ┃ ┃ ┗ 📜silicone_wire.txt
 ┃ ┃ ┣ 📂07_LED_drivers
 ┃ ┃ ┃ ┣ 📜350mA_driver.txt
 ┃ ┃ ┃ ┣ 📜500mA_driver.txt
 ┃ ┃ ┃ ┗ 📜700mA_driver.txt
 ┃ ┃ ┣ 📂08_membrane_pump
 ┃ ┃ ┃ ┣ 📜accessories_membrane_pump.txt
 ┃ ┃ ┃ ┗ 📜Membrane_Pump.txt
 ┃ ┃ ┗ 📂09_fans
 ┃ ┃ ┃ ┣ 📂00_fan_corpus_90x90mm
 ┃ ┃ ┃ ┃ ┗ 📜fan.txt
 ┃ ┃ ┃ ┣ 📂01_fan_corpus_130x130mm
 ┃ ┃ ┃ ┃ ┣ 📜fan.txt
 ┃ ┃ ┃ ┃ ┗ 📜fan_update.txt
 ┃ ┃ ┃ ┣ 📂02_power_supply_fan_corpus_90x90mm
 ┃ ┃ ┃ ┃ ┗ 📜power_supply.txt
 ┃ ┃ ┃ ┗ 📂03_Pi_Fan
 ┃ ┃ ┃ ┃ ┗ 📜Pi_Fan.txt
 ┃ ┗ 📂01_accessories
 ┃ ┃ ┣ 📂00_thermal_tube
 ┃ ┃ ┃ ┗ 📜thermal_hose.txt
 ┃ ┃ ┣ 📂01_hose_clamps
 ┃ ┃ ┃ ┗ 📜hose_clamp.txt
 ┃ ┃ ┣ 📂02_screws_nuts
 ┃ ┃ ┃ ┣ 📂00_M3_Set
 ┃ ┃ ┃ ┃ ┗ 📜M3_screw_set.txt
 ┃ ┃ ┃ ┣ 📂01_Nylon_Spacer
 ┃ ┃ ┃ ┃ ┗ 📜nylon_spacer.txt
 ┃ ┃ ┃ ┗ 📂02_M3_60mm
 ┃ ┃ ┃ ┃ ┗ 📜M3_60mm.txt
 ┃ ┃ ┣ 📂03_cooler
 ┃ ┃ ┃ ┣ 📂00_tempering_module_cooler
 ┃ ┃ ┃ ┃ ┣ 📂00_pelltier_cooler
 ┃ ┃ ┃ ┃ ┃ ┗ 📜Alpine AM4 Passive.txt
 ┃ ┃ ┃ ┃ ┗ 📂01_alu_water_cooler
 ┃ ┃ ┃ ┃ ┃ ┗ 📜alu_water_cooler.txt
 ┃ ┃ ┃ ┗ 📂01_LED_cooler
 ┃ ┃ ┃ ┃ ┣ 📂00_25mm_cooler
 ┃ ┃ ┃ ┃ ┃ ┗ 📜sink_s-1265491.txt
 ┃ ┃ ┃ ┃ ┣ 📂01_50mm_cooler
 ┃ ┃ ┃ ┃ ┃ ┗ 📜sink_s-1265491.txt
 ┃ ┃ ┃ ┃ ┗ 📂02_300mm_cooler
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ATS-EXL75-300-R0.txt
 ┃ ┃ ┣ 📂04_foam_rubber_seal
 ┃ ┃ ┃ ┗ 📜foam_rubber_seal.txt
 ┃ ┃ ┗ 📂05_PTFE
 ┃ ┃ ┃ ┣ 📂00_technical_PTFE
 ┃ ┃ ┃ ┃ ┗ 📜technical_PTFE.txt
 ┃ ┃ ┃ ┗ 📂01_optical_PTFE
 ┃ ┃ ┃ ┃ ┗ 📜optical_PTFE.txt
 ┣ 📂03_ASSEMBLY_INSTRUCTIONS
 ┃ ┣ 📂00_Corpus
 ┃ ┃ ┣ 📜Assembly_Photoreactor_Corpus_130x130x130mm.pdf
 ┃ ┃ ┣ 📜Assembly_Photoreactor_Corpus_90x90x140mm.pdf
 ┃ ┃ ┗ 📜Assembly_Photoreactor_Corpus_90x90x90mm.pdf
 ┃ ┣ 📂01_Controller
 ┃ ┃ ┣ 📜20211029_Stripboard_drill_holes.pdf
 ┃ ┃ ┣ 📜Controller_circuit_diagram.pdf
 ┃ ┃ ┣ 📜Controller_circuit_diagram.svg
 ┃ ┃ ┣ 📜Controller_Documentation.pdf
 ┃ ┃ ┣ 📜Controller_Documentation.svg
 ┃ ┃ ┣ 📜Logic_Controller.pdf
 ┃ ┃ ┣ 📜Logic_Controller.svg
 ┃ ┃ ┗ 📜Logic_Controller.vsdx
 ┃ ┣ 📂02_Peripheral_Modules
 ┃ ┃ ┣ 📂00_Tempering_Module
 ┃ ┃ ┃ ┣ 📜Peltier_Circuit_Diagram.pdf
 ┃ ┃ ┃ ┗ 📜Peltier_Circuit_Diagram.svg
 ┃ ┃ ┗ 📂01_LED_Driver_Module
 ┃ ┃ ┃ ┗ 📜LED Driver Module.pdf
 ┃ ┣ 📂03_Irradiation_Module
 ┃ ┃ ┗ 📜assembly_instruction_LED_cooler.pdf
 ┃ ┗ 📂04_Multi_Batch_Screening_Phororeactor
 ┃ ┃ ┣ 📂00_Photoreactor
 ┃ ┃ ┃ ┗ 📜Multi_Batch_Screening_Photoreactor_assembly.pdf
 ┃ ┃ ┗ 📂01_Mobile_Cover
 ┃ ┃ ┃ ┣ 📜Mobile_Cover_assembly.pdf
 ┃ ┃ ┃ ┗ 📜Mobile_Cover_assembly.stl
 ┗ 📂04_IMAGES
 ┃ ┗ 📜Licenses.png
```

## More Information

<!--- Cite this repository: [![DOI](https://zenodo.org/badge/368164449.svg)](https://zenodo.org/badge/latestdoi/368164449) --->



## Publications

* [Making Photocatalysis Comparable Using a Modular and Characterized Open-Source Photoreactor](https://chemistry-europe.onlinelibrary.wiley.com/doi/full/10.1002/cptc.202200044)

* [Making Photocatalysts Screenable - A Milli Scale Multi-Batch Screening Photoreactor as Extension for the Modular Photoreactor](https://fill_in_the_blank)