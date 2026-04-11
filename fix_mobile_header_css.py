import glob

css_block = """
        /* Responsive Navigation for Mobile */
        @media (max-width: 640px) {
            .pill-nav {
                width: 98vw !important;
                padding: 0.1rem !important;
                justify-content: center !important;
                gap: 2px !important;
            }

            .nav-link {
                padding: 0.5rem 0.35rem !important;
                font-size: 0.65rem !important;
                letter-spacing: -0.02em !important;
                white-space: nowrap !important;
            }
        }
"""

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # if header css isn't there, we inject it just before the first </style>
    if "98vw !important" not in content and "<style>" in content:
        new_content = content.replace("</style>", css_block + "</style>", 1)
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Injected header CSS into {file}")
