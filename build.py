"""
Millennial Clothing — Site Builder
Injects shared header + footer into every page and wires up internal navigation.
Run: python3 build.py
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = BASE  # html files are in root

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ─── Extract header CSS + body block ────────────────────────────────────────
header_src = read(os.path.join(SRC_DIR, 'header.html'))

# CSS (everything inside <style>...</style>)
header_css = re.search(r'<style>(.*?)</style>', header_src, re.S).group(1)

# Body block: from <body> up to (but not including) the demo-note
body_content = header_src[header_src.index('<body>') + 6 : header_src.index('<div class="demo-note">')]

# Cart drawer script block
cart_script_start = header_src.index('\n<script>\n/* ===== CART DRAWER LOGIC')
cart_script_end   = header_src.index('</body>')
cart_script = header_src[cart_script_start:cart_script_end].strip()

# Header JS (everything between </style> and </head>)
head_scripts_m = re.search(r'</style>(.*?)</head>', header_src, re.S)
head_scripts = head_scripts_m.group(1).strip() if head_scripts_m else ''

HEADER_INJECT = f"""<!-- ========== SHARED HEADER — auto-injected by build.py ========== -->
<style>
{header_css}
</style>
{head_scripts}
<!-- /head-scripts -->

{body_content.strip()}

{cart_script}
<!-- ========== /SHARED HEADER ========== -->"""

# ─── Extract footer block ────────────────────────────────────────────────────
footer_src = read(os.path.join(SRC_DIR, 'Footer.html'))
footer_css = re.search(r'<style>(.*?)</style>', footer_src, re.S).group(1)
footer_body = footer_src[footer_src.index('<body>') + 6 : footer_src.index('</body>')]
# Strip leading demo-note div
footer_body = re.sub(r'<div class="demo-note">.*?</div>\s*', '', footer_body, flags=re.S)

# Patch footer nav links
FOOTER_LINK_MAP = {
    'https://millennial-clothing.com/contact-us':              'contact-us.html',
    'https://millennial-clothing.com/faq':                     'faq.html',
    'https://millennial-clothing.com/return-cancellation-policy': 'return-cancellation-policy.html',
    'https://millennial-clothing.com/privacy-policy':          'privacy-policy.html',
    'https://millennial-clothing.com/terms-and-conditions':    'terms-and-conditions.html',
    'https://millennial-clothing.com/size-care-guide':         'size-care-guide.html',
    'https://millennial-clothing.com/store-locator':           'store-locator.html',
    'https://millennial-clothing.com/about-us':                'about-us.html',
    'https://millennial-clothing.com/store':                   'store-page.html',
    'https://millennial-clothing.com/cart':                    'cart-v3.html',
    'https://millennial-clothing.com/profile':                 'profile.html',
    'https://millennial-clothing.com/careers':                 'career.html',
    'https://millennial-clothing.com/career':                  'career.html',
    'https://millennial-clothing.com/newsletter':              'contact-us.html',
    'https://millennial-clothing.com/payment-terms':           'terms-and-conditions.html',
    'https://millennial-clothing.com/shipping-method':         'faq.html',
    'http://www.millennial-clothing.com':                      'index.html',
    'https://millennial-clothing.com/':                        'index.html',
    'https://www.millennial-clothing.com':                     'index.html',
    'https://millennial-clothing.com':                         'index.html',
}
for ext, local in FOOTER_LINK_MAP.items():
    footer_body = footer_body.replace(f'href="{ext}"', f'href="{local}"')
    footer_body = footer_body.replace(f"href='{ext}'", f"href='{local}'")

# Add Corporate/Wholesale links to footer brand strip
footer_body = footer_body.replace(
    'href="Corporate_Landing_Page.html"', 'href="Corporate_Landing_Page.html"'
).replace(
    'href="WholeSaleLanding_Page.html"', 'href="WholeSaleLanding_Page.html"'
)

FOOTER_INJECT = f"""<!-- ========== SHARED FOOTER — auto-injected by build.py ========== -->
<style>
{footer_css}
</style>
<div style="background:var(--canvas, #ECECEE); padding:0 0 0 0;">
{footer_body.strip()}
</div>
<!-- ========== /SHARED FOOTER ========== -->"""

# ─── Pages to process ───────────────────────────────────────────────────────
# Pages that have their own auth/minimal UI — no full header/footer
NO_HEADER_FOOTER = {
    'login.html', 'login-phone.html', 'signup.html',
    'forgot-password.html', 'otp-verification.html', 'social-redirect.html',
    'header.html', 'Footer.html',
}

# Pages that get header but no footer (auth-adjacent)
HEADER_ONLY = set()

# Internal link patch map (applied to every page)
INTERNAL_LINK_MAP = {
    'https://millennial-clothing.com/contact-us':                 'contact-us.html',
    'https://millennial-clothing.com/faq':                        'faq.html',
    'https://millennial-clothing.com/return-cancellation-policy': 'return-cancellation-policy.html',
    'https://millennial-clothing.com/privacy-policy':             'privacy-policy.html',
    'https://millennial-clothing.com/terms-and-conditions':       'terms-and-conditions.html',
    'https://millennial-clothing.com/size-care-guide':            'size-care-guide.html',
    'https://millennial-clothing.com/store-locator':              'store-locator.html',
    'https://millennial-clothing.com/about-us':                   'about-us.html',
    'https://millennial-clothing.com/store':                      'store-page.html',
    'https://millennial-clothing.com/cart':                       'cart-v3.html',
    'https://millennial-clothing.com/profile':                    'profile.html',
    'https://millennial-clothing.com/careers':                    'career.html',
    'https://millennial-clothing.com/career':                     'career.html',
    'https://millennial-clothing.com/newsletter':                 'contact-us.html',
    'https://millennial-clothing.com/payment-terms':              'terms-and-conditions.html',
    'https://millennial-clothing.com/shipping-method':            'faq.html',
    'http://www.millennial-clothing.com':                         'index.html',
    'https://millennial-clothing.com/':                           'index.html',
    'https://www.millennial-clothing.com':                        'index.html',
    'https://millennial-clothing.com':                            'index.html',
    'https://millennial-clothing.com/store?collection=3':         'store-page.html?collection=3',
}

def patch_internal_links(html):
    for ext, local in INTERNAL_LINK_MAP.items():
        html = html.replace(f'href="{ext}"', f'href="{local}"')
        html = html.replace(f"href='{ext}'", f"href='{local}'")
    return html

# site-nav.js script tag to insert
SITE_NAV_SCRIPT = '<script src="assets/js/site-nav.js"></script>'

def inject_page(filename, html):
    """Inject header, footer and nav script into a page."""
    # 1. Patch internal links
    html = patch_internal_links(html)

    # 2. Insert site-nav.js before </head>
    html = html.replace('</head>', SITE_NAV_SCRIPT + '\n</head>', 1)

    no_hf = filename in NO_HEADER_FOOTER
    header_only = filename in HEADER_ONLY

    if no_hf:
        return html

    # 3. Inject header immediately after <body>
    html = re.sub(r'<body([^>]*)>', lambda m: f'<body{m.group(1)}>\n' + HEADER_INJECT, html, count=1)

    # 4. Inject footer before </body>
    if not header_only:
        html = html.replace('</body>', '\n' + FOOTER_INJECT + '\n</body>', 1)

    return html

# ─── Process all pages ───────────────────────────────────────────────────────
html_files = [f for f in os.listdir(SRC_DIR) if f.endswith('.html')]
processed = []
for fname in sorted(html_files):
    if fname in ('header.html', 'Footer.html'):
        continue
    src_path = os.path.join(SRC_DIR, fname)
    html = read(src_path)
    html_out = inject_page(fname, html)
    write(src_path, html_out)
    processed.append(fname)
    print(f'  ✓ {fname}')

# ─── Create index.html (alias for Landing_Page.html) ─────────────────────────
landing = read(os.path.join(SRC_DIR, 'Landing_Page.html'))
write(os.path.join(SRC_DIR, 'index.html'), landing)
print(f'  ✓ index.html (copy of Landing_Page.html)')

print(f'\nDone! Processed {len(processed)} pages.')
