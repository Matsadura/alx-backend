# i18n

### 1. **Parametrize Flask Templates to Display Different Languages**

To display different languages in a Flask application, you need to:
1. Use a translation library like **Flask-Babel**.
2. Parametrize your templates to dynamically change the displayed text based on the selected language.

#### Steps to Parametrize Templates:

- **Install Flask-Babel**:
   ```bash
   pip install Flask-Babel
   ```

- **Set Up Flask-Babel**:
   Initialize `Flask-Babel` in your Flask app to handle language selection and localization.
   ```python
   from flask import Flask
   from flask_babel import Babel

   app = Flask(__name__)
   babel = Babel(app)

   @babel.localeselector
   def get_locale():
       # Automatically detects the language from URL or headers
       return request.accept_languages.best_match(['en', 'es', 'fr'])
   ```

- **Parametrize Templates**:
   In your Flask templates, use the `_()` function to mark the text for translation:
   ```html
   <p>{{ _("Welcome") }}</p>
   ```

- **Generate Translation Files**:
   Use `Flask-Babel` to extract texts for translation from your templates and Python code.
   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```

- **Create Translations**:
   Create translation files for each language:
   ```bash
   pybabel init -i messages.pot -d translations -l es  # Spanish
   pybabel init -i messages.pot -d translations -l fr  # French
   ```

- **Translate**:
   Open the `.po` files in the `translations` directory and provide translations for each marked string.

- **Compile Translations**:
   After editing, compile the translations:
   ```bash
   pybabel compile -d translations
   ```

#### Template Example:
```html
<!DOCTYPE html>
<html>
  <body>
    <h1>{{ _("Hello, World!") }}</h1>
  </body>
</html>
```

---

### 2. **Infer the Correct Locale Based on URL Parameters, User Settings, or Request Headers**

You can infer the correct locale based on several factors such as URL parameters, user settings (e.g., stored preferences), or request headers.

#### Approach 1: Locale from URL Parameters
You can pass the locale as part of the URL, then adjust your app to use it.
```python
@app.route('/<lang_code>/home')
def home(lang_code):
    # Set the locale based on URL parameter
    session['lang'] = lang_code
    return render_template('home.html')

@babel.localeselector
def get_locale():
    # Use the 'lang' session variable if it's set
    return session.get('lang', 'en')
```

#### Approach 2: Locale from User Settings
If you have user accounts, you can store the user's preferred language in their profile and use it when they log in.
```python
@babel.localeselector
def get_locale():
    if 'user' in session:
        user = get_user_from_session()
        return user.preferred_language
    return 'en'  # default language
```

#### Approach 3: Locale from Request Headers
If the language is not provided explicitly, you can infer it from the `Accept-Language` HTTP header sent by the browser.
```python
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'fr'])
```

---

### 3. **Localize Timestamps**

To localize timestamps, you can use `Flask-Babel` to format dates and times based on the user's locale.

#### Localizing Timestamps with Flask-Babel

- **Set up Timezone Support**:
   You can use `Flask-Babel`'s built-in support for formatting dates and times according to the user's locale and timezone.

```python
from flask_babel import format_datetime
import datetime

@app.route('/datetime')
def show_datetime():
    current_time = datetime.datetime.utcnow()
    return f"<p>{format_datetime(current_time)}</p>"
```

- **Specify Timezones**:
   You can pass a timezone to `format_datetime` to convert the time to the user’s local timezone.
```python
from pytz import timezone
local_time = format_datetime(current_time, tzinfo=timezone('Europe/Paris'))
```

- **Display Locale-Specific Timestamps in Templates**:
   In your templates, you can use the `{{ format_datetime() }}` function to automatically format dates based on the selected locale.
```html
<p>{{ format_datetime(current_time) }}</p>
```

#### Example of Localized Timestamp in French:
For a user with a French locale, a timestamp like `2024-09-18 15:30:00` would be displayed as `18 Septembre 2024, 15:30`.
