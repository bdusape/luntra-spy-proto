# check_app.py
# Purpose: To inspect the FastAPI `app` object and list all registered routes.

import sys
from fastapi.routing import Mount

print("--- Diagnostic Tool Running ---")
print(f"Python executable: {sys.executable}")

try:
    # Attempt to import the application object from your main script
    from main import app
    print("✅ Successfully imported 'app' from main.py\n")
except ImportError as e:
    print(f"❌ ERROR: Failed to import 'app' from main.py.")
    print(f"   Details: {e}")
    print("   Please ensure 'check_app.py' is in the same directory as 'main.py'.")
    exit()

print("--- Registered Routes in your FastAPI Application ---")
if not app.routes:
    print("No routes found.")

for route in app.routes:
    if isinstance(route, Mount):
        # This is for app.mount()
        print(f"MOUNTED ROUTE:")
        print(f"  Path: {route.path}")
        print(f"  Name: {route.name}\n")
    else:
        # This is for @app.get(), @app.post(), etc.
        print(f"API ROUTE:")
        print(f"  Path: {route.path}")
        print(f"  Name: {route.name}")
        print(f"  Methods: {list(route.methods)}\n")
print("--- End of Route List ---\n")


# --- Final Analysis ---
print("--- Analysis ---")
static_route_found = any(getattr(r, 'name', None) == 'static' for r in app.routes)

if static_route_found:
    print("✅ SUCCESS: The 'static' route is correctly registered in your app.")
    print("This is very strange. It means the code is correct, but the error persists.")
else:
    print("❌ DIAGNOSIS CONFIRMED: The 'static' route IS NOT registered.")
    print("This proves the version of main.py being run by the server does not contain the app.mount(...) line.")
    print("The issue is not your code, but a problem with file saving or the server process.")

