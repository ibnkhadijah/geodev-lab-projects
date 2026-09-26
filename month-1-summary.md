# Month 1 summary

## Question
Which wards in Kano Municipal LGA have the lowest accessibility to healthcare facilities within a 15-minute travel time?

## Operation
Buffered health facilities by 2,000 metres (approximating a 15-minute walk), dissolved the result, then took the difference against ward boundaries to find the uncovered percentage of each ward.

## Expected
Most central wards covered. One or two peripheral wards with gaps.

## Got
Two wards — Gandun Albasa and Sharada — have significant areas beyond 2 km from any mapped health facility. The other 11 wards are fully within the buffer.

Manual verification of every ward confirmed the pattern:
- Gandun Albasa: western edge up to 2,905 m from nearest hospital; southern edge 2,177 m.
- Sharada: centre 2,672 m from nearest facility.
- All other wards: maximum measured distance ≤ 2,000 m.

## What surprised me
The completeness of OSM health facility data for Kano Municipal is lower than I expected. Only three facilities appear in the extract, 
and I know for certain that at least one or more clinic exists. With just three facilities buffered at 2 km, 11 of 13 wards are technically "covered," 
which is almost certainly optimistic. The uncovered result for Gandun Albasa and Sharada is therefore real, 
but the overall picture of access is likely better than this analysis suggests — and I cannot say by how much.

## Limitations, stated plainly
- Straight-line distance, not travel distance. A ward within 2 km across a river or a wall is not actually 2 km on foot.
- OSM facility data is incomplete by an unknown margin.
- Only two facility types were reliably tagged (hospital, clinic); pharmacies and health posts were sparse.
- 2 km is a rough proxy for 15 minutes of walking and does not account for terrain or road network.

## What I still need
- Road network with surface tags, for travel distance in Month 5.
- Population per ward, to convert area uncovered into people uncovered — the number that actually matters.
- GRID3 health facilities layer as a second source, to compare against OSM and check the completeness gap.

  <img width="3507" height="2480" alt="kano_accessibility_map" src="https://github.com/user-attachments/assets/178ba7bc-cc2f-42d5-9094-e03c0acb45dd" />
