# MLB Non-K Prop Engine v12.1

Separate non-K prop app. Strikeouts/K picks are hidden and K model logs are not written from this screen.

Upgrades in v12.1:
- Batter-specific calibration shell (`non_k_result_log.json`)
- Plate appearance projection by lineup slot
- Bullpen matchup layer
- Lineup-slot weighting
- Hitter volatility engine
- Handedness matchup layer
- H+R+RBI correlation logic

Run locally:
```bash
pip install -r requirements.txt
streamlit run app.py
```
