# B2B Landing Page CRO, Interactive Workbench & Copywriting Deck (V4.0)

> **Strict Alignment Rule**: Every H1 and H2 below MUST preserve the target keyword assigned in `docs/seo/keyword-matrix.json` (including in the Clean URL slug, `<title>`, `<h1>`, and first 100 words). Obey the industry `decision_path` (`使用者场景→结构材料→安全→包装→定制`) and never violate `red_lines`.

## 1. First-Viewport Interactive B2B Workbench (`Zero-Signup Friction` Hero)
- **H1 Formula**: `[Verified Custom Corporate Swag Supply / Manufacturing] for [品牌商, 渠道采购, 礼品采购]`
- **Subheadline (constrained to `<= 65ch` Latin / `<= 36em` CJK)**: Highlight verifiable engineering parameters (年龄/使用者适用范围, 材料, 尺寸, 结构), batch quality control, and direct response without middleman markups.
- **Direct Action Workbench (Above the Fold)**: Embed a 1-click Material/Spec Preset Switcher or Mini 20GP/40HQ Carton Load Estimator (`sourcing_estimator.js`) directly in the first viewport. Product CTAs pass context via `/contact/?product=<Model>#inquiry`.

## 2. Asymmetrical 12-Column 4-Step B2B OEM / Sourcing Workflow (`data-layout="oem"`)
Render using a 12-column asymmetrical split (4-col sticky engineering header on left + 8-col structured steps on right):
1. **Spec & BOM Alignment**: Share target parameters (使用者, 用途, 材料) or reference sample specs.
2. **Engineering DFM & Prototype Sampling**: Confirm pre-production sample and lab test criteria (产品实拍, 测试范围, 标签).
3. **In-Line QC & Pre-Shipment Inspection**: Batch traceability and AQL inspection prior to container sealing.
4. **Export Packaging & Global Logistics**: Palletized or floor-loaded 20GP/40HQ shipment with full customs documentation.

## 3. B2B Risk Reversal & 3-Tier Commercial Inquiry Matrix (Replaces SaaS Paywalls)
Never place paywalls on B2B specifications. Use a 3-Tier Commercial Inquiry Matrix paired with progressive `email_draft` (default) or `http` (`rfq_daemon.py` with HMAC math captcha & honeypot):

| Tier | Target Buyer Stage | Commercial Scope | Risk Reversal Micro-Copy | Primary Action |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Standard Sample & Spec Pack** | Engineering Evaluation | Existing tooling models & material swatches | Strict NDA protection; courier freight credit on first bulk order | `Request Standard Sample Pack` |
| **Tier 2: Custom OEM / ODM Project** | Private Label / Custom Spec | Custom material allocation, logo tooling, bespoke packaging | Golden sample sign-off before mass production; documented QC gates | `Submit Custom BOM / Drawing RFQ` |
| **Tier 3: Bulk Container Procurement** | Repeat Wholesale / 20GP-40HQ | Mixed-SKU container loading & tiered FOB volume pricing | Pre-shipment third-party inspection support (SGS/Intertek/BV) | `Calculate Container Load & Get FOB Quote` |

## 4. Intent-Driven Procurement FAQ (5-8 Real Buyer PAA Questions)
Answer concrete buyer questions regarding MOQ mixing across SKUs, mold/tooling ownership, sample lead times, pre-shipment AQL standards, and payment/incoterms (`FOB`, `CIF`, `DDP`), feeding `src/components/seo/B2bJsonLd.tsx`.
