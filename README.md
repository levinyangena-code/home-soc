# Home SOC in a Box

A self-hosted mini-SOC lab for **synthetic log ingestion, detections, and dashboarding**. This repository is being built phase by phase; Phase 1 provides the container, ingestion, storage, and event-schema foundation.

> **Lab use only.** Use synthetic events and documentation-range addresses. Before any wider exposure, put the UI behind a VPN or reverse proxy with TLS and review the deployment security settings. Do not send real or sensitive logs to a public demo.

## Phase 1 quick start

```sh
cp .env.example .env
# Replace the example database and OpenSearch passwords in .env with unique local secrets.
docker compose config
docker compose up -d
```

The UI port is bound to `127.0.0.1:8000` by default. During Phase 1 it serves only a temporary health endpoint at <http://127.0.0.1:8000/health>; the dashboard is planned for Phase 4. Check service status with `docker compose ps` and logs with `docker compose logs -f`.

Ingestion is exposed on host TCP/UDP 514 for syslog and TCP 8080 for Vector's JSON HTTP input (`POST /ingest`). OpenSearch and Postgres are not published to the host. Persistent data is held in named Docker volumes. Remove the volumes only when you intend to delete stored state: `docker compose down -v`.

## Synthetic data policy

Use fake hostnames and MAC addresses, and only the documentation IPv4 ranges `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`. Never commit locally collected logs or secrets. The `.gitignore` excludes environment files, runtime data, and directories/files marked as real or live logs.

## Planned improvements

Outbound traffic rules will use destination-port, byte-volume, and beaconing heuristics. Country/GeoIP enrichment is intentionally out of scope for the initial implementation and may be considered later using a local dataset.
