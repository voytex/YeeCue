# YeeCue
<i>Python script adapting Yeelight bulbs as cue lights for Blackmagic ATEM switchers</i>

## About
Enterprise <b>cue lights</b> used by streaming companies or TV studios are way out of any amateur's budget. But the functionality is not <b>that</b> complicated after all. 
Since me and my friends provide streaming services, I began to think about a budget solution. First I thought about using some Arduino or ESP32 with red 
and green LEDs. It would however require a lot of other components as 5V LEDs would not be sufficient (not mentioning a 3D-printed enclosure with some sort of coldshoe adapter). I wanted more effortless solution – and then I came accross smartbulbs by <b>Yeelight</b>!

These smartbulbs are way cheaper than other brands (e.g. Phillips Hue or IKEA) and communicate over Wi-Fi, which is also handy because you don't need any ZigBee gateway. They also have a lot of trade-offs (tedious initial setup, not so strong light output...) but overall are absolutely awesome for this kind of project!


