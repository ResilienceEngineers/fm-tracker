# Sources — Force Majeure Tracker

**Status:** Internal. The public site shows tier descriptions only — no specific outlet names. This stays here so the daily updater can target searches and the team can audit reliability.

Tier discipline matters more than the list. A Tier-1 source that sloppily cites Tier-6 input gets demoted in the reliability tally; a Tier-3 outlet that consistently surfaces verified primary documents gets watched closely.

---

## Tier 1 — Primary, official, verifiable

First-party operator and regulator output. Move-the-needle authority for Wave Intensity.

- Company press releases and customer FM letters: QatarEnergy, Saudi Aramco, SABIC, Sadara, EQUATE, KPC, KNPC, BAPCO, ALBA, EGA, Borouge, Hindalco, LG Chem, Lotte Chemical, Yeochun NCC, Hanwha Solutions, Mitsui Chemicals, ENEOS, Wanhua, Formosa, Chandra Asri, TPC Singapore, OMV, Orlen Unipetrol, LyondellBasell, Inovyn, INEOS, Trinseo, Vynova, Sasol, Methanex, Invista, Radici, Excelerate Energy, OQ Trading, Petronet LNG, GAIL India, Targa Resources, Chevron Phillips Chemical, Dow, Mitsubishi Gas Chemical, Shell, TotalEnergies, MRPL.
- Stock-exchange filings: Tadawul (KSA), Bursa Saudi, BSE / NSE (India), KOSPI (Korea), SGX (Singapore), Tokyo / Osaka, LSE, NYSE, NASDAQ, Euronext.
- Regulator notices: ANSM (France medicines), EMA, FDA shortage list, EIA / IEA primary releases, OPEC+ secretariat communiqués, IMO circulars.
- Sovereign / central bank: Bank of England, ECB, BIS, US Treasury OFAC sanctions designations.
- Lloyd's List Intelligence AIS-confirmed vessel positions (paid).

## Tier 2 — Specialised commercial intelligence

Operational track record, named analysts, paid wire services. Can hold Hard tier when corroborated by Tier 1.

- Energy / petchem trade press: Argus Media, ICIS, S&P Global Platts, OPIS, Chemical Week, C&EN, Hydrocarbon Processing, Polymerupdate, ChemAnalyst, ResourceWise, Plasteurope, Kunststoffweb.
- Maritime: Lloyd's List, TradeWinds, Baird Maritime, Ship & Bunker, Splash247.
- Metals / minerals: Mining Weekly, Mining.com, alcircle, Metal Bulletin, MoneyDJ.
- Specialist regional: Bloomberg / Reuters / Dow Jones primary wire (when sourcing operator confirmation, not analyst speculation).

## Tier 3 — Analytical institutions

Rigorous publication standards. Useful for context, not for moving Wave Intensity alone.

- Carnegie Endowment, IISS, RUSI, Atlantic Council, CSIS, Chatham House, IFRI, SWP Berlin, Bruegel, ECIPE.
- Multilateral: IMF working papers, World Bank commodity desks, USGS Mineral Commodity Summaries, FAO commodity briefs.
- Industry associations: AGBI (Arab Gulf Business Insight), GPCA, Cefic, AmCham Gulf, Eurogas.

## Tier 4 — Commercial analysts and columnists

Multi-year track records named in print. Hold their positions accountable in the source-reliability tally.

- Morgan Stanley commodities desk, Goldman Sachs commodity research, JPM commodity strategy, Citi metals research.
- Specialist columnists: John Kemp (Reuters), Javier Blas (Bloomberg), David Sheppard (FT), Helima Croft (RBC).
- Long-form: Carnegie Hormuz analysts, Atlantic Council energy specialists.

## Tier 5 — Wire services and reputable regional press

Useful for surfacing leads. Always traced upward to a Tier-1/2 source before tier-Hard scoring.

- Reuters general, AP, AFP, dpa.
- Regional: The National (UAE), Gulf Business, Times of India, Korea Economic Daily / Seoul Economic Daily, Nikkei Asia, Mainichi, South China Morning Post, Express Tribune, Business Recorder, Daily News Egypt.
- Sectoral: World Fertilizer, Mining Weekly, Polymerupdate weekly, Bitget.

## Tier 6 — Excluded by default

Admitted only if the same claim is independently corroborated by Tier 1–3.

- Anonymous OSINT accounts (Twitter / X / Telegram).
- Op-eds and opinion columns.
- AI-summarised aggregator output (Bing AI, Google AI, ChatGPT-style summaries from third-party news sites).
- Whalesbook / chemall / regional aggregator translations without primary citation.

---

## Daily updater search targets

The daily updater is told to search this set in this order:

1. Tier-1 first-party releases for the named operators in the active FM list.
2. Argus / ICIS / Platts / OPIS / Chemical Week for the last 24h on naphtha / LNG / urea / aluminium / methanol / helium / jet fuel.
3. Lloyd's List + Baird Maritime for shipping / port / bunker FMs.
4. Tadawul + Bursa Saudi + BSE filings for FM-related disclosures.
5. Reuters wire for sovereign / regulator statements.
6. Polymerupdate weekly + Plasteurope for European petchem cascade.

Anything from outside this set gets flagged in the backtest log and held to Tier-2 corroboration before publication.

---

## Source reliability tally

Maintained weekly. A source falling below 0.6 hit rate over 4 weeks is downgraded one tier.

| Source | 4w hit rate | Action |
|---|---|---|
| _to be populated as runs accumulate_ | | |
