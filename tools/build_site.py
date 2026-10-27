"""Build the public site into _site/: the web app, published PDFs, desk state and live prices."""
import glob, os, shutil, subprocess, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, "_site")
shutil.rmtree(out, ignore_errors=True); os.makedirs(os.path.join(out, "reports"))
subprocess.run([sys.executable, os.path.join(root, "app", "build.py"), "--site", out], check=True)
for f in glob.glob(os.path.join(root, "reports", "published", "*.pdf")):
    shutil.copy(f, os.path.join(out, "reports"))
state = os.path.join(root, "data", "state.json")
if os.path.exists(state):
    shutil.copy(state, os.path.join(out, "state.json"))
subprocess.run([sys.executable, os.path.join(root, "tools", "fetch_prices.py"), os.path.join(out, "prices.json"),
                "--previous", "https://kosherite.github.io/Northwall-Research/prices.json"], check=False)
open(os.path.join(out, ".nojekyll"), "w").close()
print("site ready:", sorted(os.listdir(out)))
