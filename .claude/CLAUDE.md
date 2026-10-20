# B2B Export Independent Site - Skill Orchestration Protocol (`.claude/CLAUDE.md` · V4.0)

This project runs the **`b2b-seo-geo-site-master` V4.0** unified workflow, deeply fusing all 12 engineering subsystems of `cnproduct/b2b-global-brand-site-master` with 13 open-source SEO, GEO, CRO, and UI/UX skills.
All SEO, GEO, and CRO planning context MUST read and write through **`docs/seo/`**, while all company claims and assets are strictly governed by **`private/knowledge-cards.json` -> `content/public-facts.json`** and **`private/asset-register.json`**.

## 1. Strict 4-Phase Skill Routing Rules

1. **Phase 1: Fact Ingestion (`M0/M1/M2`), Keyword Matrix & SERP Teardown (`orchestrator.py` + `sitekit.py` + `seo_geo_matrix.py`)**
   - **Single Source of Truth**: `private/knowledge-cards.json` (RenWork V4 7 states, 00-20 modules), `private/gaps.md`, `docs/seo/keyword-matrix.json`, `docs/seo/topic-cluster.json`, and `docs/seo/site-brief.md`.
   - **Mandatory Rule**: Assess data maturity (`M0` / `M1` / `M2`), obey industry `red_lines`, verify SERP B2B supplier intent (>= 60%), and ensure the primary keyword appears in the Clean URL slug, `<title>`, `<h1>`, and first 100 words.

2. **Phase 2: First-Viewport B2B Workbench, 10 Page Blueprints & Dual-Mode RFQ (`marketingskills` + `liquid-skills` + `rfq_daemon.py`)**
   - **Single Source of Truth**: `docs/seo/cro-copy-deck.md`, `content/site.json`, and `content/public-facts.json`.
   - **Mandatory Rule**: Follow the industry's `decision_path` (`使用者场景→结构材料→安全→包装→定制`). Place a **Zero-Signup Friction Interactive Workbench** in the first viewport, pass product context to `/contact/?product=<Model>#inquiry`, and use **3-Tier Commercial RFQ Cards** with B2B Risk Reversal (default `email_draft` mode, or approved `http` mode backed by `scripts/rfq_daemon.py`).

3. **Phase 3: Zero AI-Slop UI, Multi-Script Typography & `data-layout` (`extract_brand_dna.py` + `design_math.py` + `renwork-web-design-master`)**
   - **Single Source of Truth**: `src/styles/design-tokens.css`, `DESIGN.md`, and `private/brand-tokens.json`.
   - **Mandatory Rule**: Enforce the 6 Anti-AI-Slop Rules, WCAG >= 4.5:1 button contrast, `font-variant-numeric: tabular-nums` on spec tables, `&nbsp;` between numbers and units, Latin `65ch` / CJK `36em` / RTL `dir="rtl"` rules, and viewport verification across `320/390/768/1440px` and `200%` zoom.

4. **Phase 4: Compiler, 10-Item Dual Audit, Edge Protection Bundle & Indexing Closure (`site_compiler.py` + `validate_site.py` + `seo_geo_matrix.py`)**
   - **Single Source of Truth**: `builds/site-*/`, `private/deploy/edge-*/` (`worker.mjs` + `wrangler.json` + `policy.json`), `acceptance.md`, `docs/seo/status-log.md`, and `private/backlink-ledger.json`.
   - **Mandatory Rule**: Deploy only via the generated Cloudflare Workers `deployment_directory` bundle (`run_worker_first: true`, `READ_LIMITER=300/60s`, `INQUIRY_LIMITER=5/60s`, `verifiedBot` exemption, `X-Frame-Options: DENY`). Never upload the root project directory containing `private/`. Record de-identified lessons via `scripts/record_learning.py`.
