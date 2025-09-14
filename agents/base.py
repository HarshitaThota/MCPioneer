from dataclasses import dataclass
from typing import List

@dataclass
class Personality:
    risk_aversion: float
    altruism: float
    curiosity: float

class Agent:
    def __init__(self, name, role, personality, world):
        self.name, self.role, self.personality, self.world = name, role, personality, world

    def propose(self, event):
        return self.role.propose(self, event)

class Roster:
    def __init__(self, agents: List[Agent], world): self.agents, self.world = agents, world

    @classmethod
    def from_config(cls, cfg, world):
        agents=[]
        for a in cfg["agents"]:
            # import role class by name (Engineer/Scientist/Politician)
            role_cls = __import__(f"agents.roles.{a['role']}", fromlist=["Role"]).Role
            p = Personality(**a["personality"])
            agents.append(Agent(a["name"], role_cls(world), p, world))
        return cls(agents, world)

    def propose(self, event): return [a.propose(event) for a in self.agents]
    def deliberate(self, proposals, event):
        # placeholder: pick proposal with highest expected survival
        return max(proposals, key=lambda p: p.expected_value())
