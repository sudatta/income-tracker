SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "हिन्दी",
    "kn": "ಕನ್ನಡ",
    "ml": "മലയാളം",
}

DEFAULT_LANGUAGE = "en"

TRANSLATIONS = {
    "en": {
        # Common / Navbar
        "app_name": "Income Tracker",
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
        "title_dashboard": "Dashboard - Income Tracker",
        "title_journal": "Journal Entry - Income Tracker",
        "title_login": "Login - Income Tracker",
        "title_register": "Register - Income Tracker",
    },
    "hi": {
        # Common / Navbar
        "app_name": "आय ट्रैकर",
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
        "title_dashboard": "डैशबोर्ड - आय ट्रैकर",
        "title_journal": "जर्नल प्रविष्टि - आय ट्रैकर",
        "title_login": "लॉग इन - आय ट्रैकर",
        "title_register": "पंजीकरण - आय ट्रैकर",
    },
    "kn": {
        # Common / Navbar
        "app_name": "ಆದಾಯ ಟ್ರ್ಯಾಕರ್",
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
        "title_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ - ಆದಾಯ ಟ್ರ್ಯಾಕರ್",
        "title_journal": "ಜರ್ನಲ್ ನಮೂದು - ಆದಾಯ ಟ್ರ್ಯಾಕರ್",
        "title_login": "ಲಾಗ್ ಇನ್ - ಆದಾಯ ಟ್ರ್ಯಾಕರ್",
        "title_register": "ನೋಂದಣಿ - ಆದಾಯ ಟ್ರ್ಯಾಕರ್",
    },
    "ml": {
        # Common / Navbar
        "app_name": "വരുമാനം ട്രാക്കർ",
        "menu": "മെനു",
        "nav_dashboard": "ഡാഷ്‌ബോർഡ്",
        "nav_journal": "ജേർണൽ",
        "nav_logout": "ലോഗ് ഔട്ട്",
        "nav_login": "ലോഗ് ഇൻ",
        "nav_register": "രജിസ്റ്റർ",

        # Dashboard
        "dashboard_title": "ഡാഷ്‌ബോർഡ്",
        "weekly_summary": "പ്രതിവാര സംഗ്രഹം (കഴിഞ്ഞ 7 ദിവസം)",
        "monthly_summary": "മാസിക സംഗ്രഹം (കഴിഞ്ഞ 6 മാസം)",
        "add_journal_entry": "ജേർണൽ എൻട്രി ചേർക്കുക",
        "chart_income": "വരുമാനം",
        "chart_expenses": "ചെലവുകൾ",
        "chart_withdrawals": "പിൻവലിക്കലുകൾ",
        "chart_net_income": "അറ്റ വരുമാനം",

        # Journal
        "journal_title": "ജേർണൽ എൻട്രി",
        "existing_entry_for": "{date} തീയതിക്കുള്ള നിലവിലുള്ള എൻട്രി:",
        "income_label": "വരുമാനം",
        "expenses_label": "ചെലവുകൾ",
        "withdrawals_label": "പിൻവലിക്കലുകൾ",
        "notes_label": "കുറിപ്പുകൾ",
        "date_label": "തീയതി",
        "entry_exists_banner": "ഈ തീയതിക്ക് ഒരു എൻട്രി നിലവിലുണ്ട്. സമർപ്പിച്ചാൽ അപ്‌ഡേറ്റ് സ്ഥിരീകരിക്കാൻ ആവശ്യപ്പെടും.",
        "optional_notes": "ഐച്ഛിക കുറിപ്പുകൾ...",
        "confirm_update": "അപ്‌ഡേറ്റ് സ്ഥിരീകരിക്കുക",
        "save_entry": "എൻട്രി സേവ് ചെയ്യുക",

        # Login
        "login_title": "ലോഗ് ഇൻ",
        "your_username": "നിങ്ങളുടെ ഉപയോക്തൃനാമം",
        "your_password": "നിങ്ങളുടെ പാസ്‌വേഡ്",
        "login_button": "ലോഗ് ഇൻ",
        "no_account": "അക്കൗണ്ട് ഇല്ലേ?",
        "register_link": "രജിസ്റ്റർ ചെയ്യുക",

        # Register
        "create_account": "അക്കൗണ്ട് ഉണ്ടാക്കുക",
        "choose_username": "ഒരു ഉപയോക്തൃനാമം തിരഞ്ഞെടുക്കുക",
        "min_chars": "കുറഞ്ഞത് 6 അക്ഷരങ്ങൾ",
        "reenter_password": "പാസ്‌വേഡ് വീണ്ടും നൽകുക",
        "register_button": "രജിസ്റ്റർ ചെയ്യുക",
        "have_account": "ഇതിനകം അക്കൗണ്ട് ഉണ്ടോ?",
        "login_link": "ലോഗ് ഇൻ ചെയ്യുക",

        # Form labels
        "form_username": "ഉപയോക്തൃനാമം",
        "form_password": "പാസ്‌വേഡ്",
        "form_confirm_password": "പാസ്‌വേഡ് സ്ഥിരീകരിക്കുക",

        # Validation
        "username_taken": "ഉപയോക്തൃനാമം ഇതിനകം ഉപയോഗിക്കപ്പെട്ടിരിക്കുന്നു.",

        # Flash messages
        "flash_register_success": "രജിസ്‌ട്രേഷൻ വിജയകരമായി. ദയവായി ലോഗ് ഇൻ ചെയ്യുക.",
        "flash_invalid_credentials": "അസാധുവായ ഉപയോക്തൃനാമം അല്ലെങ്കിൽ പാസ്‌വേഡ്.",
        "flash_logged_out": "നിങ്ങൾ ലോഗ് ഔട്ട് ചെയ്തു.",
        "flash_entry_updated": "{date} തീയതിയിലെ എൻട്രി വിജയകരമായി അപ്‌ഡേറ്റ് ചെയ്തു.",
        "flash_entry_exists": "{date} തീയതിക്ക് ഒരു എൻട്രി നിലവിലുണ്ട്. താഴെയുള്ള മൂല്യങ്ങൾ പരിശോധിച്ച് അപ്‌ഡേറ്റ് സ്ഥിരീകരിക്കുക.",
        "flash_entry_saved": "{date} തീയതിയിലെ എൻട്രി വിജയകരമായി സേവ് ചെയ്തു.",
        "flash_login_required": "ഈ പേജ് ആക്‌സസ് ചെയ്യാൻ ദയവായി ലോഗ് ഇൻ ചെയ്യുക.",

        # Page titles
        "title_dashboard": "ഡാഷ്‌ബോർഡ് - വരുമാനം ട്രാക്കർ",
        "title_journal": "ജേർണൽ എൻട്രി - വരുമാനം ട്രാക്കർ",
        "title_login": "ലോഗ് ഇൻ - വരുമാനം ട്രാക്കർ",
        "title_register": "രജിസ്റ്റർ - വരുമാനം ട്രാക്കർ",
    },
}
