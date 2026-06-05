import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update HTML in topLeftCluster
cluster_old = r"""<div id="topLeftCluster">
  <button id="linksBtn">&#9776; LINKS <span class="arrow">&#9660;</span></button>"""
cluster_new = """<div id="topLeftCluster">
  <div style="display: flex; gap: 5px;">
    <button id="linksBtn">&#9776; LINKS <span class="arrow">&#9660;</span></button>
    <button id="infoBtn">&#8505; WHAT IS VOI?</button>
  </div>"""
text = re.sub(cluster_old, cluster_new, text)

# 2. Add Info Modal HTML
modal_html = """
<!-- VOI INFO MODAL -->
<div class="q-overlay" id="infoOverlay">
  <div class="q-modal" style="max-width: 500px; text-align: left; padding: 24px;">
    <h2 style="color: var(--accent); margin-top: 0; font-family: 'Orbitron', sans-serif;">WHAT IS VOI NETWORK?</h2>
    <p style="font-family: 'Inter', sans-serif; font-size: 14px; color: var(--text); line-height: 1.6;">
      <strong>Voi Network</strong> is a user-centric, Layer-1 blockchain built for mass adoption. It focuses on empowering communities rather than just extracting value.
    </p>
    <p style="font-family: 'Inter', sans-serif; font-size: 14px; color: var(--text); line-height: 1.6;">
      Unlike traditional blockchains where early investors hold all the power, Voi allocates a massive portion of its tokenomics directly to ecosystem builders, node runners, and users. It's designed to be fast, cheap, and fiercely community-owned.
    </p>
    <button class="cyber-btn" id="closeInfoBtn" style="margin-top: 20px; width: 100%;">RESUME MISSION</button>
  </div>
</div>
"""
text = re.sub(r'<!-- MOBILE QUESTION OVERLAY -->', modal_html + '\n<!-- MOBILE QUESTION OVERLAY -->', text)

# 3. Update CSS for the buttons
css_old = r"""  /\* Links dropdown button \*/
  #linksBtn \{
    background: #0a1520; border: 1px solid var\(--accent2\); color: var\(--accent2\);
    padding: 6px 12px; font-family: 'Share Tech Mono', monospace; font-size: 11px;
    cursor: pointer; transition: all 0\.2s;
    display: flex; align-items: center; gap: 6px;
    -webkit-tap-highlight-color: transparent; letter-spacing: 0\.1em;
    white-space: nowrap; user-select: none;
  \}
  #linksBtn:hover \{ border-color: var\(--accent\); color: var\(--accent\); box-shadow: var\(--glow\); \}"""

css_new = """  /* Top Left Buttons */
  #linksBtn, #infoBtn, #muteBtn, #musicBtn {
    background: rgba(10, 21, 32, 0.6); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(0, 245, 255, 0.3); color: var(--accent2);
    padding: 8px 14px; font-family: 'Share Tech Mono', monospace; font-size: 11px;
    cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex; align-items: center; justify-content: center; gap: 6px;
    -webkit-tap-highlight-color: transparent; letter-spacing: 0.1em;
    white-space: nowrap; user-select: none; border-radius: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  }
  #linksBtn:hover, #infoBtn:hover, #muteBtn:hover, #musicBtn:hover { 
    border-color: var(--accent); color: var(--accent); 
    box-shadow: 0 0 15px rgba(0, 245, 255, 0.4); 
    background: rgba(10, 21, 32, 0.9);
    transform: translateY(-1px);
  }"""

text = re.sub(css_old, css_new, text)

# 4. Remove the old #muteBtn / #musicBtn CSS that overrides this
css_old_2 = r"""  #muteBtn, #musicBtn \{
    background: #0a1520; border: 1px solid var\(--dim\); color: var\(--dim\);
    padding: 5px 9px; font-family: 'Share Tech Mono', monospace; font-size: 10px;
    cursor: pointer; transition: all 0\.2s;
    -webkit-tap-highlight-color: transparent; letter-spacing: 0\.05em;
    white-space: nowrap;
  \}
  #muteBtn:hover, #musicBtn:hover \{ border-color: var\(--accent2\); color: var\(--accent2\); box-shadow: 0 0 8px var\(--accent2\); \}"""

text = re.sub(css_old_2, "", text)

# 5. Add JavaScript Logic for Info Button
js_logic = """
  // INFO MODAL LOGIC
  document.getElementById('infoBtn').addEventListener('click', () => {
    // Pause game
    if (state.screen === 'game') {
      if (state.animFrame) cancelAnimationFrame(state.animFrame);
      state.animFrame = null;
      if (state.timerInterval) clearInterval(state.timerInterval);
      state.timerInterval = null;
      document.getElementById('canvasWrapper').style.filter = 'blur(10px)';
    }
    document.getElementById('infoOverlay').classList.add('show');
  });

  document.getElementById('closeInfoBtn').addEventListener('click', () => {
    document.getElementById('infoOverlay').classList.remove('show');
    // Resume game
    if (state.screen === 'game') {
      document.getElementById('canvasWrapper').style.filter = 'none';
      startTimer();
      state.lastMoveTime = Date.now();
      gameLoop();
    }
  });
"""

text = re.sub(r'document\.getElementById\(\'linksBtn\'\)\.addEventListener\(\'click\'', js_logic + r"\n  document.getElementById('linksBtn').addEventListener('click'", text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated successfully")
