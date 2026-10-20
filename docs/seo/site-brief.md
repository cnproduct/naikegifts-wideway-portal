# B2B Independent Site Brief (Single Source of Truth · V4.0)

- **Company Name**: Jinjiang Naike Promo Co., Ltd. (Custom Swag Factory)
- **Industry Blueprint**: `toys-sports` (玩具与运动器材)
- **Compiler DOM Layout (`data-layout`)**: `oem`
- **Visual Archetype**: `agile_oem_lookbook` (Editorial high-contrast neutral canvas with bespoke brand-extracted accent token)
- **Typography Pairing**: Syne / General Sans (headings) + Plus Jakarta Sans (body) + JetBrains Mono (GSM/oz, MOQ, carton specs)
- **Current Data Maturity Stage**: **M2** — M2 (Test Reports + Verified Cases + Search Data): Ready for full 10-page release, evidence-backed case pages, and localized market expansion.
- **Primary Seed Keyword**: `custom corporate swag`
- **Pillar Homepage Keyword**: `custom corporate swag manufacturer`
- **Target Export Markets**: US, EU, UK, AU, CIS
- **Generated At**: 2026-10-20T02:14:23.907461+00:00

## 1. Industry Procurement Blueprint (From `assets/industries.json`)
- **Target B2B Buyers (`buyers`)**: 品牌商, 渠道采购, 礼品采购
- **Buyer Decision Sequence (`decision_path`)**: `使用者场景→结构材料→安全→包装→定制`
- **Mandatory Product Comparison Columns (`product_fields`)**: 年龄/使用者适用范围, 材料, 尺寸, 结构, 使用条件, 包装, 维护
- **Required Trust & Verification Evidence (`evidence`)**: 产品实拍, 测试范围, 标签, 说明书, 样品记录
- **Progressive Industry RFQ Fields (`rfq_fields`)**: 使用者, 用途, 材料, 数量, 市场, 包装/品牌
- **Missing-Data Fallback Strategy (`missing_data_fallback`)**: 先拆分具体品类，收集测试与用途，再决定可公开字段

## 2. Industry Red Lines (`red_lines` — Strictly Prohibited Unverified Claims)
- 🛑 不
- 🛑 编
- 🛑 年
- 🛑 龄
- 🛑 安
- 🛑 全
- 🛑 、
- 🛑 承
- 🛑 重
- 🛑 、
- 🛑 无
- 🛑 毒
- 🛑 或
- 🛑 法
- 🛑 规
- 🛑 达
- 🛑 标
- 🛑 ；
- 🛑 玩
- 🛑 具
- 🛑 与
- 🛑 运
- 🛑 动
- 🛑 用
- 🛑 品
- 🛑 分
- 🛑 别
- 🛑 核
- 🛑 实
- 🛑 用
- 🛑 途

## 3. RenWork V4 21-Module Fact & Asset Boundary Guardrails
- Every quantitative claim, specification row, certificate, or factory metric must trace to a verified atomic knowledge card (`RW-XXXXXX-XXXX`) in `private/knowledge-cards.json` exported via `sitekit.py export` to `content/public-facts.json`.
- Every public image or PDF must be registered in `private/asset-register.json` with verified `sha256`, `rights_status`, and boolean `is_ai_generated`. AI-generated illustrations must never impersonate certificates, test reports, factory photos, or customer cases.
