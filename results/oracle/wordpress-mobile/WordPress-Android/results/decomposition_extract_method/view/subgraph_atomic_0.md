<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.wordpress.android.ui.prefs.SiteSettingsFragment#onPreferenceChange(Preference,Object)`\
target: `org.wordpress.android.ui.prefs.SiteSettingsFragment#privacyStringForValue(int)`\
type: `EXTRACT`\
commit: [1b21ba4bc](https://github.com/wordpress-mobile/WordPress-Android/commit/1b21ba4bcea986988d4bbd578e3bb9a20ec69606)\
description: `Extract Method private privacyStringForValue(value int) : String extracted from public onPreferenceChange(preference Preference, newValue Object) : boolean in class org.wordpress.android.ui.prefs.SiteSettingsFragment`

id: `1`\
source `org.wordpress.android.ui.prefs.SiteSettingsFragment#onPreferenceChange(Preference,Object)`\
target: `org.wordpress.android.ui.prefs.SiteSettingsFragment#changeEditTextPreferenceValue(EditTextPreference,String)`\
type: `EXTRACT`\
commit: [1b21ba4bc](https://github.com/wordpress-mobile/WordPress-Android/commit/1b21ba4bcea986988d4bbd578e3bb9a20ec69606)\
description: `Extract Method private changeEditTextPreferenceValue(pref EditTextPreference, newValue String) : void extracted from public onPreferenceChange(preference Preference, newValue Object) : boolean in class org.wordpress.android.ui.prefs.SiteSettingsFragment`

id: `2`\
source `org.wordpress.android.ui.prefs.SiteSettingsFragment#onPreferenceChange(Preference,Object)`\
target: `org.wordpress.android.ui.prefs.SiteSettingsFragment#changeLanguageValue(String)`\
type: `EXTRACT`\
commit: [1b21ba4bc](https://github.com/wordpress-mobile/WordPress-Android/commit/1b21ba4bcea986988d4bbd578e3bb9a20ec69606)\
description: `Extract Method private changeLanguageValue(newValue String) : void extracted from public onPreferenceChange(preference Preference, newValue Object) : boolean in class org.wordpress.android.ui.prefs.SiteSettingsFragment`

