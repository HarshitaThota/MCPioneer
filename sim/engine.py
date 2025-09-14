from sim.events import EventDeck
from sim.metrics import Metrics

class Simulator:
    def __init__(self, world, roster):
        self.world = world
        self.roster = roster
        self.events = EventDeck()
        self.metrics = Metrics(self.world)

    def tick(self):
        self.world.decay()                       # oxygen/food/morale drift
        event = self.events.draw()
        proposals = self.roster.propose(event)   # agents propose actions
        chosen = self.roster.deliberate(proposals, event)  # politician bias etc.
        outcome = chosen.execute(self.world)     # may call MCP servers
        self.world.apply(outcome)
        self.metrics.update(outcome)

    def snapshot(self):
        return {
            "tick": self.world.tick,
            "resources": self.world.resources.dict(),
            "population": self.world.population.dict(),
            "morale": self.world.morale,
            "governance": self.world.gov_state,
            "last_event": self.events.last_repr(),
        }
