import time, json, os
from sim.engine import Simulator
from sim.world import World
from agents.base import Roster
from configs import loader as cfg

TICK_SECS = float(os.getenv("TICK_SECS", "1.0"))

def main():
    world_cfg = cfg.load_world("configs/scenario_space_colony.yml")
    agents_cfg = cfg.load_agents("configs/agents.default.yml")

    world = World(world_cfg)
    roster = Roster.from_config(agents_cfg, world=world)
    sim = Simulator(world, roster)

    os.makedirs("/artifacts/runs", exist_ok=True)
    path = "/artifacts/runs/latest.json"

    while True:
        if os.getenv("RUN_ONCE") == "1":  # smoke test
            for _ in range(3): sim.tick()
            break
        sim.tick()
        with open(path, "w") as f: json.dump(sim.snapshot(), f)
        time.sleep(TICK_SECS)

if __name__ == "__main__":
    main()
