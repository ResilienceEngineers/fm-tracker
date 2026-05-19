# One-shot Day-81 events.csv schema migration (PowerShell).
# Adds indicator_class and tier columns; backfills existing rows;
# appends 28 new Day-81 research events.

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$events = Join-Path $repo "events.csv"

if (-not (Test-Path $events)) { throw "events.csv not found at $events" }

$existing = Import-Csv -Path $events -Encoding UTF8
Write-Host "Read $($existing.Count) existing rows"

if ($existing.Count -gt 0 -and $existing[0].PSObject.Properties.Name -contains "indicator_class") {
    Write-Host "Schema already migrated -- no-op"
    return
}

# Backfill existing rows with indicator_class=FM, tier=1
foreach ($row in $existing) {
    $row | Add-Member -NotePropertyName "indicator_class" -NotePropertyValue "FM" -Force
    $row | Add-Member -NotePropertyName "tier" -NotePropertyValue "1" -Force
}

function Get-EventId([string]$operator, [string]$chain, [string]$date) {
    $key = "$($operator.Trim().ToLower())|$($chain.Trim().ToLower())|$($date.Trim())"
    $sha = [System.Security.Cryptography.SHA1]::Create()
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($key)
    $hash = $sha.ComputeHash($bytes)
    return ([System.BitConverter]::ToString($hash).Replace("-","").ToLower()).Substring(0, 12)
}

$seen = @{}
foreach ($r in $existing) {
    $eid = Get-EventId $r.entity $r.chain $r.date
    $seen[$eid] = $true
}

$newEvents = @(
    [PSCustomObject]@{day="-22";entity="OFAC (US Treasury)";country="USA";chain="Iran shadow fleet crude+LPG";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="OFAC recent actions 20260206; Treasury press SB0341";notes="Initial Iran shadow-fleet designations targeting crude and LPG tankers (pre-crisis)";date="2026-02-06";indicator_class="Sanction";tier="1"},
    [PSCustomObject]@{day="-1";entity="OFAC (US Treasury)";country="USA";chain="Iranian oil trade";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Federal Register 2026-03988";notes="OFAC sanctions action including LUMA and NIBA tankers (pre-crisis)";date="2026-02-27";indicator_class="Sanction";tier="1"},
    [PSCustomObject]@{day="56";entity="OFAC (US Treasury)";country="USA";chain="Iranian petroleum exports";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Treasury press; GovPing 2026-04-24";notes="19 entities + 19 vessels designated under EO 13902; targets Hengli Petrochemical (Dalian) refinery";date="2026-04-24";indicator_class="Sanction";tier="1"},
    [PSCustomObject]@{day="56";entity="OFAC General License V";country="USA";chain="Iranian petroleum exports";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Treasury press 2026-04-24";notes="General License V issued - 30-day wind-down for transactions with Hengli Petrochemical (Dalian)";date="2026-04-24";indicator_class="Sanction";tier="1"},
    [PSCustomObject]@{day="1";entity="Iran Civil Aviation Organization";country="Iran";chain="Aviation / airspace";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Iran CAO NOTAM; Liveuamap";notes="Emergency NOTAM closing all Iranian airspace (Tehran FIR / OIIX) to commercial aviation";date="2026-02-28";indicator_class="NOTAM";tier="1"},
    [PSCustomObject]@{day="1";entity="EASA";country="EU";chain="Aviation / airspace";wave="";fm_type="";volume_kt="";is_eu_direct="True";source="EASA CZIB 2026-03 initial issue";notes="Conflict Zone Information Bulletin for Middle East / Persian Gulf airspace - initial issue";date="2026-02-28";indicator_class="NOTAM";tier="1"},
    [PSCustomObject]@{day="54";entity="Iran CAO (partial reopen)";country="Iran";chain="Aviation / airspace";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Safe Airspace 22 Apr";notes="Iranian domestic flights resumed; international routes remain suspended (Tehran FIR partial)";date="2026-04-22";indicator_class="NOTAM";tier="1"},
    [PSCustomObject]@{day="62";entity="EASA CZIB R8";country="EU";chain="Aviation / airspace";wave="";fm_type="";volume_kt="";is_eu_direct="True";source="EASA CZIB 2026-03-R8; Ops Group";notes="CZIB 2026-03 revision R8 issued; validity extended to 5 May 2026";date="2026-04-30";indicator_class="NOTAM";tier="1"},
    [PSCustomObject]@{day="64";entity="UAE GCAA + GCC CAAs";country="UAE/GCC";chain="Aviation / airspace";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Gulf Business 2 May; UAE GCAA";notes="Full resumption of air traffic operations in UAE; Qatar/Bahrain/Kuwait reopen airspace after large-scale closures";date="2026-05-02";indicator_class="NOTAM";tier="1"},
    [PSCustomObject]@{day="74";entity="EASA CZIB R10";country="EU";chain="Aviation / airspace";wave="";fm_type="";volume_kt="";is_eu_direct="True";source="EASA CZIB 2026-03-R10";notes="CZIB 2026-03 revised (R10); validity extended to 27 May 2026; recommendations amended";date="2026-05-12";indicator_class="NOTAM";tier="1"},
    [PSCustomObject]@{day="1";entity="MARAD (US DOT)";country="USA";chain="Maritime / Hormuz";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="MARAD MSCI 2026-001A";notes="MSCI 2026-001A - Strait of Hormuz / Persian Gulf - Iranian military operations and potential retaliatory strikes";date="2026-02-28";indicator_class="NAVTEX";tier="1"},
    [PSCustomObject]@{day="16";entity="MARAD (US DOT) MSCI-001B";country="USA";chain="Maritime / Hormuz";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="MARAD MSCI 2026-001B (date approx)";notes="MSCI 2026-001B revision - ongoing risk environment; updates to 001A";date="2026-03-15";indicator_class="NAVTEX";tier="1"},
    [PSCustomObject]@{day="47";entity="MARAD (US DOT) MSCI-004";country="USA";chain="Maritime / Hormuz";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="MARAD MSCI 2026-004 (date approx)";notes="MSCI 2026-004 - Iranian attacks on commercial vessels (Persian Gulf / Hormuz / Gulf of Oman)";date="2026-04-15";indicator_class="NAVTEX";tier="1"},
    [PSCustomObject]@{day="65";entity="UKMTO Advisory 040";country="UK";chain="Maritime / Hormuz";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="UKMTO Advisory 040 (JMIC 03 May)";notes="Bulk carrier attacked by multiple small craft 11nm west of Sirik, Iran; crew safe";date="2026-05-03";indicator_class="NAVTEX";tier="1"},
    [PSCustomObject]@{day="67";entity="UKMTO Advisory 041";country="UK";chain="Maritime / Hormuz";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="UKMTO Advisory 041 (JMIC 05 May)";notes="US naval units in Hormuz repel threats; aggressive Iranian hailing; mines possible in/near TSS; GNSS interference sporadic";date="2026-05-05";indicator_class="NAVTEX";tier="1"},
    [PSCustomObject]@{day="76";entity="UKMTO (Fujairah boarding)";country="UK";chain="Maritime / Fujairah";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="UKMTO; gCaptain 14 May";notes="Vessel boarded by unauthorized personnel 38nm NE of Fujairah; taken toward Iranian territorial waters";date="2026-05-14";indicator_class="NAVTEX";tier="1"},
    [PSCustomObject]@{day="3";entity="Lloyd's market (AWRP surge)";country="UK";chain="War-risk insurance";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Lloyd's List LL1156586";notes="Additional War Risk Premium surged 5x to 1-5% of hull value within 48h of 28 Feb airstrikes; VLCC quotes 10-14M USD per Hormuz transit";date="2026-03-02";indicator_class="Insurance";tier="2"},
    [PSCustomObject]@{day="4";entity="Lloyd's Joint War Committee";country="UK";chain="War-risk insurance";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Lloyd's List; LMA";notes="JWC Listed Areas expanded - Bahrain, Djibouti, Kuwait, Oman, Qatar added; entire Arabian Gulf designated conflict zone";date="2026-03-03";indicator_class="Insurance";tier="1"},
    [PSCustomObject]@{day="20";entity="Lloyd's CEO statement";country="UK";chain="Insurance market";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Insurance Journal 19 Mar";notes="Public statement: critical that Mideast war cover remains available; warns of structural market withdrawal";date="2026-03-19";indicator_class="Insurance";tier="2"},
    [PSCustomObject]@{day="12";entity="IEA emergency release";country="Global";chain="Crude oil / reserves";wave="";fm_type="";volume_kt="400000";is_eu_direct="False";source="IEA news 11 Mar";notes="Largest-ever coordinated emergency oil stock release - 400 million barrels across IEA member countries";date="2026-03-11";indicator_class="Reserve";tier="1"},
    [PSCustomObject]@{day="12";entity="US DOE SPR release";country="USA";chain="Crude oil / SPR";wave="";fm_type="";volume_kt="172000";is_eu_direct="False";source="US Treasury; CNBC";notes="US SPR release of 172 Mbbl announced - 43% of IEA coordinated draw; 41% of pre-release SPR";date="2026-03-11";indicator_class="Reserve";tier="1"},
    [PSCustomObject]@{day="70";entity="IEA drawdown update";country="Global";chain="Crude oil / reserves";wave="";fm_type="";volume_kt="164000";is_eu_direct="False";source="IEA update; Discovery Alert 8 May";notes="~164 Mbbl deployed (41% of commitment); adds ~2.5 Mbpd to effective market supply during drawdown";date="2026-05-08";indicator_class="Reserve";tier="1"},
    [PSCustomObject]@{day="7";entity="GAIL India (RLNG allocation)";country="India";chain="LNG / gas";wave="3";fm_type="4";volume_kt="";is_eu_direct="False";source="Indian Chemical News";notes="RLNG allocation restriction effective 6 March; impacts Neem Urea downstream production";date="2026-03-06";indicator_class="FM";tier="1"},
    [PSCustomObject]@{day="59";entity="EU Commission (REACH cancel)";country="EU";chain="Chemical regulation";wave="";fm_type="";volume_kt="";is_eu_direct="True";source="CIRS Group; EU Commission press";notes="REACH 2.0 comprehensive revision cancelled; cited energy-crisis impact on EU chemical industry";date="2026-04-27";indicator_class="Regulatory";tier="1"},
    [PSCustomObject]@{day="26";entity="Morgan Stanley PE/PP";country="USA";chain="Petchem PE / PP";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="Morgan Stanley note via ChemAnalyst";notes="Sell-side quantification: 1.4% of global PE capacity and 1.0% of global PP capacity under FM";date="2026-03-25";indicator_class="Industry";tier="2"},
    [PSCustomObject]@{day="55";entity="Cefic (EU chemical industry)";country="EU";chain="Chemical industry energy";wave="";fm_type="";volume_kt="";is_eu_direct="True";source="Cefic news; EU policy briefing";notes="Public statement: EU chemical industry approaching point of no return; first plant closures already underway";date="2026-04-23";indicator_class="Industry";tier="2"},
    [PSCustomObject]@{day="55";entity="IEA chief Birol";country="Global";chain="Energy security";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="CNBC 23 Apr interview";notes="Public statement: biggest energy security threat in history";date="2026-04-23";indicator_class="Geopolitical";tier="2"},
    [PSCustomObject]@{day="74";entity="Lufthansa Group (route susp)";country="Germany";chain="Aviation / routes";wave="";fm_type="";volume_kt="";is_eu_direct="True";source="The National 12 May";notes="Suspensions extended: TLV 30 Jun, DXB 11 Jul, AUH/AMM/BEY/DMM/RUH/EBL/MCT/IKA 24 Oct";date="2026-05-12";indicator_class="Industry";tier="2"},
    [PSCustomObject]@{day="74";entity="KLM (route susp)";country="Netherlands";chain="Aviation / routes";wave="";fm_type="";volume_kt="";is_eu_direct="True";source="The National 12 May";notes="RUH / DMM / DXB suspended until 28 June; continues avoiding Iran / Iraq / Israel airspace";date="2026-05-12";indicator_class="Industry";tier="2"},
    [PSCustomObject]@{day="74";entity="Qatar Airways (route susp)";country="Qatar";chain="Aviation / routes";wave="";fm_type="";volume_kt="";is_eu_direct="False";source="The National 12 May";notes="Iran flight suspensions extended to 30 June 2026";date="2026-05-12";indicator_class="Industry";tier="2"}
)

$appended = 0
$skipped = 0
$mergedRows = New-Object System.Collections.ArrayList
foreach ($r in $existing) { $null = $mergedRows.Add($r) }
foreach ($ev in $newEvents) {
    $eid = Get-EventId $ev.entity $ev.chain $ev.date
    if ($seen.ContainsKey($eid)) {
        Write-Host "SKIP (dupe): $($ev.date) - $($ev.entity) - $($ev.chain)"
        $skipped++
        continue
    }
    $seen[$eid] = $true
    $null = $mergedRows.Add($ev)
    $appended++
}

Write-Host "Appended $appended new rows; skipped $skipped dupes; total now $($mergedRows.Count)"

$newCols = @("day","entity","country","chain","wave","fm_type","volume_kt","is_eu_direct","source","notes","date","indicator_class","tier")
$mergedRows | Select-Object -Property $newCols | Export-Csv -Path $events -NoTypeInformation -Encoding UTF8
Write-Host "Wrote $events with $($mergedRows.Count) rows; schema: $($newCols -join ',')"
