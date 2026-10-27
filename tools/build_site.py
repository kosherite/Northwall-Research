"""Build the public site into _site/: front end, signed-in desk, public data, published PDFs and live prices.
No Excel models, model inputs or desk data are copied into the site."""
import glob, os, shutil, subprocess, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, "_site")
shutil.rmtree(out, ignore_errors=True); os.makedirs(os.path.join(out, "reports"))
subprocess.run([sys.executable, os.path.join(root, "tools", "make_state.py")], check=True)
subprocess.run([sys.executable, os.path.join(root, "app", "build.py"), "--site", out], check=True)
subprocess.run(["node", os.path.join(root, "tools", "public_data.js"), os.path.join(out, "public.json")], check=True)
for f in glob.glob(os.path.join(root, "reports", "published", "*.pdf")):
    shutil.copy(f, os.path.join(out, "reports"))
subprocess.run([sys.executable, os.path.join(root, "tools", "fetch_prices.py"), os.path.join(out, "prices.json"),
                "--previous", "https://kosherite.github.io/Northwall-Research/prices.json"], check=False)
open(os.path.join(out, ".nojekyll"), "w").close()
open(os.path.join(out, "robots.txt"), "w").write("User-agent: *\nDisallow: /desk/\n")
print("site ready:", sorted(os.listdir(out)))
