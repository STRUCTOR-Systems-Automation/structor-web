import glob

script_block = """
    <!-- iOS Video Autoplay Fallback -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const allVids = document.querySelectorAll('video');
            allVids.forEach(v => {
                v.muted = true;
                v.setAttribute('playsinline', '');
                v.play().catch(() => {});
            });
            const unlockAllVids = () => {
                allVids.forEach(v => v.play().catch(() => {}));
                document.removeEventListener('touchstart', unlockAllVids);
                document.removeEventListener('click', unlockAllVids);
            };
            document.addEventListener('touchstart', unlockAllVids, { once: true, passive: true });
            document.addEventListener('click', unlockAllVids, { once: true, passive: true });
        });
    </script>
"""

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # if bypass isn't there, we inject it just before </body>
    if "unlockAllVids" not in content and "</body>" in content:
        new_content = content.replace("</body>", script_block + "\n</body>")
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Injected iOS bypass into {file}")
