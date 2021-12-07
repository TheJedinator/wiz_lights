from pywizlight.bulb import wizlight, PilotBuilder, discovery
# create/get the current thread's asyncio loop
loop = asyncio.get_event_loop()
# setup a standard light
light = wizlight("192.168.2.13")
# setup the light with a custom port
light = wizlight("<your bulb ip",12345)

#the following calls need to be done inside an asyncio coroutine
#to run them fron normal synchronous code, you can wrap them with asyncio.run(..)
#see test.py for examples

    # turn on the light into "rhythm mode"
await light.turn_on(PilotBuilder())
# set bulb brightness
await light.turn_on(PilotBuilder(brightness = 255)

# set bulb brightness (with async timeout)
# timeout_secs = 10
await asyncio.wait_for(light.turn_on(PilotBuilder(brightness = 255)), wait_secs)

# set bulb to warm white
await light.turn_on(PilotBuilder(warm_white = 255)

# set rbb values
# red to 0 = 0%, green to 128 = 50%, blue to 255 = 100%
await light.turn_on(PilotBuilder(rgb = (0, 128, 255))

# get the current color temperature, rgb values
state = await light.updateState()
print(state.get_colortemp())
r, g, b = state.get_rgb()
print("red %i green %i blue %i" % (r, g, b))

# start a scene 
await light.turn_on(PilotBuilder(scene = 14)) # party

# get the name of the current scene
state = await light.updateState()
print(state.get_scene())

# turns the light off
await light.turn_off()

# do operations on multiple lights parallely
bulb1 = wizlight("192.168.2.13")
bulb2 = wizlight("192.168.2.23")
await asyncio.gather(bulb1.turn_on(PilotBuilder(brightness = 255),
    bulb2.turn_on(PilotBuilder(warm_white = 255), loop = loop)

# Discover all bulbs in the network via broadcast datagram (UDP)
# function takes the discovery object and returns a list with wizlight objects.
bulbs = await discovery.find_wizlights(discovery)
# print the ip of the bulb on index 0
print(bulbretrun[0].ip)
# iterate over all returned bulbs
for bulb in bulbs:
    await bulb.turn_off()