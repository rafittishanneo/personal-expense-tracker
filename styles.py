import streamlit as st


def inject_custom_css():
    st.markdown(
        """
        <style>

        /* =====================================================
           THEME VARIABLES

           Two full palettes, switched purely by the presence of
           [data-theme="light"] on <html>. Nothing here touches
           Streamlit's own server-side theme (.streamlit/config.toml)
           — that stays fixed at server start, which is why native
           widgets (buttons, selects, sidebar radio) keep their dark
           styling even in light mode. Every custom surface below
           (cards, headers, chart accents via var()) fully switches.
        ===================================================== */

        html {
            --bg-app: #06070C;
            --bg-app-2: #0B0D17;
            --bg-card: #10121D;
            --bg-input: #0B0D17;
            --border: #1E2130;
            --border-soft: rgba(255, 255, 255, 0.06);
            --text-primary: #EDEEF5;
            --text-secondary: #9297AC;
            --text-muted: #666B80;
            --accent: #7C6CFF;
            --accent-2: #22D3EE;
            --accent-soft: rgba(124, 108, 255, 0.14);
            --success: #34D399;
            --danger: #FB7185;
            --warning: #FBBF24;
            --shadow-lg: rgba(0, 0, 0, 0.55);
            --shadow-sm: rgba(0, 0, 0, 0.30);
            --glow: rgba(124, 108, 255, 0.35);
            --gradient-brand: linear-gradient(135deg, #7C6CFF 0%, #22D3EE 100%);
        }

        html[data-theme="light"] {
            --bg-app: #F3F4FC;
            --bg-app-2: #E9EAFA;
            --bg-card: #FFFFFF;
            --bg-input: #F8F8FF;
            --border: #E1E2F0;
            --border-soft: rgba(30, 30, 60, 0.06);
            --text-primary: #14162B;
            --text-secondary: #565A75;
            --text-muted: #8A8DA3;
            --accent: #6247F5;
            --accent-2: #0EA5B7;
            --accent-soft: rgba(98, 71, 245, 0.10);
            --success: #059669;
            --danger: #DC2626;
            --warning: #D97706;
            --shadow-lg: rgba(80, 70, 180, 0.14);
            --shadow-sm: rgba(80, 70, 180, 0.08);
            --glow: rgba(98, 71, 245, 0.18);
            --gradient-brand: linear-gradient(135deg, #6247F5 0%, #0EA5B7 100%);
        }

        /* =====================================================
           GLOBAL
        ===================================================== */

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont,
                         'Segoe UI', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 15% -10%, var(--accent-soft) 0%, transparent 40%),
                radial-gradient(circle at 100% 10%, var(--bg-app-2) 0%, transparent 45%),
                var(--bg-app) !important;
            transition: background 0.25s ease;
        }

        .block-container {
            padding-top: 2.2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }

        /* =====================================================
           TEXT — force every native text element to follow the
           active palette, since Streamlit's own theme otherwise
           locks these to the server-side dark values.
        ===================================================== */

        p, span, label, li,
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li {
            color: var(--text-primary);
        }

        [data-testid="stCaptionContainer"] {
            color: var(--text-muted) !important;
        }

        h1 {
            font-weight: 800 !important;
            letter-spacing: -0.03em;
            background: var(--gradient-brand);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2, h3 {
            font-weight: 700 !important;
            letter-spacing: -0.02em;
            color: var(--text-primary) !important;
        }

        /* =====================================================
           SIDEBAR
        ===================================================== */

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, var(--bg-card) 0%, var(--bg-app) 100%) !important;
            border-right: 1px solid var(--border);
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            background: transparent;
            border-radius: 12px;
            padding: 0.6rem 1rem;
            margin-bottom: 0.2rem;
            width: 100%;
            transition: background 0.18s ease;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: var(--accent-soft);
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
            background: var(--gradient-brand);
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }

        /* =====================================================
           THEME TOGGLE
           A clickable pill driven by inline JS + localStorage.
           No st.rerun, no session_state — instant visual flip,
           no server round-trip.
        ===================================================== */

        .theme-toggle-track {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 0.5rem 0.9rem;
            cursor: pointer;
            margin-bottom: 1rem;
            transition: border-color 0.18s ease, box-shadow 0.18s ease;
            user-select: none;
        }

        .theme-toggle-track:hover {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px var(--accent-soft);
        }

        .theme-toggle-icon { font-size: 1rem; line-height: 1; }

        .theme-toggle-label {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-secondary);
        }

        /* =====================================================
           CARD SURFACES
        ===================================================== */

        .app-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 1.5rem 1.6rem;
            margin-bottom: 1rem;
            box-shadow: 0 10px 30px var(--shadow-sm);
            position: relative;
            overflow: hidden;
            transition: box-shadow 0.2s ease, border-color 0.2s ease, background 0.25s ease;
        }

        .app-card::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: var(--gradient-brand);
            opacity: 0.85;
        }

        .app-card-tight {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.1rem 1.3rem;
            margin-bottom: 0.75rem;
            transition: transform 0.15s ease, border-color 0.15s ease,
                        box-shadow 0.15s ease, background 0.25s ease;
        }

        .app-card-tight:hover {
            transform: translateX(4px);
            border-color: var(--accent);
            box-shadow: 0 8px 24px var(--shadow-sm);
        }

        /* =====================================================
           METRIC CARDS
        ===================================================== */

        div[data-testid="stMetric"] {
            background: var(--bg-card) !important;
            border: 1px solid var(--border) !important;
            border-radius: 20px;
            padding: 1.3rem 1.5rem 1.2rem 1.5rem;
            box-shadow: 0 10px 28px var(--shadow-sm);
            transition: transform 0.2s ease, box-shadow 0.2s ease,
                        border-color 0.2s ease, background 0.25s ease;
        }

        div[data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            box-shadow: 0 18px 40px var(--shadow-lg);
            border-color: var(--accent);
        }

        div[data-testid="stMetricLabel"] {
            font-weight: 600;
            color: var(--text-secondary) !important;
        }

        div[data-testid="stMetricValue"] {
            font-weight: 800 !important;
            letter-spacing: -0.02em;
            color: var(--text-primary) !important;
        }

        /* =====================================================
           BUTTONS
        ===================================================== */

        .stButton > button {
            border-radius: 12px !important;
            font-weight: 600 !important;
            border: 1px solid var(--border) !important;
            background: var(--bg-card) !important;
            color: var(--text-primary) !important;
            transition: transform 0.15s ease, border-color 0.15s ease,
                        color 0.15s ease;
        }

        .stButton > button:hover {
            border-color: var(--accent) !important;
            color: var(--accent) !important;
            transform: translateY(-1px);
        }

        .stFormSubmitButton > button {
            background: var(--gradient-brand) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            box-shadow: 0 8px 24px var(--glow);
            transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease;
        }

        .stFormSubmitButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 32px var(--glow);
            filter: brightness(1.06);
        }

        /* =====================================================
           INPUTS
        ===================================================== */

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        .stNumberInput > div > div,
        .stDateInput > div > div {
            background: var(--bg-input) !important;
            border-radius: 12px !important;
            border: 1px solid var(--border) !important;
        }

        /* dropdown / date popovers rendered in a floating layer */
        ul[data-baseweb="menu"], div[data-baseweb="popover"] {
            background: var(--bg-card) !important;
            border: 1px solid var(--border) !important;
            border-radius: 12px !important;
        }

        li[role="option"] { color: var(--text-primary) !important; }

        /* =====================================================
           STATUS PILLS
        ===================================================== */

        div[data-testid="stAlertContentSuccess"],
        div[data-testid="stAlertContentError"],
        div[data-testid="stAlertContentWarning"],
        div[data-testid="stAlertContentInfo"] {
            border-radius: 12px !important;
            font-weight: 600 !important;
        }

        /* =====================================================
           DIVIDERS
        ===================================================== */

        hr { border-color: var(--border) !important; margin: 1.6rem 0 !important; }

        /* =====================================================
           PROGRESS BAR
        ===================================================== */

        div[data-testid="stProgress"] > div > div {
            background-color: var(--border) !important;
            border-radius: 10px !important;
            height: 10px !important;
        }

        div[data-testid="stProgress"] > div > div > div {
            background: var(--gradient-brand) !important;
            border-radius: 10px !important;
        }

        /* =====================================================
           DATAFRAME
        ===================================================== */

        [data-testid="stDataFrame"] {
            border-radius: 14px !important;
            overflow: hidden;
            border: 1px solid var(--border) !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


def render_theme_toggle():
    """
    Renders a clickable pill that flips html[data-theme] on the
    PARENT page between 'dark' and 'light'.

    Why st.iframe and not st.sidebar.markdown:
    st.markdown(..., unsafe_allow_html=True) is parsed by
    react-markdown + rehype-raw and converted into a React element
    tree. React never executes <script> tags inserted this way, and
    it never wires up string-valued inline event attributes like
    onclick="..." as real event listeners (those are only honored
    when the browser parses raw HTML directly, e.g. via innerHTML —
    not when React builds elements from a virtual DOM). So a toggle
    built with st.markdown renders correctly but is permanently
    inert: nothing happens on click, and any restore-on-load logic
    in an accompanying <script> tag never runs either.

    st.iframe embeds raw HTML in a real sandboxed iframe where
    <script> tags DO execute normally, same as a plain webpage.
    Because the iframe is same-origin with the Streamlit app,
    window.parent.document and window.parent.localStorage are both
    reachable, which is how this script sets data-theme on the
    actual app page (not the iframe's own separate document) and
    reads/writes the same localStorage the whole app shares.

    No st.rerun, no session_state — the flip is instant and never
    touches the server. Theme choice is restored from
    window.parent.localStorage every time this iframe is (re)created,
    which happens on every Streamlit rerun, so the choice survives
    form submissions and page interactions without flashing back
    to the default.
    """
    with st.sidebar:
        st.iframe(
            """
            <!DOCTYPE html>
            <html>
            <head>
            <style>
                body {
                    margin: 0;
                    font-family: -apple-system, BlinkMacSystemFont,
                                 'Segoe UI', sans-serif;
                }
                .theme-toggle-track {
                    display: flex;
                    align-items: center;
                    gap: 0.6rem;
                    background: #10121D;
                    border: 1px solid #1E2130;
                    border-radius: 999px;
                    padding: 0.5rem 0.9rem;
                    cursor: pointer;
                    user-select: none;
                    transition: border-color 0.18s ease, box-shadow 0.18s ease;
                    width: fit-content;
                }
                .theme-toggle-track:hover {
                    border-color: #7C6CFF;
                    box-shadow: 0 0 0 3px rgba(124, 108, 255, 0.14);
                }
                .theme-toggle-icon { font-size: 1rem; line-height: 1; }
                .theme-toggle-label {
                    font-size: 0.85rem;
                    font-weight: 600;
                    color: #9297AC;
                }
            </style>
            </head>
            <body>
                <div class="theme-toggle-track" id="toggle-pill">
                    <span class="theme-toggle-icon" id="theme-toggle-icon">🌙</span>
                    <span class="theme-toggle-label" id="theme-toggle-label">Dark mode</span>
                </div>

                <script>
                    var STORAGE_KEY = 'expense-tracker-theme';

                    function applyTheme(theme) {
                        // set the attribute on the PARENT page's <html>,
                        // where inject_custom_css()'s CSS variables live —
                        // not this iframe's own throwaway <html>
                        window.parent.document.documentElement.setAttribute(
                            'data-theme', theme
                        );

                        var icon = document.getElementById('theme-toggle-icon');
                        var label = document.getElementById('theme-toggle-label');
                        icon.textContent = theme === 'dark' ? '🌙' : '☀️';
                        label.textContent = theme === 'dark' ? 'Dark mode' : 'Light mode';
                    }

                    // restore saved choice from the PARENT's localStorage
                    // every time this iframe loads (i.e. every rerun)
                    var saved = window.parent.localStorage.getItem(STORAGE_KEY) || 'dark';
                    applyTheme(saved);

                    document.getElementById('toggle-pill').addEventListener(
                        'click',
                        function () {
                            var current = window.parent.document.documentElement
                                .getAttribute('data-theme') || 'dark';
                            var next = current === 'dark' ? 'light' : 'dark';
                            window.parent.localStorage.setItem(STORAGE_KEY, next);
                            applyTheme(next);
                        }
                    );
                </script>
            </body>
            </html>
            """,
            height=52,
        )
