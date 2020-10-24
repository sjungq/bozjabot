i have no idea what im doing btw

This script was written to ping myself or other users on Discord for specific Bozja skirmishes as they spawn. It periodically takes a screenshot of a region of my screen (currently, starting from 0,0 to 500, 400) where my map is placed, and then loops through all images in the "needles" folder to try to locate them on the map.

**REQUIRES Python 3.6 <= x <= 3.8. One of the libraries (pyautogui I think?) does not like the latest Python 3.9**

### Requirements for proper image matching:

1. A consistent AFK spot where you can use /hudlayout to bypass the AFK timer. I sit on a specific chair in one of the tents at the base to keep this position consistent, and angle my camera in a way where my FOV cone on the map won't interfere with the skirmishes that spawn right outside of base (if you care about those). Reset the map and make sure to toggle on "Center map on player location" so that the map itself opens in a consistent position.

2. Set map transparency to 0 (Character Configuration, Map Settings)

3. Grab "needle" (ie. needle in the haystack) screenshots of the Bozja skirmishes you want to be notified for. This MUST be done while the map is still in the same "position" that it would be while you're AFKing in base with /hudlayout on, because variations in the /hudlayout gridlines depending on map position will interfere with the image matching process.

4. make sure no pesky party members are running around the area where the fate will pop because the blue party member dot will interfere with image match

Note that you can't do this for fates that are out of bounds of the map while you're AFKing in base - specifically, The Shadow of Death's Hand (big birb). But like, no one cares about the non 1v1 fates right?????

### more notes about the 'needle' images

you can use smaller slices (see examples in needle folder) as long as you include enough distinguishing detail from the surrounding area on the map, which would also make for faster image matching. Note that large needle images isn't necessarily good either; for example the Red Chocobo skirmish can spawn alongside another skirmish in the Zone 3 ("Desperately Seeking Something" / "Waste the Rainbow"). If your image for Red Chocobo includes the portion of Zone 3 where those skirmishes can spawn, the image match will fail if Red Chocobo AND the Zone 3 skirmish are up at the same time.
