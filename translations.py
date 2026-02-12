SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "हिन्दी",
    "kn": "ಕನ್ನಡ",
}

DEFAULT_LANGUAGE = "en"

TRANSLATIONS = {
    "en": {
        # Common / Navbar
        "app_name": "Expense Tracker",
        "menu": "Menu",
        "nav_dashboard": "Dashboard",
        "nav_journal": "Journal",
        "nav_logout": "Logout",
        "nav_login": "Login",
        "nav_register": "Register",

        # Dashboard
        "dashboard_title": "Dashboard",
        "weekly_summary": "Weekly Summary (Last 7 Days)",
        "monthly_summary": "Monthly Summary (Last 6 Months)",
        "add_journal_entry": "Add Journal Entry",
        "chart_income": "Income",
        "chart_expenses": "Expenses",
        "chart_withdrawals": "Withdrawals",
        "chart_net_income": "Net Income",

        # Journal
        "journal_title": "Journal Entry",
        "existing_entry_for": "Existing entry found for {date}:",
        "income_label": "Income",
        "expenses_label": "Expenses",
        "withdrawals_label": "Withdrawals",
        "notes_label": "Notes",
        "date_label": "Date",
        "entry_exists_banner": "An entry already exists for this date. Submitting will prompt you to confirm the update.",
        "optional_notes": "Optional notes...",
        "confirm_update": "Confirm Update",
        "save_entry": "Save Entry",

        # Login
        "login_title": "Log In",
        "your_username": "Your username",
        "your_password": "Your password",
        "login_button": "Log In",
        "no_account": "Don't have an account?",
        "register_link": "Register",

        # Register
        "create_account": "Create Account",
        "choose_username": "Choose a username",
        "min_chars": "Min. 6 characters",
        "reenter_password": "Re-enter password",
        "register_button": "Register",
        "have_account": "Already have an account?",
        "login_link": "Log in",

        # Form labels
        "form_username": "Username",
        "form_password": "Password",
        "form_confirm_password": "Confirm Password",

        # Validation
        "username_taken": "Username already taken.",

        # Flash messages
        "flash_register_success": "Registration successful. Please log in.",
        "flash_invalid_credentials": "Invalid username or password.",
        "flash_logged_out": "You have been logged out.",
        "flash_entry_updated": "Entry for {date} updated successfully.",
        "flash_entry_exists": "An entry already exists for {date}. Review the existing values below and confirm to update.",
        "flash_entry_saved": "Entry for {date} saved successfully.",
        "flash_login_required": "Please log in to access this page.",

        # Page titles
        "title_dashboard": "Dashboard - Expense Tracker",
        "title_journal": "Journal Entry - Expense Tracker",
        "title_login": "Login - Expense Tracker",
        "title_register": "Register - Expense Tracker",
    },
    "hi": {
        # Common / Navbar
        "app_name": "व्यय ट्रैकर",
        "menu": "मेनू",
        "nav_dashboard": "डैशबोर्ड",
        "nav_journal": "जर्नल",
        "nav_logout": "लॉग आउट",
        "nav_login": "लॉग इन",
        "nav_register": "पंजीकरण",

        # Dashboard
        "dashboard_title": "डैशबोर्ड",
        "weekly_summary": "साप्ताहिक सारांश (पिछले 7 दिन)",
        "monthly_summary": "मासिक सारांश (पिछले 6 महीने)",
        "add_journal_entry": "जर्नल प्रविष्टि जोड़ें",
        "chart_income": "आय",
        "chart_expenses": "व्यय",
        "chart_withdrawals": "निकासी",
        "chart_net_income": "शुद्ध आय",

        # Journal
        "journal_title": "जर्नल प्रविष्टि",
        "existing_entry_for": "{date} के लिए मौजूदा प्रविष्टि:",
        "income_label": "आय",
        "expenses_label": "व्यय",
        "withdrawals_label": "निकासी",
        "notes_label": "टिप्पणियाँ",
        "date_label": "तारीख",
        "entry_exists_banner": "इस तारीख के लिए एक प्रविष्टि पहले से मौजूद है। सबमिट करने पर अपडेट की पुष्टि करनी होगी।",
        "optional_notes": "वैकल्पिक टिप्पणियाँ...",
        "confirm_update": "अपडेट की पुष्टि करें",
        "save_entry": "प्रविष्टि सहेजें",

        # Login
        "login_title": "लॉग इन",
        "your_username": "आपका उपयोगकर्ता नाम",
        "your_password": "आपका पासवर्ड",
        "login_button": "लॉग इन",
        "no_account": "खाता नहीं है?",
        "register_link": "पंजीकरण करें",

        # Register
        "create_account": "खाता बनाएँ",
        "choose_username": "उपयोगकर्ता नाम चुनें",
        "min_chars": "न्यूनतम 6 अक्षर",
        "reenter_password": "पासवर्ड दोबारा दर्ज करें",
        "register_button": "पंजीकरण करें",
        "have_account": "पहले से खाता है?",
        "login_link": "लॉग इन करें",

        # Form labels
        "form_username": "उपयोगकर्ता नाम",
        "form_password": "पासवर्ड",
        "form_confirm_password": "पासवर्ड की पुष्टि करें",

        # Validation
        "username_taken": "उपयोगकर्ता नाम पहले से लिया गया है।",

        # Flash messages
        "flash_register_success": "पंजीकरण सफल। कृपया लॉग इन करें।",
        "flash_invalid_credentials": "अमान्य उपयोगकर्ता नाम या पासवर्ड।",
        "flash_logged_out": "आप लॉग आउट हो गए हैं।",
        "flash_entry_updated": "{date} की प्रविष्टि सफलतापूर्वक अपडेट की गई।",
        "flash_entry_exists": "{date} के लिए एक प्रविष्टि पहले से मौजूद है। नीचे मौजूदा मान देखें और अपडेट की पुष्टि करें।",
        "flash_entry_saved": "{date} की प्रविष्टि सफलतापूर्वक सहेजी गई।",
        "flash_login_required": "कृपया इस पृष्ठ तक पहुँचने के लिए लॉग इन करें।",

        # Page titles
        "title_dashboard": "डैशबोर्ड - व्यय ट्रैकर",
        "title_journal": "जर्नल प्रविष्टि - व्यय ट्रैकर",
        "title_login": "लॉग इन - व्यय ट्रैकर",
        "title_register": "पंजीकरण - व्यय ट्रैकर",
    },
    "kn": {
        # Common / Navbar
        "app_name": "ವೆಚ್ಚ ಟ್ರ್ಯಾಕರ್",
        "menu": "ಮೆನು",
        "nav_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "nav_journal": "ಜರ್ನಲ್",
        "nav_logout": "ಲಾಗ್ ಔಟ್",
        "nav_login": "ಲಾಗ್ ಇನ್",
        "nav_register": "ನೋಂದಣಿ",

        # Dashboard
        "dashboard_title": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "weekly_summary": "ಸಾಪ್ತಾಹಿಕ ಸಾರಾಂಶ (ಕಳೆದ 7 ದಿನಗಳು)",
        "monthly_summary": "ಮಾಸಿಕ ಸಾರಾಂಶ (ಕಳೆದ 6 ತಿಂಗಳುಗಳು)",
        "add_journal_entry": "ಜರ್ನಲ್ ನಮೂದು ಸೇರಿಸಿ",
        "chart_income": "ಆದಾಯ",
        "chart_expenses": "ವೆಚ್ಚಗಳು",
        "chart_withdrawals": "ಹಿಂಪಡೆಯುವಿಕೆಗಳು",
        "chart_net_income": "ನಿವ್ವಳ ಆದಾಯ",

        # Journal
        "journal_title": "ಜರ್ನಲ್ ನಮೂದು",
        "existing_entry_for": "{date} ಗೆ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ನಮೂದು:",
        "income_label": "ಆದಾಯ",
        "expenses_label": "ವೆಚ್ಚಗಳು",
        "withdrawals_label": "ಹಿಂಪಡೆಯುವಿಕೆಗಳು",
        "notes_label": "ಟಿಪ್ಪಣಿಗಳು",
        "date_label": "ದಿನಾಂಕ",
        "entry_exists_banner": "ಈ ದಿನಾಂಕಕ್ಕೆ ಈಗಾಗಲೇ ನಮೂದು ಅಸ್ತಿತ್ವದಲ್ಲಿದೆ. ಸಲ್ಲಿಸಿದರೆ ನವೀಕರಣವನ್ನು ಖಚಿತಪಡಿಸಲು ಕೇಳಲಾಗುತ್ತದೆ.",
        "optional_notes": "ಐಚ್ಛಿಕ ಟಿಪ್ಪಣಿಗಳು...",
        "confirm_update": "ನವೀಕರಣ ಖಚಿತಪಡಿಸಿ",
        "save_entry": "ನಮೂದು ಉಳಿಸಿ",

        # Login
        "login_title": "ಲಾಗ್ ಇನ್",
        "your_username": "ನಿಮ್ಮ ಬಳಕೆದಾರ ಹೆಸರು",
        "your_password": "ನಿಮ್ಮ ಪಾಸ್‌ವರ್ಡ್",
        "login_button": "ಲಾಗ್ ಇನ್",
        "no_account": "ಖಾತೆ ಇಲ್ಲವೇ?",
        "register_link": "ನೋಂದಣಿ",

        # Register
        "create_account": "ಖಾತೆ ರಚಿಸಿ",
        "choose_username": "ಬಳಕೆದಾರ ಹೆಸರು ಆಯ್ಕೆಮಾಡಿ",
        "min_chars": "ಕನಿಷ್ಠ 6 ಅಕ್ಷರಗಳು",
        "reenter_password": "ಪಾಸ್‌ವರ್ಡ್ ಮರು-ನಮೂದಿಸಿ",
        "register_button": "ನೋಂದಣಿ",
        "have_account": "ಈಗಾಗಲೇ ಖಾತೆ ಇದೆಯೇ?",
        "login_link": "ಲಾಗ್ ಇನ್",

        # Form labels
        "form_username": "ಬಳಕೆದಾರ ಹೆಸರು",
        "form_password": "ಪಾಸ್‌ವರ್ಡ್",
        "form_confirm_password": "ಪಾಸ್‌ವರ್ಡ್ ಖಚಿತಪಡಿಸಿ",

        # Validation
        "username_taken": "ಬಳಕೆದಾರ ಹೆಸರು ಈಗಾಗಲೇ ತೆಗೆದುಕೊಳ್ಳಲಾಗಿದೆ.",

        # Flash messages
        "flash_register_success": "ನೋಂದಣಿ ಯಶಸ್ವಿ. ದಯವಿಟ್ಟು ಲಾಗ್ ಇನ್ ಮಾಡಿ.",
        "flash_invalid_credentials": "ಅಮಾನ್ಯ ಬಳಕೆದಾರ ಹೆಸರು ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್.",
        "flash_logged_out": "ನೀವು ಲಾಗ್ ಔಟ್ ಆಗಿದ್ದೀರಿ.",
        "flash_entry_updated": "{date} ನಮೂದು ಯಶಸ್ವಿಯಾಗಿ ನವೀಕರಿಸಲಾಗಿದೆ.",
        "flash_entry_exists": "{date} ಗೆ ಈಗಾಗಲೇ ನಮೂದು ಅಸ್ತಿತ್ವದಲ್ಲಿದೆ. ಕೆಳಗಿನ ಮೌಲ್ಯಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನವೀಕರಿಸಲು ಖಚಿತಪಡಿಸಿ.",
        "flash_entry_saved": "{date} ನಮೂದು ಯಶಸ್ವಿಯಾಗಿ ಉಳಿಸಲಾಗಿದೆ.",
        "flash_login_required": "ದಯವಿಟ್ಟು ಈ ಪುಟವನ್ನು ಪ್ರವೇಶಿಸಲು ಲಾಗ್ ಇನ್ ಮಾಡಿ.",

        # Page titles
        "title_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ - ವೆಚ್ಚ ಟ್ರ್ಯಾಕರ್",
        "title_journal": "ಜರ್ನಲ್ ನಮೂದು - ವೆಚ್ಚ ಟ್ರ್ಯಾಕರ್",
        "title_login": "ಲಾಗ್ ಇನ್ - ವೆಚ್ಚ ಟ್ರ್ಯಾಕರ್",
        "title_register": "ನೋಂದಣಿ - ವೆಚ್ಚ ಟ್ರ್ಯಾಕರ್",
    },
}
