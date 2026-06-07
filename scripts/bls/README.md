# BLS/O*NET Scripts

Maintained scripts for extracting role-quality and labor-market-direction
features from `data/bls`.

## Compact SOC Occupation Table

```bash
python3 scripts/bls/extract-soc-occupation-table.py
```

Outputs:

- `data/bls/compact/soc_occupation_compact.csv`
- `data/bls/bls-audit.md`

The compact table combines:

- O*NET occupation identity and descriptions.
- O*NET alternate titles.
- O*NET job zones.
- Selected O*NET ability and recipe Level scores.
- Latest BLS OEWS national employment and wage estimates.

Use the compact table for downstream scoring. Keep the full `data/bls` archive
as source/reference provenance.
