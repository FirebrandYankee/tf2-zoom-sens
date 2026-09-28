from math import tan, atan, radians

# ---- user settings ----
FOV = 90                # your fov_desired
WIDTH = 1152            # your resolution
HEIGHT = 720
# -----------------------

def zoomsens(zoom, hip, target):
    return atan(target * tan(atan(tan(radians(zoom) / 2) * (3/4)))) / atan(target * tan(atan(tan(radians(hip) / 2) * (3/4)))) / (zoom / hip)
SCOPE_FOV = 20
CENTER = 1e-52
aspect = WIDTH / HEIGHT
same_feel = zoomsens(SCOPE_FOV, FOV, CENTER)
same_degrees = FOV / SCOPE_FOV
same_pixels = zoomsens(SCOPE_FOV, FOV, aspect)

print(f'FOV {FOV}, {WIDTH}x{HEIGHT} (aspect {aspect:.4f})')
print(f'zoom_sensitivity_ratio {same_feel:.15f}   // same feel (crosshair)')
print(f'zoom_sensitivity_ratio {same_pixels:.15f}   // same pixels (screen edge)')
print(f'zoom_sensitivity_ratio {same_degrees:.15f}   // same degrees (equal cm/360)')
