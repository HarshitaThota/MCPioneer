.PHONY: up down logs test fmt smoke
up:      ; docker compose -f infra/docker-compose.yml up --build -d
down:    ; docker compose -f infra/docker-compose.yml down -v
logs:    ; docker compose -f infra/docker-compose.yml logs -f --tail=200
smoke:   ; RUN_ONCE=1 docker compose -f infra/docker-compose.yml up --build orchestrator
test:    ; pytest -q
fmt:     ; ruff check . --fix || true
