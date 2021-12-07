import time

from pywizlight.bulb import wizlight, PilotBuilder, discovery
import asyncio

loop = asyncio.get_event_loop()


async def turn_off_bulb(ip):
    bulb = wizlight(ip)
    await bulb.turn_off()


async def turn_on_bulb(ip):
    bulb = wizlight(ip)
    await bulb.turn_on()


async def find_bulbs():
    return await discovery.find_wizlights(discovery)


async def get_bulb_states(bulb):
    await bulb.updateState()
    return bulb.state

async def main():
    # light = wizlight("192.168.2.23")
    # await light.turn_on()
    # await light.updateState()
    # state = light.state
    # is_on = state.get_state()
    # print(is_on)
    # await turn_on_bulb("192.168.2.23")
    # await turn_off_bulb("192.168.2.23")
    # while True:
    #     await turn_on_bulb("192.168.2.23")
    #     time.sleep(.2)
    #     await turn_off_bulb("192.168.2.23")
    #     time.sleep(.2)
    bulbs = await find_bulbs()
    for bulb in bulbs:
        await turn_on_bulb(bulb.ip)
        print(bulb.ip)
        time.sleep(5)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


