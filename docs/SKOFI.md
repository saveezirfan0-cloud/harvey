# Harvey for Skofi

Harvey is trained for Skofi (skofi.tech) and split across two places.

| Where | What it does | Runs on |
|---|---|---|
| **Skofi portal** (`skofi` repo, `portal/`) | Harvey's writer and reply handler: opening lines for verified prospects, intent + drafted answers for every reply. Everything waits for approval on `/harvey`. The portal's existing engine discovers, enriches, verifies and sends. | Vercel cron (every 15 min) + the Anthropic API key on the `skofi-portal` project |
| **This repo** | Deep research and list-building: web prospecting, tech-stack and hiring signals, email pattern + verification. Email sending is **off** (`channels.email.enabled: false`) so nobody is emailed by both systems. | Your machine or any Docker host |

## The trained files

- `harvey.yaml`: Skofi persona (Saveez, Founder), offer (15-minute call at
  cal.com/skofi/15min), ICP (ops leaders at 10-200 person firms in the UK, US
  and Australia), hiring signals, quiet hours in Europe/London.
- `skills/product_knowledge.md`: services, case studies (by sector only),
  buying signals, UK PECR note.
- `skills/competitive_intel.md`: the honest trade-off against DIY Zapier,
  big agencies, freelancers, more SaaS and "let AI build it".
- The portal's copy of the same playbook: `skofi/portal/lib/harvey/knowledge.ts`.
  Change both together.

## Running this side with an API key (no Max login)

The Claude CLI uses `ANTHROPIC_API_KEY` when it is set, so a key works instead
of `claude login`:

```bash
echo "ANTHROPIC_API_KEY=sk-ant-..." >> .env     # plus REOON_API_KEY / SERPER_API_KEY
docker compose up -d --build                     # or: source .venv/bin/activate && harvey run
harvey signals --confirm free
harvey export                                    # -> prospects.csv
```

Import `prospects.csv` into the portal (Lead lists), where enrichment,
verification and sequencing take over.

Vercel cannot host this loop (no long-lived process, no persistent disk, no
browser), which is why the portal half was ported to TypeScript instead.
