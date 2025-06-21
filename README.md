# anki-jkscroll
Scroll in reviewer with vi/vim keys j and k

### Rational
If you type in your cards and the backside of cards in the deck is huge then you often find yourself reaching for page up/page down/arrow keys to scroll down.
Since I am a vim user it was really frustrating not having jk to scroll considering they are not even mapped to anything by default.
This usecase might be rare, but it was so refreshing finally not having to move hands to just scroll for every card.


### Configuration
You can configure the amount of scroll in a config.
Also notice that there are additional mappings for J and K (shift+j, shift+k), so that you can use them as page up/page down, though there was no way to do an actual page-vise scrolling, because qtwebengine does not support that javascript function, but within a few minutes of tweaking you should be able to find the right value.

### Supported Anki versions
I have not tested this on earlier versions, but I think this should work just fine even before 2.1.35. Tell me if it is broken on earlier versions and I will look into it
