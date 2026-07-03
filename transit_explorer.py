import matplotlib.pyplot as plt
import lightkurve as lk
import numpy as np
import os

# ==========================================================
# Transit Explorer Configuration
# ==========================================================
TARGET = "AU Mic"
MISSION = "TESS"
SECTOR = 1           # AU Mic активно изучалась в 1 секторе
QUARTER = None

PERIOD_MIN = 4.8
PERIOD_MAX = 4.9
PERIOD_STEP = 0.0001
TRANSIT_DURATION = 0.2
PHASE_WINDOW = 0.5
BIN_SIZE = 0.005
OUTPUT_DIR = "examples"

def download_lightcurve():
    """Download raw light curve data from MAST archive."""
    print("[1/6] Downloading data...")
    try:
        search = lk.search_lightcurve(TARGET, mission=MISSION, sector=SECTOR, quarter=QUARTER)
        if not search:
            print("Error: No observations found.")
            return None
        lc = search.download()
        if isinstance(lc, lk.LightCurveCollection):
            lc = lc[0]
        return lc
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def normalize_lightcurve(lc):
    """Normalize the light curve flux."""
    print("[2/6] Normalizing light curve...")
    return lc.normalize()

def find_period(lc):
    """Detect the dominant orbital period using the BLS algorithm."""
    print("[3/6] Searching for orbital period (BLS)...")
    period_range = np.arange(PERIOD_MIN, PERIOD_MAX, PERIOD_STEP)
    pg = lc.to_periodogram(method='bls', period=period_range, duration=TRANSIT_DURATION)
    return pg

def plot_results(lc, pg):
    """Visualize raw, normalized, periodogram, and phase-folded light curve."""
    print(f"[6/6] Saving visualization to {OUTPUT_DIR}/...")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    period = pg.period_at_max_power
    t0 = pg.transit_time_at_max_power
    folded = lc.fold(period=period, t0=t0).bin(time_bin_size=BIN_SIZE)
    
    
    fig, axes = plt.subplots(4, 1, figsize=(18, 14))
    
    # 1. Raw Data
    lc.scatter(ax=axes[0], color='gray', s=1)
    axes[0].set_title(f"Raw Data: {TARGET}")
    
    # 2. Normalized
    lc.scatter(ax=axes[1], color='royalblue', s=1)
    axes[1].set_title("Normalized Light Curve")
    
    # 3. Periodogram
    pg.plot(ax=axes[2], color='black')
    axes[2].set_title("BLS Periodogram")
    
    # 4. Phase-folded Transit Profile
    folded.scatter(ax=axes[3], color='darkred', s=10)
    axes[3].set_xlim(-PHASE_WINDOW, PHASE_WINDOW)
    axes[3].set_title(f"Phase-folded Transit Profile (P: {period.value:.5f} d)")
    
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/{TARGET.replace(' ', '_')}_transit.png")
    plt.close()

def main():
    print("=== Starting Transit Explorer ===")
    
    lc = download_lightcurve()
    if lc is None: return

    lc = normalize_lightcurve(lc)
    pg = find_period(lc)
    
    print("[4/6] Folding light curve...")
    plot_results(lc, pg)
    print("[5/6] Analysis completed successfully.")
    
    # Summary
    print(f"\n{'='*40}\nTransit Explorer Summary\n{'='*40}")
    print(f"Target:             {TARGET}")
    print(f"Mission:            {MISSION}")
    print(f"Sector/Quarter:     {SECTOR if SECTOR else QUARTER}")
    print(f"Detected Period:    {pg.period_at_max_power.value:.5f} days")
    print(f"Transit Duration:   {TRANSIT_DURATION} days")
    print(f"Observations:       {len(lc)}")
    print(f"Output Figure:      {OUTPUT_DIR}/{TARGET.replace(' ', '_')}_transit.png")
    print(f"{'='*40}\nAnalysis completed successfully.")

if __name__ == "__main__":
    main()