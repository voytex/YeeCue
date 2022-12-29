# YeeCue
<i>Python script adapting Yeelight bulbs as cue lights for Blackmagic ATEM switchers</i>

## About
Enterprise <b>cue lights</b> used by streaming companies or TV studios are way out of any amateur's budget. But the functionality is not <b>that</b> complicated after all. 
Since me and my friends provide streaming services, I began to think about a budget solution. First I thought about using some Arduino or ESP32 with red 
and green LEDs. It would however require a lot of other components as 5V LEDs would not be sufficient (not mentioning a 3D-printed enclosure with some sort of coldshoe adapter). I wanted more effortless solution – and then I came accross smartbulbs by <b>Yeelight</b>!

These smartbulbs are way cheaper than other brands (e.g. Phillips Hue or IKEA) and communicate over Wi-Fi, which is also handy because you don't need any ZigBee gateway. They also have a lot of trade-offs (tedious initial setup, not so strong light output...) but overall are absolutely awesome for this kind of project!

The whole sstem is being used and tested with our stream setup

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
As far as I know all Blackmagic ATEM switchers <b>should</b> be able to be compatible. Everything depends on Python library <a href="https://clvlabs.github.io/PyATEMMax/">PyATEMMax</a> (huge thanks to the authors, mainly SKAARHOJ). However, as stated in the docs:
```markdown
August 2018: The free open source SKAARHOJ provided Arduino Libraries will only work with 
ATEM Software Control firmware versions up to 7.5.0.

(SKAARHOJs commercial products will work with ATEM Software Control firmwares beyond 7.5.0)
```
It <b>might cease working</b> with Blackmagic ATEM firmware update and nobody might be able to patch it. But for now, it works.

| ATEM type | Firmware Version | Tested and working |
| --------- | ---------------- | ------------------ | 
| Blackmagic ATEM Mini Pro | TBD | ✅ |
| other ATEMs | ❓ | ❓ |


### Software


## Installation

## Usage
