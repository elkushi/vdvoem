import base64, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
SPR  = os.path.join(HERE, "sprites")
tpl  = open(os.path.join(HERE,"src/template.html"), encoding="utf-8").read()
entries=[]
for f in sorted(glob.glob(os.path.join(SPR,"*.png"))):
    key=os.path.splitext(os.path.basename(f))[0]
    b64=base64.b64encode(open(f,"rb").read()).decode()
    entries.append(f'  {key}: "data:image/png;base64,{b64}"')
out = tpl.replace("/*__SPRITES__*/{}", "{\n"+",\n".join(entries)+"\n}")

# Firebase config (optional): put it in firebase.json next to this script
cfg = os.path.join(HERE, "firebase.json")
if os.path.exists(cfg):
    raw = open(cfg, encoding="utf-8").read().strip()
    out = out.replace("/*__FIREBASE__*/null", raw)
    print("firebase: config embedded")
else:
    print("firebase: none (online mode disabled - add coop/firebase.json)")
dst = os.path.join(HERE,"index.html")
open(dst,"w",encoding="utf-8").write(out)
print(f"built {dst} — {len(out)/1024:.0f} KB, {len(entries)} sprites")
