# Copyright 2021 LeMaRiva|tech lemariva.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# RASPBERRY PI Pico 
device_config = {
    'spi_unit': 0,
    'miso':4,
    'mosi':3,
    'ss':5,
    'sck':2,
    'dio_0':6,
    'reset':7,
    'led':25, 
}

app_config = {
    'loop': 200,
    'sleep': 100,
}

#SF7BW125
lora_parameters = {
    'tx_power_level': 2, 
    'signal_bandwidth': 'SF7BW125',
    'spreading_factor': 7,    
    'coding_rate': 5, 
    'sync_word': 0x34, 
    'implicit_header': False,
    'preamble_length': 8,
    'enable_CRC': True,
    'invert_IQ': False,
}


wifi_config = {
    'ssid':'',
    'password':''
}

#configuration for V2 TTN
ttn_config = {
    'devaddr': bytearray([0x26, 0x01, 0x1A, 0x2A]),
    'nwkey': bytearray([0x81, 0x7E, 0x57, 0x71, 0x33, 0xD6, 0x62, 0x38,
                   0x96, 0x6F, 0x20, 0x50, 0x81, 0x2B, 0x63, 0xB1]),
    'app': bytearray([0xFC, 0xA9, 0x01, 0xA8, 0xCF, 0xFD, 0xE4, 0x03,
                 0xA9, 0x43, 0x4E, 0x03, 0x57, 0x9D, 0x96, 0x8A]),
    'country': 'EU',
}

#configuration for V3 TTN
#ttn_config = {
#    'devaddr': bytearray([0x26, 0x0B, 0x8F, 0xDB]),
#    'nwkey': bytearray([0xA8, 0x85, 0xA8, 0xDA, 0x2B, 0x1A, 0xD8, 0xEF,
#                   0xE5, 0x54, 0x8A, 0xD4, 0xA7, 0x55, 0x48, 0x6F]),
#    'app': bytearray([0x07, 0x32, 0x19, 0x15, 0xAE, 0x4B, 0x9C, 0x5F,
#                 0x15, 0xAA, 0xF3, 0x99, 0xA7, 0x4D, 0x7E, 0xFC]),
#    'country': 'EU',
#}