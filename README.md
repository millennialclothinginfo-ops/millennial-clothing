# Millennial Clothing — Website

Full 35-page static website for Millennial Clothing.

## Structure

```
millennial-clothing/
├── index.html                   ← Home (Landing Page)
├── store-page.html              ← Shop / Store
├── product-page.html            ← Product Detail
├── cart-v3.html                 ← Cart
├── checkout.html                ← Checkout
│
├── login.html                   ← Login (email)
├── login-phone.html             ← Login (phone)
├── signup.html                  ← Sign Up
├── forgot-password.html         ← Forgot Password
├── otp-verification.html        ← OTP Verification
├── social-redirect.html         ← Social Auth Redirect
│
├── profile.html                 ← My Profile
├── Order_History_Page.html      ← Order History
├── wishlist.html                ← Wishlist
├── quotes.html                  ← My Quotes
├── track-order.html             ← Track Order
│
├── Corporate_Landing_Page.html  ← Corporate Landing
├── corporate_product_page.html  ← Corporate Product
├── WholeSaleLanding_Page.html   ← Wholesale Landing
├── wholesale-catalog.html       ← Wholesale Catalog
├── wholesale-product-page.html  ← Wholesale Product
├── wholesale_checkout.html      ← Wholesale Checkout
├── get-quote.html               ← Get a Quote
├── bulk-orders.html             ← Bulk Orders
│
├── about-us.html                ← About Us
├── contact-us.html              ← Contact Us
├── career.html                  ← Careers
├── faq.html                     ← FAQ
├── store-locator.html           ← Store Locator
├── privacy-policy.html          ← Privacy Policy
├── return-cancellation-policy.html ← Return Policy
├── terms-and-conditions.html    ← Terms & Conditions
├── size-care-guide.html         ← Size & Care Guide
│
├── header.html                  ← Header component (source)
├── Footer.html                  ← Footer component (source)
│
├── assets/
│   └── js/
│       └── site-nav.js          ← Shared navigation & link routing
│
└── build.py                     ← Build script (re-injects header/footer)
```

## Re-building

If you edit `header.html` or `Footer.html`, re-run the build to propagate changes to all pages:

```bash
python3 build.py
```

## Navigation

All internal links from `millennial-clothing.com/*` are automatically resolved to local `.html` files via `assets/js/site-nav.js`.

## Theme

- Font: Inter + Big Shoulders Display + IBM Plex Mono (Google Fonts)
- Colors: Light Ash `#ECECEE` canvas, Dark Black gradient `#3A3A42 → #000000`
- Currency: ৳ (BDT)
