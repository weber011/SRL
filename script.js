document.addEventListener('DOMContentLoaded', () => {

    // ===== NAVBAR SCROLL =====
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // ===== MOBILE MENU =====
    const hamburger = document.getElementById('hamburger');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const drawerLinks = mobileDrawer.querySelectorAll('a');
    let menuOpen = false;

    function toggleMenu() {
        menuOpen = !menuOpen;
        if (menuOpen) {
            mobileDrawer.classList.add('open');
            hamburger.innerHTML = '<span></span><span></span>';
        } else {
            mobileDrawer.classList.remove('open');
            hamburger.innerHTML = '<span></span><span></span><span></span>';
        }
    }

    hamburger.addEventListener('click', toggleMenu);
    drawerLinks.forEach(link => {
        link.addEventListener('click', () => { if (menuOpen) toggleMenu(); });
    });

    // ===== SCROLL ANIMATIONS (IntersectionObserver) =====
    const animatedEls = document.querySelectorAll('.fade-up, .fade-left, .fade-right');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: unobserve after animating
                // observer.unobserve(entry.target);
            }
        });
    }, { root: null, rootMargin: '0px', threshold: 0.1 });

    animatedEls.forEach(el => observer.observe(el));

    // Trigger on load for elements already in view
    setTimeout(() => {
        animatedEls.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight) el.classList.add('visible');
        });
    }, 150);


    // ===== COLLECTION FILTERING =====
    const tabs = document.querySelectorAll('.cat-tab');
    const products = document.querySelectorAll('.product-card');

    // Show all initially
    products.forEach(p => p.classList.add('show'));

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Add active to clicked tab
            tab.classList.add('active');

            const filter = tab.getAttribute('data-cat');

            products.forEach(product => {
                if (filter === 'all' || product.getAttribute('data-cat').includes(filter)) {
                    product.classList.add('show');
                } else {
                    product.classList.remove('show');
                }
            });
        });
    });

});

// ===== ENQUIRY FORM =====
function sendEnquiry(e) {
    e.preventDefault();
    const name = document.getElementById('eq-name').value;
    const phone = document.getElementById('eq-phone').value;
    const city = document.getElementById('eq-city').value;
    const product = document.getElementById('eq-product').value;
    const msg = document.getElementById('eq-msg').value;

    let text = `Hi SRL Bandhel Jewellery! I'd like to place a B2B enquiry.\n\n`;
    text += `*Name:* ${name}\n`;
    text += `*Phone:* ${phone}\n`;
    text += `*City/State:* ${city}\n`;
    if (product) text += `*Product Interest:* ${product}\n`;
    text += `*Message/Quantity:* ${msg}\n`;

    const encoded = encodeURIComponent(text);
    window.open(`https://wa.me/916239005605?text=${encoded}`, '_blank');
}
