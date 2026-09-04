# modularPhotoreactor

A modular and characterized open source photoreactor and the mutli-batch screening phototreactor extension

## Documentation

The assembly of the devices is documented in the [CAD section](./01_CAD/).

See also the 3D-pdfs for detailed assembly instructions in the [assembly section](./03_ASSEMBLY_INSTRUCTIONS/).

The Python modules for the operation of the reactor controller are documented in the repository [Py4ModPhotoreactor](https://github.com/photonZfeed/Py4ModPhotoreactor). See also the fairly detailed docstrings in the code. 



## Folder Structure

```
📦HARDWARE_Modular_Photoreactor
┣ 📂 01_CAD
┃  ┣ 📂 00_Corpus
┃  ┃  ┣ 📂 00_Corpus_90x90x100mm
┃  ┃  ┃  ┣ 📂 00_corpus
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90x100mm_back_wall.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90x100mm_front_wall.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90x100mm_side_walls.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90x100mm_side_walls_LED_holder.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_cover.stl
┃  ┃  ┃  ┃  ┗ 📜 corpus_stand.stl
┃  ┃  ┃  ┣ 📂 01_irradiation_module
┃  ┃  ┃  ┃  ┣ 📜 20210104_Thorlabsl_modul.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Max350.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Max350_adapter.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_starcool.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Thorlabs.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Thorlabs_adapter.stl
┃  ┃  ┃  ┃  ┗ 📜 corpus_90x90mm_irrad_Thorlabs_collimator.stl
┃  ┃  ┃  ┣ 📂 02_stirring_module
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_stirring_module.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_stirring_module_holder_electric_motor.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_stirring_module_magnet_holder.stl
┃  ┃  ┃  ┃  ┗ 📜 corpus_90x90mm_stirring_module_magnet_holder_blind_plug.stl
┃  ┃  ┃  ┗ 📂 03_sample_holders
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_11mL_Biotage_MWvial_6S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_11mL_Biotage_MWvial_6S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_10S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_10S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_1S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_1S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_4S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_4S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_6S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_6S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_8S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_8S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_8mL_GCvial_ND13_10S_alignment_holder.stl
┃  ┃  ┃     ┗ 📜 corpus_90x90mm_8mL_GCvial_ND13_1S_alignment_holder.stl
┃  ┃  ┣ 📂 01_Corpus_90x90x140mm
┃  ┃  ┃  ┣ 📂 00_corpus
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90x140mm_back_wall.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90x140mm_front_wall.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90x140mm_side_walls.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_cover.stl
┃  ┃  ┃  ┃  ┗ 📜 corpus_stand.stl
┃  ┃  ┃  ┣ 📂 01_irradiation_module
┃  ┃  ┃  ┃  ┣ 📜 20210104_Thorlabsl_modul.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Max350.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Max350_adapter.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_starcool.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Thorlabs.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_irrad_Thorlabs_adapter.stl
┃  ┃  ┃  ┃  ┗ 📜 corpus_90x90mm_irrad_Thorlabs_collimator.stl
┃  ┃  ┃  ┣ 📂 02_stirring_module
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_stirring_module.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_stirring_module_holder_electric_motor.stl
┃  ┃  ┃  ┃  ┣ 📜 corpus_90x90mm_stirring_module_magnet_holder.stl
┃  ┃  ┃  ┃  ┗ 📜 corpus_90x90mm_stirring_module_magnet_holder_blind_plug.stl
┃  ┃  ┃  ┗ 📂 03_sample_holders
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_11mL_Biotage_MWvial_6S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_11mL_Biotage_MWvial_6S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_10S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_10S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_1S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_1S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_4S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_4S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_6S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_6S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_8S_alignment_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_4mL_GCvial_ND13_8S_holder.stl
┃  ┃  ┃     ┣ 📜 corpus_90x90mm_8mL_GCvial_ND13_10S_alignment_holder.stl
┃  ┃  ┃     ┗ 📜 corpus_90x90mm_8mL_GCvial_ND13_1S_alignment_holder.stl
┃  ┃  ┗ 📂 02_Corpus_130x130x130mm
┃  ┃     ┣ 📂 00_corpus
┃  ┃     ┃  ┣ 📜 corpus130x130mm_side_walls.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_back_wall.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_cover.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_front_wall_monting_thermal_hose.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_side_wall_left.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_side_wall_right.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_stand_20mm.stl
┃  ┃     ┃  ┣ 📜 fin_back_wall.stl
┃  ┃     ┃  ┣ 📜 fin_front_wall.stl
┃  ┃     ┃  ┣ 📜 spacer_side_walls_5mm.stl
┃  ┃     ┃  ┗ 📜 spacer_stand_5mm.stl
┃  ┃     ┣ 📂 01_irradiation_module
┃  ┃     ┃  ┗ 📜 irrad_module.stl
┃  ┃     ┣ 📂 02_sample_holders
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_GCvial_ND13_18S_alignment_holder.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_GCvial_ND13_18S_holder.stl
┃  ┃     ┃  ┣ 📜 corpus_130x130mm_GCvial_ND13_1S_alignment_holder.stl
┃  ┃     ┃  ┗ 📜 corpus_130x130mm_GCvial_ND13_1S_holder.stl
┃  ┃     ┗ 📂 03_tempering_module
┃  ┃        ┣ 📜 back_mounting_thermo_hose.stl
┃  ┃        ┣ 📜 fan_holder.stl
┃  ┃        ┣ 📜 holder_tempering_module.stl
┃  ┃        ┣ 📜 mounting_alu_water_cooler.stl
┃  ┃        ┗ 📜 spacer_holder_tempering_module.stl
┃  ┣ 📂 01_controller
┃  ┃  ┣ 📜 controller_case.stl
┃  ┃  ┣ 📜 controller_case_LCD_holder.stl
┃  ┃  ┗ 📜 controller_electronic_board_holder.stl
┃  ┣ 📂 02_Peripheral_Modules
┃  ┃  ┣ 📂 00_ambient_temperature
┃  ┃  ┃  ┣ 📜 base_plate_ambient_temperature_extension.stl
┃  ┃  ┃  ┗ 📜 case_ambient_temperature_extension.stl
┃  ┃  ┣ 📂 01_tempering_extension
┃  ┃  ┃  ┣ 📜 base_plate.stl
┃  ┃  ┃  ┗ 📜 case_tempering_extension.stl
┃  ┃  ┣ 📂 02_master_extension
┃  ┃  ┃  ┣ 📜 base_plate.stl
┃  ┃  ┃  ┗ 📜 case_master_extension.stl
┃  ┃  ┣ 📂 03_membrane_pump_extension
┃  ┃  ┃  ┣ 📜 base_plate_membrane_pump.stl
┃  ┃  ┃  ┣ 📜 base_plate_membrane_pump_exension.stl
┃  ┃  ┃  ┣ 📜 case_membrane_pump.stl
┃  ┃  ┃  ┗ 📜 case_membrane_pump_extension.stl
┃  ┃  ┗ 📂 04_pressure_sensor_extension
┃  ┃     ┣ 📜 base_plate.stl
┃  ┃     ┣ 📜 base_plate_updated.stl
┃  ┃     ┣ 📜 case_pressure_extension.stl
┃  ┃     ┗ 📜 case_pressure_extension_updated.stl
┃  ┣ 📂 03_Multi_Batch_Screening_Photoreactor
┃  ┃  ┣ 📂 00_Indirect_Irradiation_Module
┃  ┃  ┃  ┣ 📂 00_Base_Module
┃  ┃  ┃  ┃  ┗ 📜 Base_Module.stl
┃  ┃  ┃  ┣ 📂 01_Irradiation_Module
┃  ┃  ┃  ┃  ┣ 📜 300mm_alu_heatsink.stl
┃  ┃  ┃  ┃  ┣ 📜 heatsink_holder_left.stl
┃  ┃  ┃  ┃  ┣ 📜 heatsink_holder_right.stl
┃  ┃  ┃  ┃  ┗ 📜 stand_irradiation_module.stl
┃  ┃  ┃  ┣ 📂 02_Reflector_Module
┃  ┃  ┃  ┃  ┣ 📜 PTFE_Side_Wall.stl
┃  ┃  ┃  ┃  ┣ 📜 Reflector_Holder_Nut.stl
┃  ┃  ┃  ┃  ┗ 📜 Reflector_Holder_Screw.stl
┃  ┃  ┃  ┣ 📂 03_Mobile_Cover
┃  ┃  ┃  ┃  ┣ 📜 back.stl
┃  ┃  ┃  ┃  ┣ 📜 connector.stl
┃  ┃  ┃  ┃  ┣ 📜 front.stl
┃  ┃  ┃  ┃  ┣ 📜 sides.stl
┃  ┃  ┃  ┃  ┗ 📜 top.stl
┃  ┃  ┃  ┗ 📂 04_Accesories
┃  ┃  ┃     ┗ 📂 00_UV_Vis_Cell_4mL_GC_Vial
┃  ┃  ┃        ┣ 📜 UV_vis_cell_4mL_GC_vial_SLA.png
┃  ┃  ┃        ┗ 📜 UV_vis_cell_4mL_GC_vial_SLA.stl
┃  ┃  ┗ 📂 01_Direct_Irradiation_Module
┃  ┃     ┣ 📂 00_reflector_fixed_height
┃  ┃     ┃  ┣ 📜 corner_pillar_1.stl
┃  ┃     ┃  ┣ 📜 corner_pillar_2.stl
┃  ┃     ┃  ┣ 📜 corner_pillar_3.stl
┃  ┃     ┃  ┣ 📜 corner_pillar_4.stl
┃  ┃     ┃  ┣ 📜 corner_pillar_connector_330mm.stl
┃  ┃     ┃  ┣ 📜 corner_pillar_connector_350mm.stl
┃  ┃     ┃  ┣ 📜 corner_pillar_support.stl
┃  ┃     ┃  ┣ 📜 heatsink_holder_female.stl
┃  ┃     ┃  ┣ 📜 heatsink_holder_male.stl
┃  ┃     ┃  ┣ 📜 holder_feet.stl
┃  ┃     ┃  ┣ 📜 holder_feet_assembly.stl
┃  ┃     ┃  ┣ 📜 holder_feet_support.stl
┃  ┃     ┃  ┣ 📜 reflector_fixed_height_assembly.stl
┃  ┃     ┃  ┗ 📜 reflector_holder.stl
┃  ┃     ┣ 📂 01_modular_reflector_adjustable_height
┃  ┃     ┃  ┣ 📜 corner_reflector_holder_1a.stl
┃  ┃     ┃  ┣ 📜 corner_reflector_holder_1b.stl
┃  ┃     ┃  ┣ 📜 modular_reflector_assembly.stl
┃  ┃     ┃  ┣ 📜 reflector_holder_330mm_1cm.stl
┃  ┃     ┃  ┣ 📜 reflector_holder_330mm_2cm.stl
┃  ┃     ┃  ┣ 📜 reflector_holder_330mm_6cm.stl
┃  ┃     ┃  ┣ 📜 reflector_holder_350mm_1cm.stl
┃  ┃     ┃  ┣ 📜 reflector_holder_350mm_2cm.stl
┃  ┃     ┃  ┗ 📜 reflector_holder_350mm_6cm.stl
┃  ┃     ┗ 📂 02_heatsink_and _LED_mounting_plate
┃  ┃        ┣ 📜 heatsink_200x200.stl
┃  ┃        ┗ 📜 LED_mount_400x400.stl
┃  ┗ 📜 readme.md
┣ 📂 02_MATERIALS
┃  ┣ 📂 00_electronics
┃  ┃  ┣ 📂 00_Tinkerforge
┃  ┃  ┃  ┗ 📜 Tinkerforge.txt
┃  ┃  ┣ 📂 01_LEDs
┃  ┃  ┃  ┣ 📂 blue
┃  ┃  ┃  ┃  ┣ 📂 453nm
┃  ┃  ┃  ┃  ┃  ┗ 📜 LZ4-00B208-0000.txt
┃  ┃  ┃  ┃  ┣ 📂 455nm
┃  ┃  ┃  ┃  ┃  ┗ 📜 LST1-01F06-RYL1-00.txt
┃  ┃  ┃  ┃  ┗ 📂 460nm
┃  ┃  ┃  ┃     ┣ 📜 5412869-LED_2520Engin_Datasheet_LuxiGen_LZ1-00DB00-1532005.pdf
┃  ┃  ┃  ┃     ┗ 📜 LZ1-00DB00.txt
┃  ┃  ┃  ┣ 📂 green
┃  ┃  ┃  ┃  ┗ 📂 530nm
┃  ┃  ┃  ┃     ┗ 📜 LST1-01F06-GRN1-00.txt
┃  ┃  ┃  ┣ 📂 RGBA
┃  ┃  ┃  ┃  ┗ 📜 LZ4-20MA00-0000.txt
┃  ┃  ┃  ┗ 📂 UV
┃  ┃  ┃     ┣ 📂 365nm
┃  ┃  ┃     ┃  ┗ 📜 LST1-01G01-UV01-00.txt
┃  ┃  ┃     ┣ 📂 385nm
┃  ┃  ┃     ┃  ┗ 📜 LZ1-10UB00-01U4.txt
┃  ┃  ┃     ┗ 📂 405nm
┃  ┃  ┃        ┣ 📂 onecore
┃  ┃  ┃        ┃  ┗ 📜 LZ1-10UB00-01U7.txt
┃  ┃  ┃        ┗ 📂 quadcore
┃  ┃  ┃           ┗ 📜 LZ4-V0UB0R-00U8.txt
┃  ┃  ┣ 📂 02_raspberry_pi
┃  ┃  ┃  ┗ 📜 raspberry_pi_4_8GB.txt
┃  ┃  ┣ 📂 03_sd_card
┃  ┃  ┃  ┗ 📜 SD_card.txt
┃  ┃  ┣ 📂 04_peltier_element
┃  ┃  ┃  ┗ 📜 peltier.txt
┃  ┃  ┣ 📂 05_power_supplies
┃  ┃  ┃  ┣ 📂 00_12V_5A
┃  ┃  ┃  ┃  ┗ 📜 12V_5A.txt
┃  ┃  ┃  ┗ 📂 00_24V_6A
┃  ┃  ┃     ┗ 📜 24V_6A.txt
┃  ┃  ┣ 📂 06_small_parts
┃  ┃  ┃  ┣ 📂 00_stripboard
┃  ┃  ┃  ┃  ┗ 📜 stripboard_WR_914-HP.txt
┃  ┃  ┃  ┣ 📂 01_connection_jacks
┃  ┃  ┃  ┃  ┣ 📜 2Pin_PCB_Mount_2.5mm_Pitch.txt
┃  ┃  ┃  ┃  ┣ 📜 2Pin_PCB_Mount_5mm_Pitch.txt
┃  ┃  ┃  ┃  ┣ 📜 banana_plug_female.txt
┃  ┃  ┃  ┃  ┣ 📜 banana_plug_male.txt
┃  ┃  ┃  ┃  ┣ 📜 Cable_extension_PWM_4-Pin_Moltex.txt
┃  ┃  ┃  ┃  ┣ 📜 DC_Jack.txt
┃  ┃  ┃  ┃  ┗ 📜 wago_2Conductur_clamp.txt
┃  ┃  ┃  ┣ 📂 02_Stacking_Header_Raspberry_Pi
┃  ┃  ┃  ┃  ┗ 📜 Stacking_Header_Raspberry_Pi.txt
┃  ┃  ┃  ┣ 📂 03_two_position_switch
┃  ┃  ┃  ┃  ┗ 📜 two_position_switch.txt
┃  ┃  ┃  ┗ 📂 04_silicone_wire
┃  ┃  ┃     ┗ 📜 silicone_wire.txt
┃  ┃  ┣ 📂 07_LED_drivers
┃  ┃  ┃  ┣ 📜 350mA_driver.txt
┃  ┃  ┃  ┣ 📜 500mA_driver.txt
┃  ┃  ┃  ┗ 📜 700mA_driver.txt
┃  ┃  ┣ 📂 08_membrane_pump
┃  ┃  ┃  ┣ 📜 accessories_membrane_pump.txt
┃  ┃  ┃  ┗ 📜 Membrane_Pump.txt
┃  ┃  ┗ 📂 09_fans
┃  ┃     ┣ 📂 00_fan_corpus_90x90mm
┃  ┃     ┃  ┗ 📜 fan.txt
┃  ┃     ┣ 📂 01_fan_corpus_130x130mm
┃  ┃     ┃  ┣ 📜 fan.txt
┃  ┃     ┃  ┗ 📜 fan_update.txt
┃  ┃     ┣ 📂 02_power_supply_fan_corpus_90x90mm
┃  ┃     ┃  ┗ 📜 power_supply.txt
┃  ┃     ┗ 📂 03_Pi_Fan
┃  ┃        ┗ 📜 Pi_Fan.txt
┃  ┣ 📂 01_accessories
┃  ┃  ┣ 📂 00_thermal_tube
┃  ┃  ┃  ┗ 📜 thermal_hose.txt
┃  ┃  ┣ 📂 01_hose_clamps
┃  ┃  ┃  ┗ 📜 hose_clamp.txt
┃  ┃  ┣ 📂 02_screws_nuts
┃  ┃  ┃  ┣ 📂 00_M3_Set
┃  ┃  ┃  ┃  ┗ 📜 M3_screw_set.txt
┃  ┃  ┃  ┣ 📂 01_Nylon_Spacer
┃  ┃  ┃  ┃  ┗ 📜 nylon_spacer.txt
┃  ┃  ┃  ┣ 📂 02_M3_60mm
┃  ┃  ┃  ┃  ┗ 📜 M3_60mm.txt
┃  ┃  ┃  ┗ 📂 02_M3_70mm
┃  ┃  ┃     ┗ 📜 M3_70mm.txt
┃  ┃  ┣ 📂 03_cooler
┃  ┃  ┃  ┣ 📂 00_tempering_module_cooler
┃  ┃  ┃  ┃  ┣ 📂 00_pelltier_cooler
┃  ┃  ┃  ┃  ┃  ┗ 📜 Alpine AM4 Passive.txt
┃  ┃  ┃  ┃  ┗ 📂 01_alu_water_cooler
┃  ┃  ┃  ┃     ┗ 📜 alu_water_cooler.txt
┃  ┃  ┃  ┗ 📂 01_LED_cooler
┃  ┃  ┃     ┣ 📂 00_25mm_cooler
┃  ┃  ┃     ┃  ┗ 📜 sink_s-1265491.txt
┃  ┃  ┃     ┣ 📂 01_50mm_cooler
┃  ┃  ┃     ┃  ┗ 📜 sink_s-1265491.txt
┃  ┃  ┃     ┗ 📂 02_300mm_cooler
┃  ┃  ┃        ┗ 📜 ATS-EXL75-300-R0.txt
┃  ┃  ┣ 📂 04_foam_rubber_seal
┃  ┃  ┃  ┗ 📜 foam_rubber_seal.txt
┃  ┃  ┗ 📂 05_PTFE
┃  ┃     ┣ 📂 00_technical_PTFE
┃  ┃     ┃  ┗ 📜 technical_PTFE.txt
┃  ┃     ┗ 📂 01_optical_PTFE
┃  ┃        ┗ 📜 optical_PTFE.txt
┃  ┗ 📜 readme.md
┣ 📂 03_ASSEMBLY_INSTRUCTIONS
┃  ┣ 📂 00_Corpus
┃  ┃  ┣ 📜 Assembly_Photoreactor_Corpus_130x130x130mm.pdf
┃  ┃  ┣ 📜 Assembly_Photoreactor_Corpus_90x90x140mm.pdf
┃  ┃  ┗ 📜 Assembly_Photoreactor_Corpus_90x90x90mm.pdf
┃  ┣ 📂 01_Controller
┃  ┃  ┣ 📜 20211029_Stripboard_drill_holes.pdf
┃  ┃  ┣ 📜 Controller_circuit_diagram.pdf
┃  ┃  ┣ 📜 Controller_Documentation.pdf
┃  ┃  ┗ 📜 Logic_Controller.pdf
┃  ┣ 📂 02_Peripheral_Modules
┃  ┃  ┣ 📂 00_Tempering_Module
┃  ┃  ┃  ┗ 📜 Peltier_Circuit_Diagram.pdf
┃  ┃  ┗ 📂 01_LED_Driver_Module
┃  ┃     ┗ 📜 LED Driver Module.pdf
┃  ┣ 📂 03_Irradiation_Module
┃  ┃  ┗ 📜 assembly_instruction_LED_cooler.pdf
┃  ┣ 📂 04_Multi_Batch_Screening_Phororeactor
┃  ┃  ┣ 📂 00_Photoreactor
┃  ┃  ┃  ┗ 📜 Multi_Batch_Screening_Photoreactor_assembly.pdf
┃  ┃  ┗ 📂 01_Mobile_Cover
┃  ┃     ┣ 📜 Mobile_Cover_assembly.pdf
┃  ┃     ┗ 📜 Mobile_Cover_assembly.stl
┃  ┗ 📜 readme.md
┣ 📂 04_IMAGES
┃  ┣ 📜 Licenses.png
┃  ┗ 📜 Licenses.svg
┣ 📜 License.md
┗ 📜 Readme.md
```

## More Information

<!--- Cite this repository: [![DOI](https://zenodo.org/badge/368164449.svg)](https://zenodo.org/badge/latestdoi/368164449) --->



## Publications

### Core Modular Photoreactor Platform

* **2022**  
  Kowalczyk et al.  
  *Making Photocatalysis Comparable Using a Modular and Characterized Open-Source Photoreactor*  
  ChemPhotoChem, 6 (2022).  
  https://doi.org/10.1002/cptc.202200044

* **2023**  
  Kowalczyk et al.  
  *Making Photocatalysts Screenable – A Milli-Scale Multi-Batch Screening Photoreactor as Extension for the Modular Photoreactor*  
  Reaction Chemistry & Engineering (2023).  
  https://doi.org/10.1039/D3RE00398A

### Related Preprints

* **2025**  
  Koba et al.  
  *Improving Efficiency of Light-Driven Water Oxidation Catalysis through Dynamic Irradiation*  
  To be submitted (2025).  
  https://doi.org/10.5281/zenodo.17867915

* **2025**  
  Wiedemann et al.  
  *Making Photocatalyst Screening Photoefficient – Combining Radiation Field Models to Design a Direct Irradiation Module for the Multi-Batch Screening Reactor*  
  To be submitted (2025).  
  https://doi.org/10.5281/zenodo.17867874
  
### Related Journal Articles

* **2022**  
  Buday et al.  
  *Activating a [FeFe] Hydrogenase Mimic for Hydrogen Evolution under Visible Light*  
  Angewandte Chemie International Edition (2022).  
  https://doi.org/10.1002/anie.202202079

* **2023**  
  Knorr et al.  
  *Unlocking the potential of ketocoumarins: efficient photosensitizers for sustainable light-driven hydrogen evolution*  
  Journal of Materials Chemistry A (2023).  
  https://doi.org/10.1039/D3TA04450E

* **2023**  
  Çeper et al.  
  *Visible-Light-Driven Hydrogen Evolution of PtNP/[Ru(bpy)3]2+/Polyampholyte Hybrid Hydrogels*  
  ACS Applied Polymer Materials (2023).  
  https://doi.org/10.1021/acsapm.3c01051

* **2023**  
  Abbas et al.  
  *Initial Quenching Efficiency Determines Light-Driven H2 Evolution of [Mo3S13]2− in Lipid Bilayers*  
  Chemistry – A European Journal (2023).  
  https://doi.org/10.1002/chem.202302284

* **2024**  
  Çeper et al.  
  *Noble Metal-Free Light-Driven Hydrogen Evolution Catalysis in Polyampholytic Hydrogel Networks*  
  ACS Applied Materials & Interfaces (2024).  
  https://doi.org/10.1021/acsami.4c04045

* **2024**  
  Kasahara et al.  
  *Molecular Dyad vs Multi-Component Approach – Photocatalytic Hydrogen Evolution by Combining Oligothiophene Photosensitizers with [FeFe]-Hydrogenase Mimics*  
  ChemCatChem (2024).  
  https://doi.org/10.1002/cctc.202400247

* **2025**  
  Kasahara et al.  
  *[FeFe]-Hydrogenase Mimic with Organic Photosensitizers for Long-Lived Excited States and Efficient Photocatalytic H2 Production*  
  Cell Reports Physical Science (2025).  
  https://doi.org/10.1016/j.xcrp.2025.102975

* **2025**  
  Basma et al.  
  *Engineered [FeFe]-Hydrogenase Mimics Featuring Heteroaryl Linkers: Molecular Design and Photocatalytic Hydrogen Evolution under Visible Light*  
  Inorganic Chemistry Frontiers (2025).  
  https://doi.org/10.1039/D5QI01191D

* **2025**  
  Abbas et al.  
  *Selective Light-Driven CO2 to CO Reduction by a [FeFe]-Hydrogenase Mimic in Water*  
  ChemCatChem (2025).  
  https://doi.org/10.1002/cctc.202401947

* **2025**  
  Mandal et al.  
  *Mn2+ and [Ru(bpy)3]2+ in UiO-67 Metal-Organic Frameworks Enhance Photocatalytic Oxidation of Benzylamine via an Electron Transfer Pathway*  
  RSC Advances (2025).  
  https://doi.org/10.1039/D5RA04503G

* **2025**  
  Mandal et al.  
  *Enhanced and Durable Light-Driven Hydrogen Evolution by Cobalt-Based Prussian Blue Analogs in Phospholipid Bilayers*  
  Advanced Energy and Sustainability Research (2025).  
  https://doi.org/10.1002/aesr.202400372

* **2025**  
  Mandal et al.  
  *The Zr8O6 Secondary Building Unit and Porphyrin Linker Catalyze Light-Driven H2 Evolution in Porphyrin-Based Metal-Organic Frameworks*  
  ChemSusChem (2025).  
  https://doi.org/10.1002/cssc.202500372

* **2026**  
  Kolbinger et al.  
  *{Mo2} can do it too: dynamic irradiation increases photonic efficiency of light-driven hydrogen evolution by [Mo2S12]2−*  
  Sustainable Energy & Fuels (2026).  
  https://doi.org/10.1039/D6SE00078A

* **2026**  
  Kolbinger et al.  
  *Fewer photons, more hydrogen: effects of dynamic irradiation on light-driven hydrogen evolution by thiomolybdate catalysts*  
  Sustainable Energy & Fuels (2026).  
  https://doi.org/10.1039/D5SE01490E

* **2026**  
  Brezhneva et al.  
  *Insights Into Overall Photocatalytic Water Splitting Through Simultaneous In Situ H2 and O2 Measurements*  
  ChemSusChem (2026).  
  https://doi.org/10.1002/cssc.202502721

* **2026**  
  Tombrink et al.  
  *4CzIPN Photosensitizes the Cobaloxime-Catalyzed Light-Driven Hydrogen Evolution Reaction*  
  ChemSusChem (2026).  
  https://doi.org/10.1002/cssc.70942

* **2026**  
  Baumgarten et al.  
  *Phenothiazine redox mediators boost photocatalytic hydrogen evolution*  
  EES Catalysis (2026).  
  https://doi.org/10.1039/D6EY00029K

* **2026**  
  Utievskyi et al.  
  *Embedding a Dinuclear Ru–Pt Photocatalyst Into Polyampholytic Graft Copolymer Matrix Enables Prolonged Hydrogen Evolution While Allowing Catalyst Repair*  
  Chemistry – A European Journal (2026).  
  https://doi.org/10.1002/chem.71568

* **2026**  
  Schleicher et al.  
  *Light-driven hydrogen evolution reactivity of molecular thio-oxomolybdate catalysts*  
  Sustainable Energy & Fuels (2026).  
  https://doi.org/10.1039/D6SE00061D

* **2026**  
  Tran et al.  
  *Soft-Matter Confinement Modulates Excited-State Dynamics of Ru Photocatalysts for Hydrogen Evolution in Aqueous Media*  
  ACS Materials Au (2026).  
  https://doi.org/10.1021/acsmaterialsau.5c00212
