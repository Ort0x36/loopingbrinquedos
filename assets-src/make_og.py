"""Gera og-image.png (1200x630), a imagem de prévia do link.

Uso: python3 assets-src/make_og.py
Reaproveita a ilustração do pula-pula definida no index.html (ART.castle).
"""
import pathlib, re
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "index.html").read_text(encoding="utf-8")
consts = re.search(r'var P="#F28BB0".*?;\n', src).group(0)
sh = re.search(r"var SH=.*?;\n", src).group(0)
hl = re.search(r"var HL=.*?;\n", src).group(0)
castle = re.search(r" castle:(SH\+'.*?'),\n", src).group(1)

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito:wght@700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;height:630px;overflow:hidden;background:#FFF8EE;font-family:Nunito,sans-serif;color:#1B2A4A;position:relative}
.l{position:absolute;left:72px;top:64px;width:600px}
.wm{display:inline-flex;flex-direction:column;align-items:flex-start;font:600 64px/1 Fredoka;color:#2F6FCB}
.wm span{display:flex;align-items:center}
.wm svg{height:.6em;width:.9em;margin:0 .02em}
.sub{font:800 16px/1 Nunito;letter-spacing:.36em;color:#C2477F;margin:6px 0 0 4px}
h1{font:600 62px/1.04 Fredoka;letter-spacing:-.01em;margin-top:44px}
h1 em{font-style:normal;color:#2F6FCB;position:relative;z-index:0}
h1 em::after{content:"";position:absolute;left:-4px;right:-4px;bottom:6px;height:20px;border-radius:99px;background:#FFC83D;opacity:.6;z-index:-1}
p{font:700 26px/1.35 Nunito;color:#4A5876;margin-top:18px;max-width:540px}
.chips{position:absolute;left:72px;bottom:58px;display:flex;gap:12px}
.chip{display:inline-flex;align-items:center;gap:10px;height:54px;padding:0 24px;border-radius:99px;font:800 22px Nunito}
.c1{background:#1B2A4A;color:#fff}.c2{background:#1B7F46;color:#fff}
.chip svg{width:22px;height:22px}
.r{position:absolute;right:0;top:0;width:560px;height:630px}
.mark{position:absolute;left:36px;top:70px;width:500px}
.toy{position:absolute;left:78px;top:232px;width:420px;filter:drop-shadow(0 22px 22px rgba(27,42,74,.22))}
.pc{position:absolute;display:block}
.kb{--pf:#2F6FCB;--pd:#1F56A8}.kp{--pf:#F28BB0;--pd:#D7678F}.ky{--pf:#FFC83D;--pd:#E0A21C}.kn{--pf:#1B2A4A;--pd:#0C1730}
</style></head><body>
<svg width="0" height="0" style="position:absolute">
 <symbol id="p-block" viewBox="0 0 100 106"><rect x="2" y="8" width="96" height="96" rx="26" style="fill:var(--pd)"/><rect x="2" y="2" width="96" height="96" rx="26" style="fill:var(--pf)"/></symbol>
 <symbol id="p-arch" viewBox="-5 -5 110 96"><path transform="translate(0 6)" d="M0 80V50a50 50 0 0 1 100 0v30H70V50a20 20 0 0 0-40 0v30z" style="fill:var(--pd);stroke:var(--pd);stroke-width:8;stroke-linejoin:round"/><path d="M0 80V50a50 50 0 0 1 100 0v30H70V50a20 20 0 0 0-40 0v30z" style="fill:var(--pf);stroke:var(--pf);stroke-width:8;stroke-linejoin:round"/></symbol>
 <symbol id="p-lens" viewBox="0 0 58 106"><path transform="translate(0 6)" d="M29 0a57.7 57.7 0 0 1 0 100A57.7 57.7 0 0 1 29 0z" style="fill:var(--pd)"/><path d="M29 0a57.7 57.7 0 0 1 0 100A57.7 57.7 0 0 1 29 0z" style="fill:var(--pf)"/></symbol>
 <symbol id="p-pill" viewBox="0 0 130 56"><rect x="2" y="8" width="126" height="46" rx="23" style="fill:var(--pd)"/><rect x="2" y="2" width="126" height="46" rx="23" style="fill:var(--pf)"/></symbol>
</svg>
<div class="l">
 <div class="wm"><span>L<svg viewBox="8 22 84 56"><circle cx="36" cy="50" r="28" fill="#2F6FCB"/><circle cx="64" cy="50" r="28" fill="#F28BB0"/><path d="M50 25.75A28 28 0 0 1 50 74.25A28 28 0 0 1 50 25.75Z" fill="#1B2A4A"/></svg>ping</span><span class="sub">BRINQUEDOS</span></div>
 <h1>Aluguel de <em>brinquedos</em> para festas</h1>
 <p>Pula-pula, cama elástica, piscina de bolinhas e muito mais.</p>
</div>
<div class="chips">
 <span class="chip c1"><svg viewBox="0 0 24 24" fill="#F28BB0"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>Praia Grande/SP</span>
 <span class="chip c2"><svg viewBox="0 0 24 24" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.2 14c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.4.6c-.1.1-.3.3-.1.6.7 1.1 1.5 1.8 2.6 2.4.3.1.5.1.6-.1l.8-1c.2-.2.4-.2.6-.1l1.9.9c.3.1.4.2.5.3.1.3.1.8-.1 1.4z"/></svg>Orçamento pelo WhatsApp</span>
</div>
<div class="r">
 <svg class="mark" viewBox="8 22 84 56"><circle cx="36" cy="50" r="28" fill="#2F6FCB"/><circle cx="64" cy="50" r="28" fill="#F28BB0"/><path d="M50 25.75A28 28 0 0 1 50 74.25A28 28 0 0 1 50 25.75Z" fill="#FFF8EE"/></svg>
 <div class="toy" id="toy"></div>
 <svg class="pc ky" viewBox="-5 -5 110 96" style="left:150px;top:510px;width:96px;transform:rotate(-8deg)"><use href="#p-arch"/></svg>
 <svg class="pc kp" viewBox="0 0 130 56" style="right:22px;top:40px;width:120px;transform:rotate(16deg)"><use href="#p-pill"/></svg>
 <svg class="pc kn" viewBox="0 0 58 106" style="left:40px;top:44px;width:38px;transform:rotate(-20deg)"><use href="#p-lens"/></svg>
 <svg class="pc kb" viewBox="0 0 100 106" style="right:26px;top:430px;width:76px;transform:rotate(12deg)"><use href="#p-block"/></svg>
</div>
<script>
""" + consts + sh + hl + """
document.getElementById("toy").innerHTML='<svg viewBox="0 0 240 160">'+""" + castle + """+'</svg>';
</script>
</body></html>"""

out_html = ROOT / "assets-src" / "og-image.html"
out_html.write_text(HTML, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    pg.goto(out_html.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(500)
    pg.screenshot(path=str(ROOT / "og-image.png"))
    b.close()
print("ok", (ROOT / "og-image.png").stat().st_size, "bytes")
