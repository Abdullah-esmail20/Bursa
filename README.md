# Bursa
# ACO - Bursa Route Optimization (Senaryo 3)

Streamlit application that optimizes a route between **12 school locations in Bursa** using **Ant Colony Optimization (ACO)**.  
Coordinates and pairwise travel distances are fetched from **Google Maps APIs** (Geocoding + Distance Matrix), then the best tour is visualized on an interactive **Folium** map with a convergence plot.

## Demo Output
- Best total route distance (km)
- Best tour indices + resolved place addresses
- Convergence chart (best distance per iteration)
- Interactive map (markers + polyline route)

## Tech Stack
- Python
- Streamlit
- NumPy
- Matplotlib
- Folium + streamlit-folium
- Google Maps Platform (`googlemaps` client)

## Project Files
Your code assumes this structure:

```text
.
├─ main.py              # Streamlit UI (route optimization + plots + map)
├─ maps.py              # Geocoding + Distance Matrix via Google Maps APIs
├─ aco.py               # ACO implementation (run_aco)
├─ schools.py           # List of 12 locations (SCHOOLS)
├─ requirements.txt
└─ .streamlit/
   └─ secrets.toml      # contains GOOGLE_MAPS_API_KEY (DO NOT COMMIT)
