# YeeCue | Budget Cue Lights for Blackmagic ATEM Switchers
<i>Python script adapting Yeelight bulbs as cue lights for Blackmagic ATEM switchers</i>

## About
Enterprise <b>cue lights</b> used by streaming companies or TV studios are way out of any amateur's budget. But the functionality is not <b>that</b> complicated after all. 
Since me and my friends provide streaming services, I began to think about a budget solution. First I thought about using some Arduino or ESP32 with red 
and green LEDs. It would however require a lot of other components as 5V LEDs would not be sufficient (not mentioning a 3D-printed enclosure with some sort of coldshoe adapter). I wanted more effortless solution – and then I came accross smartbulbs by <b>Yeelight</b>!

These smartbulbs are way cheaper than other brands (e.g. Phillips Hue or IKEA) and communicate over Wi-Fi, which is also handy because you don't need any ZigBee gateway. They also have a lot of trade-offs (tedious initial setup, not so strong light output...) but overall are absolutely awesome for this kind of project!

The whole system is being used and tested with our stream setup

<img src="https://user-images.githubusercontent.com/63453314/209685236-5d55c558-8f29-4c99-a1a0-12867db283f4.jpg"  width="500">

## Requirements
### Bulbs
Firstly, we need <b>the bulbs</b>. Here in CZE, they are a bit harder to find, still possible tho. See the following table of tested compatible bulbs:

| Bulb type | Tested and working |
| --------- | :---: |
| Yeelight 1SE (color) | ✅ |
| Yeelight W3 (color) | ✅ |
| Yeelight M2 | ❌ not working ❌ |

There might be other types which I haven't been able to test, still W3 and 1SE are safe bets. Feel free to report other types.
### Blackmagic ATEM
As far as I know all Blackmagic ATEM switchers <b>should</b> be able to be compatible. Everything depends on Python library <a href="https://clvlabs.github.io/PyATEMMax/">PyATEMMax</a> which is derived from SKAARHOJ Arduino library (huge thanks to all contributors). However, as stated in the docs:
```markdown
August 2018: The free open source SKAARHOJ provided Arduino Libraries will only work with 
ATEM Software Control firmware versions up to 7.5.0.

(SKAARHOJs commercial products will work with ATEM Software Control firmwares beyond 7.5.0)
```
It <b>might cease working</b> with Blackmagic ATEM firmware update and nobody might be able to patch it. But for now, it works.

| ATEM type | Firmware Version | Tested and working |
| --------- | :--------------: | :----------------: | 
| Blackmagic ATEM Mini Pro | TBD | ✅ |
| other ATEMs | ❓ | ❓ |

### Software
As mentioned, YeeCue is depended on <a href="https://clvlabs.github.io/PyATEMMax/">PyATEMMax</a>. In addition, it also uses <a href="https://yeelight.readthedocs.io/en/latest/"> Python YeeLight Library</a> (again, huge thanks to contributors). Both libraries could be installed using ``pip``.
```shell
$ pip install yeelight
$ pip install PyATEMMax
```

## Usage
The script has to be running on a PC/Mac within the same network all the bulbs and the ATEM are connected into. 
### 1. Bulb initialization
The first task is to <i>activate</i> the bulbs and connect them to a single network. As far as I know, it <b>has to be done</b> via official Yeelight app. During the activation, the bulb has to send <i>some</i> data to the internet, therefore the LAN you are adding the bulb into, has to be connected to the internet. 
1. On your smartphone, download official Yeelight App (not the Mi Home)
2. Connect your smartphone to the same network you wish to connect the bulb into
3. In Yeelight App, add a new bulb following the instructions
4. Once the procedure is done, <b>be sure to turn on LAN control</b> (it should be on by default). This is absolutely crucial, it allows you to control the bulb locally, even without the LAN connected to the internet
5. Now it is very handy for the bulb to have a static IP. In your AP settings (probably somewhere in DHCP tab) assign this bulb a static IP.

Repeat for all the bulbs you wish to use. Regarding the IPs, assign them <b>sequentially</b>, the script won't work otherwise. 

### 2. Run the script
After you connect bulbs, ATEM and the PC/Mac into a single network, you can proceed and run the script. In Terminal or Command Line , ``cd`` into the folder you downloaded the script. You can either run
```shell
$ python3 main.py
```
and go through the <i>wizard</i> filling the number of bulbs being used and all the IPs, or run
```shell
$ python3 main.py [n_bulbs] [ip_start] [ip_atem] (-v)
```
where ``n_bulbs`` sets the number of bulbs being used, ``ip_start`` is the last of nibble of first bulb's IP, ``ip_atem`` is the last nibble of the ATEM's IP address. Optional ``-v`` turns on verbose mode. 
#### Example
Let's say, I have three bulbs, the first one's IP address is ``192.168.1.100``, the second has ``.101``, the third ``.102``. ATEM's IP address is ``192.168.1.50``. My computer has IP within the same subnet, for example ``192.168.1.7``. I can now run the script as 
```shell
$ main.py 3 100 50 -v
```
Input 1 of the ATEM switcher will be then assigned to the first bulb ``192.168.1.100``, input 2 to the bulb ``.101`` and input 3 to the bulb ``.102``. If the video input is set to <b>Preview</b>, the corresponding bulb turns green. If the input is set to <b>Program</b>, corresponding bulbs turns red. Otherwise the bulb is turned off. 

## Plans for the future
This project is very very much <b>work in progress</b>, I would like to develop a simple GUI for everyone to use. Of course feel free to fix my bugs or improve anything. This project is now <b>on hold</b>, since I have to finish my Master's project. 

