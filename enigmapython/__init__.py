import sys

# Try importing the original enigmapython package
try:
    import enigmapython
except ImportError:
    pass  # Handle gracefully if enigmapython is not available

# Block the 'XRay' module
class BlockedModule:
    def __getattr__(self, name):
        raise ImportError(f"Module '{name}' is not available in MicroPython.")

# Override 'enigmapython.XRay' to block it
sys.modules["enigmapython.XRay"] = BlockedModule()

# Optionally, you can still expose the rest of 'enigmapython' as needed
# e.g., expose only the compatible parts