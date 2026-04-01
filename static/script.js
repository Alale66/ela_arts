console.log("Website loaded successfully.");

// Instant search functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, looking for search elements...');

    const searchInput = document.querySelector('.search-bar input');
    const searchContainer = document.querySelector('.search-bar');

    console.log('Search input found:', searchInput);
    console.log('Search container found:', searchContainer);

    if (searchInput && searchContainer) {
        console.log('Search elements found, setting up instant search...');

        // Available pages for search
        const pages = [
            { name: 'Portfolio', url: '/', keywords: ['portfolio', 'home', 'main', 'art', 'work'] },
            { name: 'Shop', url: '/shop', keywords: ['shop', 'store', 'buy', 'purchase', 'products'] },
            { name: 'About', url: '/about', keywords: ['about', 'artist', 'ela', 'bio', 'biography'] },
            { name: 'Contact', url: '/contact', keywords: ['contact', 'email', 'message', 'reach'] },
            { name: 'Blog', url: '/blog', keywords: ['blog', 'posts', 'news', 'articles'] },
            { name: 'Log In', url: '/log-in', keywords: ['log', 'login', 'sign', 'account', 'user'] },
            { name: 'Cart', url: '/cart', keywords: ['cart', 'basket', 'shopping', 'checkout'] }
        ];

        // Create results dropdown
        const resultsDropdown = document.createElement('div');
        resultsDropdown.className = 'search-results';
        resultsDropdown.style.cssText = `
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            max-height: 300px;
            overflow-y: auto;
            z-index: 1000;
            display: none;
        `;
        searchContainer.style.position = 'relative';
        searchContainer.appendChild(resultsDropdown);

        // Search function
        function performSearch(query) {
            console.log('Performing search for:', query);
            if (query.length < 1) {
                resultsDropdown.style.display = 'none';
                return;
            }

            const results = pages.filter(page => {
                const searchText = (page.name + ' ' + page.keywords.join(' ')).toLowerCase();
                return searchText.includes(query.toLowerCase());
            });

            console.log('Found results:', results.length);

            if (results.length > 0) {
                resultsDropdown.innerHTML = results.map(page => `
                    <a href="${page.url}" class="search-result-item" style="
                        display: block;
                        padding: 12px 16px;
                        text-decoration: none;
                        color: #333;
                        border-bottom: 1px solid #eee;
                        transition: background 0.2s;
                    " onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">
                        <strong>${page.name}</strong>
                    </a>
                `).join('');
                resultsDropdown.style.display = 'block';
            } else {
                resultsDropdown.innerHTML = `
                    <div style="padding: 12px 16px; color: #666; font-style: italic;">
                        No results found for "${query}"
                    </div>
                `;
                resultsDropdown.style.display = 'block';
            }
        }

        // Input event listener
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const query = this.value.trim();
            console.log('Input event, query:', query);
            searchTimeout = setTimeout(() => performSearch(query), 200); // Debounce
        });

        // Hide results when clicking outside
        document.addEventListener('click', function(e) {
            if (!searchContainer.contains(e.target)) {
                resultsDropdown.style.display = 'none';
            }
        });

        // Hide results on escape
        searchInput.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                resultsDropdown.style.display = 'none';
                searchInput.blur();
            }
        });

        console.log('Instant search setup complete');
    } else {
        console.error('Search elements not found!');
        console.log('Available elements with search-bar class:', document.querySelectorAll('.search-bar'));
        console.log('Available input elements:', document.querySelectorAll('input'));
    }
});
