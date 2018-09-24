# Main Binds For Other .py's
file = open("C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/cfg/aMain.cfg", "w")
file.write('''
bind "j" "net_channels 1"
bind "k" "exec aConfig"
bind "l" "exec a1v1"
bind "h" "exec aMain"
say Config 2.0 Loaded
''')
file.close()

# Main Config Files
file = open("C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/cfg/aConfig.cfg", "w")
file.write('''
cl_viewmodel_shift_left_amt "0.500000"
cl_viewmodel_shift_right_amt "0.250000"
viewmodel_fov "68"
viewmodel_offset_x "1.25"
viewmodel_offset_y "0.75"
viewmodel_offset_z "-1.600000"
viewmodel_presetpos "0"
viewmodel_recoil "1.0"
cl_bob_lower_amt "5.000000"
cl_bobamt_lat "0.100000"
cl_bobamt_vert "0.100000"
cl_bobcycle "0.98"
cl_crosshairstyle 4;
cl_crosshairsize 1.6;
cl_crosshairthickness 1;
cl_crosshairgap -0.6;
cl_crosshair_drawoutline 1;
cl_crosshair_outlinethickness 1;
cl_crosshairdot 0;
cl_crosshair_t 0;
cl_crosshaircolor 5;
cl_crosshaircolor_r 255;
cl_crosshaircolor_g 255;
cl_crosshaircolor_b 255;
hud_scaling 0.65
cl_allowdownload 1
cl_autohelp 0
cl_crosshairgap_useweaponvalue 0

bind "ESCAPE" "cancelselect"
bind "`" "toggleconsole"

bind "TAB" "+showscores"
bind "SPACE" "+jump"
bind "," "buyammo1"
bind "." "buyammo2"
bind "0" "slot10"
bind "1" "slot1"
bind "2" "slot2"
bind "3" "slot3"
bind "4" "slot4"
bind "5" "slot5"
bind "6" "slot6"
bind "7" "slot7"
bind "8" "slot8"
bind "9" "slot9"
bind "a" "+moveleft"
bind "b" "buymenu"
bind "c" "radio3"
bind "d" "+moveright"
bind "e" "+use"
bind "f" "+lookatweapon"
bind "g" "drop"
bind "i" "show_loadout_toggle"
bind "MOUSE5" "+voicerecord"
bind "m" "teammenu"
bind "q" "lastinv"
bind "r" "+reload"
bind "s" "+back"
bind "u" "messagemode2"
bind "w" "+forward"
bind "x" "radio2"
bind "y" "messagemode"
bind "z" "radio1"
bind "CTRL" "+duck"
bind "SHIFT" "+speed"
bind "F3" "autobuy"
bind "F4" "rebuy"
bind "F5" "jpeg"
bind "F6" "save quick"
bind "F7" "load quick"
bind "F10" "quit prompt"
bind "MWHEELDOWN" "invnext"
bind "MWHEELUP" "invprev"
bind "MOUSE1" "+attack"
bind "MOUSE2" "+attack2"
bind "PAUSE" "pause"
bind "DEL" "mute"
bind "t" "+spray_menu"
say Config Loaded''')
file.close()

# 1v1 Config
file = open("C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/cfg/a1v1.cfg", "w")
file.write('''
bot_kick;
mp_freezetime 1;
mp_buy_anywhere 1;
mp_roundtime 80250;
mp_maxrounds 60;
sv_cheats 1;
mp_maxmoney 65535;
mp_startmoney 65535;
mp_afterroundmoney 65535;
mp_match_can_clinch 1;
mp_limitteams 1;
sv_allow_votes 0;
mp_free_armor 1;
mp_ct_default_primary weapon_ak47;
mp_t_default_primary weapon_m4a1;
mp_ct_default_secondary weapon_deagle;
mp_t_default_secondary weapon_deagle;
mp_weapons_allow_map_placed 0;
mp_death_drop_gun 0;
mp_ignore_round_win_conditions 0;
bot_quota 0;
mp_halftime 1;
sv_infinite_ammo 2;
mp_halftime_duration 8;
mp_warmup_end;
mp_restartgame 3;
say 1v1 Config Loaded
''')
file.close()
