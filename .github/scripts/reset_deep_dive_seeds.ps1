# One-shot: reset industryData and goldenScrewData in index.html + brief.html
# to a clean curated seed. Fixes the 238/223-entry bloat + missing-comma
# syntax errors that broke the JS parser on the live page.

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

$industrySeed = @'
{ name: "Healthcare & Pharma", severity: "Critical", commodities: ["Helium", "BASF excipients", "MCC", "CO2"], pathway: "MRI scanners depend on Qatar helium; BASF excipient +20% already realised; vaccine cold-chain CO2 comes from urea plants now offline.", hidden: "An MRI helium leak triggers a 6-month rebuild cycle even if helium returns next week." },
{ name: "Automotive & Heavy Transport", severity: "Critical", commodities: ["Aluminium", "AdBlue/Urea", "Naphtha to interiors", "Butadiene to tyres"], pathway: "EGA/ALBA aluminium gap hits body panels and EV battery housings; AdBlue scarcity is a legal block on EU diesel truck operation.", hidden: "AdBlue is a regulatory chokepoint, not a material one - fleets stop in 24h if missing, before any factory runs out of metal." },
{ name: "Semiconductor & Electronics", severity: "Critical", commodities: ["Helium", "High-purity Al sputter", "Methanol cleaning", "Isocyanates"], pathway: "Airgas FM puts US fabs on rationing; sputter targets, wafer purge gas, chip-packaging encapsulants all tied to ME chains.", hidden: "Fab schedules slip 6-10 weeks before throughput drops show in earnings - the lag hides the damage." },
{ name: "Food & Beverage", severity: "Critical", commodities: ["Urea fertilizer", "Food-grade CO2", "PET/MEG", "Aluminium foil"], pathway: "Urea cut hits crop yields; food-grade CO2 is a co-product of ammonia plants, so beverage carbonation and MAP packaging dry up at retail.", hidden: "Hospitals competing with breweries for the same CO2 stream - happened in 2018 and 2022 from ammonia outages." },
{ name: "Aerospace & Aviation", severity: "High", commodities: ["Jet fuel", "Aerospace Al", "Specialty lubricants", "Helium"], pathway: "Lufthansa 31 grounded, KLM 80 cancelled, 20k flights cut May-Oct; aerospace-grade Al backlog from EGA hits airframe deliveries by Q4.", hidden: "Helium also feeds missile-guidance gyros and satellite pressurisation - defence quietly competes with healthcare." },
{ name: "Construction & Insulation", severity: "High", commodities: ["MDI/TDI isocyanates", "Methanol to formaldehyde", "PVC", "Urea-melamine"], pathway: "Wanhua + Sadara cover roughly half of global TDI/MDI capacity - both under FM. PU foam for insulation panels and roofing constrained.", hidden: "EU building-energy retrofits depend on PU foam at scale; new isocyanate capacity takes years, not quarters." },
{ name: "Power & Energy Infrastructure", severity: "High", commodities: ["LNG turbines", "Aluminium HV", "BAPCO base oils"], pathway: "EU gas-fired generation, transmission upgrades, data-centre buildouts all under cost and timing pressure.", hidden: "Wind-turbine gearboxes need PAO synthetic base oils - a single OEM-specified grade, not interchangeable with abundant alternatives." },
{ name: "Defence & Maritime", severity: "High", commodities: ["Aerospace Al", "Helium avionics", "Specialty steels", "Stealth-coating isocyanates"], pathway: "Naval platforms, military aviation, missile systems all hit by qualification-grade Al + helium constraints.", hidden: "EGA Al Taweelah carried defence-qualified lines that take 9-12 months to re-qualify elsewhere." },
{ name: "Packaging & Consumer Goods", severity: "High", commodities: ["PET/MEG bottles", "Al foil/cans", "PP containers", "PA6 caprolactam"], pathway: "Sinopec CPDC caprolactam halt + Asian PET starvation + Al foil scarcity cascade to FMCG packaging costs +20-30%.", hidden: "Beverage carbonation, food-grade sealants and can-coating epoxies all depend on chains hit by different FMs - a single-chain fix does not restore the aisle." },
{ name: "Solar & Renewable Energy", severity: "Medium", commodities: ["EVA encapsulants", "Polysilicon precursors", "Aluminium frames"], pathway: "Solar module makers single-qualify EVA grades from Wanhua and Sumitomo.", hidden: "A 4-6 month EVA delay slips project IRR enough to push deals past financial close - paper losses cascade to debt covenants." },
{ name: "Textile & Apparel", severity: "Medium", commodities: ["PA66", "PET fibre", "Spandex precursors"], pathway: "Synthetic clothing, athleisure, technical fabrics, carpets all on Asian-cracker feedstock.", hidden: "PA66 is also the structural polymer for vehicle seatbelts and airbag fabrics - Invista's adipic-acid FM threatens automotive recall before apparel margin." },
{ name: "Water & Sanitation", severity: "Medium", commodities: ["Aluminium sulfate", "Chlorine / NaOH", "PVC pipes"], pathway: "Municipal water treatment plants and new sewage infrastructure both depend on chlor-alkali output from Tianjin Bohua and Sulfindo.", hidden: "Tianjin Bohua's 50% caustic cut spreads quietly through utilities in low- and middle-income markets - waterborne-disease incidence ticks up by Q3 if it persists." }
'@

$goldenScrewSeed = @'
{ component: "MRI helium cryogen", industry: "Healthcare imaging", risk: "Single-source Qatar field; loss = no MRI for surgery prep, no leak-detection for fabs, no avionics cooling. No drop-in substitute.", fm: "QatarEnergy production halt + Airgas formal distribution FM", severity: "Critical", sub_time: "No substitute - 6-mo rebuild if leak" },
{ component: "AdBlue / DEF urea", industry: "Diesel road transport", risk: "EU emissions rules forbid diesel operation without DEF. 7-day shortage cascades into immobilised heavy-truck fleets. Grocery + pharma logistics first hit.", fm: "QAFCO + SABIC Agri + Industries Qatar (urea)", severity: "Critical", sub_time: "72h operational cliff" },
{ component: "Solar EVA encapsulants", industry: "Renewable energy projects", risk: "Module makers single-qualify EVA grade. 4-6 month requalification lag. Project IRR slips trigger debt covenant breaches before any farm goes dark.", fm: "Wanhua + Sumitomo (TDI/EVA cascade)", severity: "High", sub_time: "4-6 months requalify" },
{ component: "Food-grade CO2", industry: "Beverage + vaccine cold chain", risk: "Co-product of ammonia synthesis. When urea plants halt, food-grade CO2 vanishes. Beer, soda, MAP meat packaging, dry ice for vaccines share the same supply.", fm: "QAFCO / KAFCO / SABIC Agri (urea/ammonia chain)", severity: "Critical", sub_time: "No commercial substitute at scale" },
{ component: "PA66 polymer (nylon 66)", industry: "Automotive safety / industrial", risk: "Seatbelts, airbag fabric, engineering plastics. Invista FM cascades to PA66 chip availability; safety-critical recall risk if alt grades not pre-qualified.", fm: "Invista Shanghai + Radici (adipic acid)", severity: "High", sub_time: "6-9 months qualify alternate grade" },
{ component: "High-purity MEG (food-contact PET)", industry: "Beverage packaging", risk: "MEG-2 purity needed for food-contact PET. EQUATE EG-2 suspension narrows qualified suppliers to ~5. Brand owners face shortage rather than grade substitution.", fm: "EQUATE + TKSC + Hanwha Solutions", severity: "High", sub_time: "Contract cycle - 3-6 months" },
{ component: "Wind turbine PAO base oils", industry: "Renewable energy O&M", risk: "PAO grades for gearboxes are OEM-specified. BAPCO base oil interruption stops scheduled turbine servicing - turbines fail open, unplanned outages weeks-to-months later.", fm: "BAPCO base oils (380 kt/yr FM Day 9)", severity: "High", sub_time: "OEM re-spec 6+ months" },
{ component: "Specialty isocyanates (TDI/MDI)", industry: "Insulation foam, auto seating, footwear", risk: "Wanhua + Sadara together cover roughly half of global TDI/MDI capacity. Both under FM. PU foam for buildings, mattresses, vehicle interiors competes with footwear soles for residual.", fm: "Wanhua Chemical + Sadara Chemical (full plant shutdown)", severity: "Critical", sub_time: "New capacity: years" }
'@

function Replace-Block([string]$file, [string]$startMarker, [string]$endMarker, [string]$body) {
    $content = [System.IO.File]::ReadAllText($file, [System.Text.UTF8Encoding]::new($false))
    $pattern = "(?s)(// $([regex]::Escape($startMarker))\r?\n)(.*?)(\r?\n// $([regex]::Escape($endMarker)))"
    $rx = [regex]::new($pattern)
    if (-not $rx.IsMatch($content)) { throw "Markers not found in $file for $startMarker" }
    $new = $rx.Replace($content, {
        param($m)
        return $m.Groups[1].Value + $body + $m.Groups[3].Value
    }, 1)
    [System.IO.File]::WriteAllText($file, $new, [System.Text.UTF8Encoding]::new($false))
    Write-Host "  updated $startMarker in $(Split-Path $file -Leaf)"
}

foreach ($file in @("$repo\index.html", "$repo\brief.html")) {
    Write-Host "Processing $file"
    Replace-Block $file "BRIEF:INDUSTRY_DATA_START" "BRIEF:INDUSTRY_DATA_END" $industrySeed
    Replace-Block $file "BRIEF:GOLDEN_SCREW_DATA_START" "BRIEF:GOLDEN_SCREW_DATA_END" $goldenScrewSeed
}
Write-Host "Done."
