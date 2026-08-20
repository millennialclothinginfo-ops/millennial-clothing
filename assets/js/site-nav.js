/**
 * Millennial Clothing — Site Navigation Map
 * Central routing for all 35 pages.
 */
window.MC_PAGES = {
  /* Core */
  home:                 'index.html',
  store:                'store-page.html',
  product:              'product-page.html',
  cart:                 'cart-v3.html',
  checkout:             'checkout.html',

  /* Auth */
  login:                'login.html',
  loginPhone:           'login-phone.html',
  signup:               'signup.html',
  forgotPassword:       'forgot-password.html',
  otpVerification:      'otp-verification.html',
  socialRedirect:       'social-redirect.html',

  /* Account */
  profile:              'profile.html',
  orderHistory:         'Order_History_Page.html',
  wishlist:             'wishlist.html',
  quotes:               'quotes.html',
  trackOrder:           'track-order.html',

  /* Corporate / Wholesale */
  corporate:            'Corporate_Landing_Page.html',
  corporateProduct:     'corporate_product_page.html',
  wholesale:            'WholeSaleLanding_Page.html',
  wholesaleCatalog:     'wholesale-catalog.html',
  wholesaleProduct:     'wholesale-product-page.html',
  wholesaleCheckout:    'wholesale_checkout.html',
  getQuote:             'get-quote.html',
  bulkOrders:           'bulk-orders.html',

  /* Info */
  aboutUs:              'about-us.html',
  contactUs:            'contact-us.html',
  career:               'career.html',
  faq:                  'faq.html',
  storeLocator:         'store-locator.html',
  privacyPolicy:        'privacy-policy.html',
  returnPolicy:         'return-cancellation-policy.html',
  termsConditions:      'terms-and-conditions.html',
  sizeCareGuide:        'size-care-guide.html',
};

/**
 * Replace all millennial-clothing.com external links with local page links.
 * Call after DOM ready.
 */
(function patchExternalLinks() {
  var MAP = {
    'millennial-clothing.com/contact-us':             'contact-us.html',
    'millennial-clothing.com/faq':                    'faq.html',
    'millennial-clothing.com/return-cancellation-policy': 'return-cancellation-policy.html',
    'millennial-clothing.com/privacy-policy':         'privacy-policy.html',
    'millennial-clothing.com/terms-and-conditions':   'terms-and-conditions.html',
    'millennial-clothing.com/size-care-guide':        'size-care-guide.html',
    'millennial-clothing.com/store-locator':          'store-locator.html',
    'millennial-clothing.com/about-us':               'about-us.html',
    'millennial-clothing.com/store':                  'store-page.html',
    'millennial-clothing.com/cart':                   'cart-v3.html',
    'millennial-clothing.com/profile':                'profile.html',
    'millennial-clothing.com/careers':                'career.html',
    'millennial-clothing.com/career':                 'career.html',
    'millennial-clothing.com/newsletter':             'contact-us.html',
    'millennial-clothing.com/payment-terms':          'terms-and-conditions.html',
    'millennial-clothing.com/shipping-method':        'faq.html',
    'millennial-clothing.com/':                       'index.html',
    'millennial-clothing.com':                        'index.html',
    'www.millennial-clothing.com':                    'index.html',
  };

  function resolveHref(href) {
    if (!href) return null;
    for (var key in MAP) {
      if (href.indexOf(key) !== -1) return MAP[key];
    }
    return null;
  }

  function patch() {
    var links = document.querySelectorAll('a[href]');
    links.forEach(function(a) {
      var resolved = resolveHref(a.getAttribute('href'));
      if (resolved) {
        a.setAttribute('href', resolved);
        a.removeAttribute('target');
        a.removeAttribute('rel');
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', patch);
  } else {
    patch();
  }
})();

/**
 * Patch header navigation links to local pages.
 * Also updates the profile dropdown links.
 */
(function patchHeaderLinks() {
  function patchNav() {
    // Menu drawer links (expand-menu)
    var menuLinks = document.querySelectorAll('.expand-menu a, .menu-accordion-body-inner a, .menu-subaccordion-body-inner a');
    var NAV_MAP = {
      'Home':                   'index.html',
      'Browse Shop':            'store-page.html',
      'Sportswear':             'store-page.html?collection=sportswear',
      'Riding Gear':            'store-page.html?collection=riding-gear',
      'Streetwear':             'store-page.html?collection=streetwear',
      'Formal Wear':            'store-page.html?collection=formal',
      'Men':                    'store-page.html?dept=men',
      'Women':                  'store-page.html?dept=women',
      'Unisex':                 'store-page.html?dept=unisex',
      'Kids':                   'store-page.html?dept=kids',
      'T-Shirts':               'store-page.html?cat=tshirts',
      'Shirts':                 'store-page.html?cat=shirts',
      'Trousers':               'store-page.html?cat=trousers',
      'Jackets':                'store-page.html?cat=jackets',
      'Tops':                   'store-page.html?cat=tops',
      'Dresses':                'store-page.html?cat=dresses',
      'Jeans':                  'store-page.html?cat=jeans',
      'Outerwear':              'store-page.html?cat=outerwear',
      'Sneakers':               'store-page.html?cat=sneakers',
      'Boots':                  'store-page.html?cat=boots',
      'Sandals':                'store-page.html?cat=sandals',
      'Bags':                   'store-page.html?cat=bags',
      'Belts':                  'store-page.html?cat=belts',
      'Caps':                   'store-page.html?cat=caps',
      'All Brands':             'store-page.html?filter=brands',
      'Featured Brands':        'store-page.html?filter=featured',
      'Manufacturing':          'wholesale-catalog.html',
      'Bulk Purchase':          'bulk-orders.html',
      'Contact Us':             'contact-us.html',
      'Millennial Corporate':   'Corporate_Landing_Page.html',
      'AP International':       'wholesale-catalog.html',
      'Minas Dream':            'WholeSaleLanding_Page.html',
    };
    menuLinks.forEach(function(a) {
      var text = a.textContent.trim();
      if (NAV_MAP[text]) a.setAttribute('href', NAV_MAP[text]);
    });

    // Logo home link
    var logoLink = document.querySelector('.logo-link');
    if (logoLink) logoLink.setAttribute('href', 'index.html');

    // Profile dropdown
    var profileItems = document.querySelectorAll('.profile-item');
    var PROFILE_MAP = {
      'View Profile':    'profile.html',
      'My Orders':       'Order_History_Page.html',
      'My Carts':        'cart-v3.html',
      'Wishlist':        'wishlist.html',
      'Quotes':          'quotes.html',
      'Track Order':     'track-order.html',
      'Switch Account':  'login.html?switch=1',
    };
    profileItems.forEach(function(a) {
      var text = a.textContent.trim();
      if (PROFILE_MAP[text]) a.setAttribute('href', PROFILE_MAP[text]);
    });

    // Cart checkout buttons in drawer
    document.addEventListener('click', function(e) {
      var btn = e.target.closest('.cd-btn-checkout, .cd-checkout-sel');
      if (btn) { window.location.href = 'checkout.html'; }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', patchNav);
  } else {
    patchNav();
  }
})();
