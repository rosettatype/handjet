## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[15] Family checks</b></summary><div><details><summary>ℹ <b>INFO:</b> Check axis ordering on the STAT table.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT/axis_order">com.google.fonts/check/STAT/axis_order</a>)</summary><div>

>
>This is (for now) a merely informative check to detect what's the axis ordering declared on the STAT table of fonts in the Google Fonts collection.
>
>We may later update this to enforce some unified axis ordering scheme, yet to be determined.
>
* ℹ **INFO** From a total of 1 font files, 0 of them (0.00%) lack a STAT table.

	And these are the most common STAT axis orderings:
	('wght-ELSH-ELGR', 1) [code: summary]
</div></details><details><summary>🍞 <b>PASS:</b> Ensure that all variable font files have the same set of axes and axis ranges. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/consistent_axes">com.google.fonts/check/varfont/consistent_axes</a>)</summary><div>

>
>In order to facilitate the construction of intuitive and friendly user interfaces, all variable font files in a given family should have the same set of variation axes. Also, each axis must have a consistent setting of min/max value ranges accross all the files.
>
* 🍞 **PASS** All looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Does font file include unacceptable control character glyphs? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/control_chars">com.google.fonts/check/family/control_chars</a>)</summary><div>

>
>Use of some unacceptable control characters in the U+0000 - U+001F range can lead to rendering issues on some platforms.
>
>Acceptable control characters are defined as .null (U+0000) and CR (U+000D) for this test.
>
* 🍞 **PASS** Unacceptable control characters were not identified.
</div></details><details><summary>🍞 <b>PASS:</b> Ensure Italic styles have Roman counterparts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/italics_have_roman_counterparts">com.google.fonts/check/family/italics_have_roman_counterparts</a>)</summary><div>

>
>For each font family on Google Fonts, every Italic style must have a Roman sibling.
>
>This kind of problem was first observed at [1] where the Bold style was missing but BoldItalic was included.
>
>[1] https://github.com/google/fonts/pull/1482
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Checking all files are in the same directory. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/single_directory">com.google.fonts/check/family/single_directory</a>)</summary><div>

>
>If the set of font files passed in the command line is not all in the same directory, then we warn the user since the tool will interpret the set of files as belonging to a single family (and it is unlikely that the user would store the files from a single family spreaded in several separate directories).
>
* 🍞 **PASS** All files are in the same directory.
</div></details><details><summary>🍞 <b>PASS:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>

>
>We want all fonts within a family to have the same vertical metrics so their line spacing is consistent across the family.
>
* 🍞 **PASS** Vertical metrics are the same across the family.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have equal unicode encodings? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cmap.html#com.google.fonts/check/family/equal_unicode_encodings">com.google.fonts/check/family/equal_unicode_encodings</a>)</summary><div>


* 🍞 **PASS** Fonts have equal unicode encodings.
</div></details><details><summary>🍞 <b>PASS:</b> Make sure all font files have the same version value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/family/equal_font_versions">com.google.fonts/check/family/equal_font_versions</a>)</summary><div>


* 🍞 **PASS** All font files have the same version.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have consistent PANOSE proportion? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_proportion">com.google.fonts/check/family/panose_proportion</a>)</summary><div>


* 🍞 **PASS** Fonts have consistent PANOSE proportion.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have consistent PANOSE family type? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_familytype">com.google.fonts/check/family/panose_familytype</a>)</summary><div>


* 🍞 **PASS** Fonts have consistent PANOSE family type.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have consistent underline thickness? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/family/underline_thickness">com.google.fonts/check/family/underline_thickness</a>)</summary><div>

>
>Dave C Lemon (Adobe Type Team) recommends setting the underline thickness to be consistent across the family.
>
>If thicknesses are not family consistent, words set on the same line which have different styles look strange.
>
* 🍞 **PASS** Fonts have consistent underline thickness.
</div></details><details><summary>🍞 <b>PASS:</b> Verify that each group of fonts with the same nameID 1 has maximum of 4 fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/family/max_4_fonts_per_family_name">com.adobe.fonts/check/family/max_4_fonts_per_family_name</a>)</summary><div>

>
>Per the OpenType spec:
>
>'The Font Family name [...] should be shared among at most four fonts that differ only in weight or style [...]'
>
* 🍞 **PASS** There were no more than 4 fonts per family name.
</div></details><details><summary>💤 <b>SKIP:</b> All tabular figures must have the same width across the RIBBI-family. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/tnum_horizontal_metrics">com.google.fonts/check/family/tnum_horizontal_metrics</a>)</summary><div>

>
>Tabular figures need to have the same metrics in all styles in order to allow tables to be set with proper typographic control, but to maintain the placement of decimals and numeric columns between rows.
>
>Here's a good explanation of this: https://www.typography.com/techniques/fonts-for-financials/#tabular-figs
>
* 💤 **SKIP** Unfulfilled Conditions: RIBBI_ttFonts
</div></details><details><summary>💤 <b>SKIP:</b> Check README.md has a sample image. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/sample_image">com.google.fonts/check/repo/sample_image</a>)</summary><div>

>
>In order to showcase what a font family looks like, the project's README.md file should ideally include a sample image and highlight it in the upper portion of the document, no more than 10 lines away from the top of the file.
>
* 💤 **SKIP** Unfulfilled Conditions: readme_contents, readme_directory
</div></details><details><summary>💤 <b>SKIP:</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1 (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.adobe.fonts/check/family/bold_italic_unique_for_nameid1">com.adobe.fonts/check/family/bold_italic_unique_for_nameid1</a>)</summary><div>

>
>Per the OpenType spec: name ID 1 'is used in combination with Font Subfamily name (name ID 2), and should be shared among at most four fonts that differ only in weight or style.
>
>This four-way distinction should also be reflected in the OS/2.fsSelection field, using bits 0 and 5.
>
* 💤 **SKIP** Unfulfilled Conditions: RIBBI_ttFonts
</div></details><br></div></details><details><summary><b>[212] Handjet[ELGR,ELSH,wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Stricter unitsPerEm criteria for Google Fonts.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict">com.google.fonts/check/unitsperem_strict</a>)</summary><div>

>
>Even though the OpenType spec allows unitsPerEm to be any value between 16 and 16384, the Google Fonts project aims at a narrower set of reasonable values.
>
>The spec suggests usage of powers of two in order to get some performance improvements on legacy renderers, so those values are acceptable.
>
>But values of 500 or 1000 are also acceptable, with the added benefit that it makes upm math easier for designers, while the performance hit of not using a power of two is most likely negligible nowadays.
>
>Additionally, values above 2048 would likely result in unreasonable filesize increases.
>
* 🔥 **FAIL** Font em size (unitsPerEm) is 8160. If possible, please consider using 1000. Good values for unitsPerEm, though, are typically these: [16, 32, 64, 128, 256, 500, 512, 1000, 1024, 2000, 2048]. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

>
>There have been bugs rendering variable fonts with nested components. Additionally, some static fonts with nested components have been reported to have rendering and printing issues.
>
>For more info, see: * https://github.com/googlefonts/fontbakery/issues/2961 * https://github.com/arrowtype/recursive/issues/412
>
* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* Q
	* i
	* i
	* j
	* j
	* quotedbl
	* quotedbl
	* uni2010
	* uni00AD
	* uni2011 and 1656 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>

>
>Check a font's STAT table contains compulsory Axis Values which exist in the Google Fonts Axis Registry.
>
>We cannot determine what Axis Values the user will set for axes such as opsz, GRAD since these axes are unique for each font so we'll skip them.
>
* 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

 | Name | Axis | Current Value | Current Flags | Current LinkedValue | Expected Value | Expected Flags | Expected LinkedValue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Thin | wght | 100.0 | 0 | None | 100.0 | 0 | None |
| ExtraLight | wght | 200.0 | 0 | None | 200.0 | 0 | None |
| Light | wght | 300.0 | 0 | None | 300.0 | 0 | None |
| Regular | wght | 400.0 | 0 | None | 400.0 | 2 | 700.0 |
| Medium | wght | 500.0 | 0 | None | 500.0 | 0 | None |
| SemiBold | wght | 600.0 | 0 | None | 600.0 | 0 | None |
| Bold | wght | 700.0 | 0 | None | 700.0 | 0 | None |
| ExtraBold | wght | 800.0 | 0 | None | 800.0 | 0 | None |
| Black | wght | 900.0 | 0 | None | 900.0 | 0 | None |
 [code: bad-axis-values]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender+abs(descender)+linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 9120 when it should be at least 9792 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure that the font can be rasterized by FreeType. (derived from com.adobe.fonts/check/freetype_rasterizer) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.adobe.fonts/check/freetype_rasterizer">com.adobe.fonts/check/freetype_rasterizer</a>)</summary><div>

>
>Malformed fonts can cause FreeType to crash.
>
* 🔎 **DEBUG** Overridden check status, original: <Status SKIP>
* 🔥 **FAIL** FreeType is not available; to install it, invoke the 'freetype' extra when installing Font Bakery. [code: freetype-not-installed]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>

>
>Fonts with ligatures should have kerning on the corresponding non-ligated sequences for text where ligatures aren't used (eg https://github.com/impallari/Raleway/issues/14).
>
* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- idieresis + idieresis

	- a.men + a.ech

	- a.ech + a.eh

	- a.eh + a.ini

	- a.ini + a.ken

	- a.ken + a.now

	- a.now + a.xeh

	- hbVav + hbVav

	- hbVav + hbYod

	- hbYod + hbYod

	- hbYod + hbPatah 

	- And hbYod_hbYod + hbPatah [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure variable fonts include an avar table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mandatory_avar_table">com.google.fonts/check/mandatory_avar_table</a>)</summary><div>

>
>Most variable fonts should include an avar table to correctly define axes progression rates.
>
>For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000, because a 10% progression from 0% may be too much to define the 200, while 90% may be too little to define the 900.
>
>If the progression rates of axes is linear, this check can be ignored. Fontmake will also skip adding an avar table if the progression rates are linear. However, we still recommend designers visually proof each instance is at the expected weight, width etc.
>
* ⚠ **WARN** This variable font does not have an avar table. [code: missing-avar]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>

>
>The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
>
>- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font is designed for.
>
>- slng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font supports.
>
>The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
>
>The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
>
>The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
>
>This check ensures that the font has the meta table containing the slng and dlng structures.
>
>All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
>
>In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.
>
* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>

>
>Microsoft's recommendations for OpenType Fonts states the following:
>
>'NOTE: The PostScript glyph name must be no longer than 31 characters, include only uppercase or lowercase English letters, European digits, the period or the underscore, i.e. from the set [A-Za-z0-9_.] and should start with a letter, except the special glyph name ".notdef" which starts with a period.'
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/recom#post-table
>
>In practice, though, particularly in modern environments, glyph names can be as long as 63 characters.
>
>According to the "Adobe Glyph List Specification" available at:
>
>https://github.com/adobe-type-tools/agl-specification
>
* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
arLam.init_arAlifHamzabelow.fina, arLam.medi_arAlifHamzabelow.fina, arLam.init_arLam.medi_arHeh.fina, arHehDoachashmi.init_arYehBarri.fina and arHehDoachashmi.medi_arYehBarri.fina [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>

>
>Glyphs are either accessible directly through Unicode codepoints or through substitution rules.
>
>In Color Fonts, glyphs are also referenced by the COLR table.
>
>Any glyphs not accessible by either of these means are redundant and serve only to increase the font's file size.
>
* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- arFourFarsi.URD

	- arSevenFarsi.URD

	- dblgrave

	- guillemotleft.arab

	- guillemotright.arab

	- parenleft.arab

	- parenright.arab

	- period.arab

	- periodcentered.hebr

	- u1F415.black 

	- And 4 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>💤 <b>SKIP:</b> Does DESCRIPTION file contain broken links? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/broken_links">com.google.fonts/check/description/broken_links</a>)</summary><div>

>
>The snippet of HTML in the DESCRIPTION.en_us.html file is added to the font family webpage on the Google Fonts website. For that reason, all hyperlinks in it must be properly working.
>
* 💤 **SKIP** Unfulfilled Conditions: description_html
</div></details><details><summary>💤 <b>SKIP:</b> URLs on DESCRIPTION file must not display http(s) prefix. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/urls">com.google.fonts/check/description/urls</a>)</summary><div>

>
>The snippet of HTML in the DESCRIPTION.en_us.html file is added to the font family webpage on the Google Fonts website.
>
>Google Fonts has a content formatting policy for that snippet that expects the text content of links not to include the http:// or https:// prefixes.
>
* 💤 **SKIP** Unfulfilled Conditions: description_html
</div></details><details><summary>💤 <b>SKIP:</b> Does DESCRIPTION file contain a upstream Git repo URL? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/git_url">com.google.fonts/check/description/git_url</a>)</summary><div>

>
>The contents of the DESCRIPTION.en-us.html file are displayed on the Google Fonts website in the about section of each font family specimen page.
>
>Since all of the Google Fonts collection is composed of libre-licensed fonts, this check enforces a policy that there must be a hypertext link in that page directing users to the repository where the font project files are made available.
>
>Such hosting is typically done on sites like Github, Gitlab, GNU Savannah or any other git-based version control service.
>
* 💤 **SKIP** Unfulfilled Conditions: description_html
</div></details><details><summary>💤 <b>SKIP:</b> Is this a proper HTML snippet? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/valid_html">com.google.fonts/check/description/valid_html</a>)</summary><div>

>
>Sometimes people write malformed HTML markup. This check should ensure the file is good.
>
>Additionally, when packaging families for being pushed to the `google/fonts` git repo, if there is no DESCRIPTION.en_us.html file, some older versions of the `add_font.py` tool insert a placeholder description file which contains invalid html. This file needs to either be replaced with an existing description file or edited by hand.
>
* 💤 **SKIP** Unfulfilled Conditions: description
</div></details><details><summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html must have more than 200 bytes. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/min_length">com.google.fonts/check/description/min_length</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: description
</div></details><details><summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html should end in a linebreak. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/eof_linebreak">com.google.fonts/check/description/eof_linebreak</a>)</summary><div>

>
>Some older text-handling tools sometimes misbehave if the last line of data in a text file is not terminated with a newline character (also known as '\n').
>
>We know that this is a very small detail, but for the sake of keeping all DESCRIPTION.en_us.html files uniformly formatted throughout the GFonts collection, we chose to adopt the practice of placing this final linebreak character on them.
>
* 💤 **SKIP** Unfulfilled Conditions: description
</div></details><details><summary>💤 <b>SKIP:</b> Check METADATA.pb parse correctly. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/parses">com.google.fonts/check/metadata/parses</a>)</summary><div>

>
>The purpose of this check is to ensure that the METADATA.pb file is not malformed.
>
* 💤 **SKIP** Font family at 'fonts' lacks a METADATA.pb file. [code: file-not-found]
</div></details><details><summary>💤 <b>SKIP:</b> Font designer field in METADATA.pb must not be 'unknown'. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unknown_designer">com.google.fonts/check/metadata/unknown_designer</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Font designer field in METADATA.pb must not contain 'Multiple designers'. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/multiple_designers">com.google.fonts/check/metadata/multiple_designers</a>)</summary><div>

>
>For a while the string "Multiple designers" was used as a placeholder on METADATA.pb files. We should replace all those instances with actual designer names so that proper credits are displayed on the Google Fonts family specimen pages.
>
>If there's more than a single designer, the designer names must be separated by commas.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Multiple values in font designer field in METADATA.pb must be separated by commas. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/designer_values">com.google.fonts/check/metadata/designer_values</a>)</summary><div>

>
>We must use commas instead of forward slashes because the server-side code at the fonts.google.com directory will segment the string on the commas into a list of names and display the first item in the list as the "principal designer" while the remaining names are identified as "contributors".
>
>See eg https://fonts.google.com/specimen/Rubik
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Does METADATA.pb copyright field contain broken links? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/broken_links">com.google.fonts/check/metadata/broken_links</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Ensure METADATA.pb lists all font binaries. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/undeclared_fonts">com.google.fonts/check/metadata/undeclared_fonts</a>)</summary><div>

>
>The set of font binaries available, except the ones on a "static" subdir, must match exactly those declared on the METADATA.pb file.
>
>Also, to avoid confusion, we expect that font files (other than statics) are not placed on subdirectories.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Ensure METADATA.pb category field is valid. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/category">com.google.fonts/check/metadata/category</a>)</summary><div>

>
>There are only five acceptable values for the category field in a METADATA.pb file:
>
>- MONOSPACE
>
>- SANS_SERIF
>
>- SERIF
>
>- DISPLAY
>
>- HANDWRITING
>
>This check is meant to avoid typos in this field.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Check for METADATA subsets with zero support. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unsupported_subsets">com.google.fonts/check/metadata/unsupported_subsets</a>)</summary><div>

>
>This check ensures that the subsets specified on a METADATA.pb file are actually supported (even if only partially) by the font files.
>
>Subsets for which none of the codepoints are supported will cause the check to FAIL.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Check font has a license. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/has_license">com.google.fonts/check/family/has_license</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure
</div></details><details><summary>💤 <b>SKIP:</b> Font has ttfautohint params? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/has_ttfautohint_params">com.google.fonts/check/has_ttfautohint_params</a>)</summary><div>


* 💤 **SKIP** Font appears to our heuristic as not hinted using ttfautohint. [code: not-hinted]
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Fontfamily is listed on Google Fonts API? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/listed_on_gfonts">com.google.fonts/check/metadata/listed_on_gfonts</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: check if fonts field only has unique "full_name" values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unique_full_name_values">com.google.fonts/check/metadata/unique_full_name_values</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: check if fonts field only contains unique style:weight pairs. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unique_weight_style_pairs">com.google.fonts/check/metadata/unique_weight_style_pairs</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb license is "APACHE2", "UFL" or "OFL"? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/license">com.google.fonts/check/metadata/license</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb should contain at least "menu" and "latin" subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/menu_and_latin">com.google.fonts/check/metadata/menu_and_latin</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb subsets should be alphabetically ordered. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/subsets_order">com.google.fonts/check/metadata/subsets_order</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Check METADATA.pb includes production subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/includes_production_subsets">com.google.fonts/check/metadata/includes_production_subsets</a>)</summary><div>

>
>Check METADATA.pb file includes the same subsets as the family in production.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata, listed_on_gfonts_api
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Copyright notice is the same in all fonts? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/copyright">com.google.fonts/check/metadata/copyright</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Check that METADATA.pb family values are all the same. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/familyname">com.google.fonts/check/metadata/familyname</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: According to Google Fonts standards, families should have a Regular style. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/has_regular">com.google.fonts/check/metadata/has_regular</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Regular should be 400. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/regular_is_400">com.google.fonts/check/metadata/regular_is_400</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata, has_regular_style
</div></details><details><summary>💤 <b>SKIP:</b> Checks METADATA.pb font.name field matches family name declared on the name table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/family_name">com.google.fonts/check/metadata/nameid/family_name</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Checks METADATA.pb font.post_script_name matches postscript name declared on the name table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/post_script_name">com.google.fonts/check/metadata/nameid/post_script_name</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.full_name value matches fullname declared on the name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/full_name">com.google.fonts/check/metadata/nameid/full_name</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.name value should be same as the family name declared on the name table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/font_name">com.google.fonts/check/metadata/nameid/font_name</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata, style
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.full_name and font.post_script_name fields have equivalent values ? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_fullname_postscript">com.google.fonts/check/metadata/match_fullname_postscript</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_filename_postscript">com.google.fonts/check/metadata/match_filename_postscript</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata, not is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.name field contains font name in right format? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_name_values">com.google.fonts/check/metadata/valid_name_values</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: style, font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.full_name field contains font name in right format? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_full_name_values">com.google.fonts/check/metadata/valid_full_name_values</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: style, font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.filename field contains font name in right format? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_filename_values">com.google.fonts/check/metadata/valid_filename_values</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: style, family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.post_script_name field contains font name in right format? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_post_script_name_values">com.google.fonts/check/metadata/valid_post_script_name_values</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Copyright notices match canonical pattern in METADATA.pb (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_copyright">com.google.fonts/check/metadata/valid_copyright</a>)</summary><div>

>
>The expected pattern for the copyright string adheres to the following rules:
>
>* It must say "Copyright" followed by a 4 digit year (optionally followed by a hyphen and another 4 digit year)
>
>* Then it must say "The <familyname> Project Authors"
>
>* And within parentheses, a URL for a git repository must be provided
>
>* The check is case insensitive and does not validate whether the familyname is correct, even though we'd expect it is (and we may soon update the check to validate that aspect as well!)
>
>Here is an example of a valid copyright string:
>
>"Copyright 2017 The Archivo Black Project Authors (https://github.com/Omnibus-Type/ArchivoBlack)"
>
* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Copyright notice on METADATA.pb should not contain 'Reserved Font Name'. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/reserved_font_name">com.google.fonts/check/metadata/reserved_font_name</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Copyright notice shouldn't exceed 500 chars. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/copyright_max_length">com.google.fonts/check/metadata/copyright_max_length</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Font filenames match font.filename entries? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/filenames">com.google.fonts/check/metadata/filenames</a>)</summary><div>

>
>Note: This check only looks for files in the current directory.
>
>Font files in subdirectories are checked by these other two checks: - com.google.fonts/check/metadata/undeclared_fonts - com.google.fonts/check/repo/vf_has_static_fonts
>
>We may want to merge them all into a single check.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.style "italic" matches font internals? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/italic_style">com.google.fonts/check/metadata/italic_style</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.style "normal" matches font internals? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/normal_style">com.google.fonts/check/metadata/normal_style</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/family_and_full_names">com.google.fonts/check/metadata/nameid/family_and_full_names</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Check if fontname is not camel cased. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/fontname_not_camel_cased">com.google.fonts/check/metadata/fontname_not_camel_cased</a>)</summary><div>

>
>We currently have a policy of avoiding camel-cased font family names other than in a very small set of exceptions.
>
>If you want to have your family name added to the exceptions list, please read the instructions at https://github.com/googlefonts/fontbakery/issues/3270
>
* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Check font name is the same as family name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_name_familyname">com.google.fonts/check/metadata/match_name_familyname</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: family_metadata, font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Check that font weight has a canonical value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/canonical_weight_value">com.google.fonts/check/metadata/canonical_weight_value</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Check METADATA.pb font weights are correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/os2_weightclass">com.google.fonts/check/metadata/os2_weightclass</a>)</summary><div>

>
>Check METADATA.pb font weights are correct.
>
>For static fonts, the metadata weight should be the same as the static font's OS/2 usWeightClass.
>
>For variable fonts, the weight value should be 400 if the font's wght axis range includes 400, otherwise it should be the value closest to 400.
>
* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb weight matches postScriptName for static fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_weight_postscript">com.google.fonts/check/metadata/match_weight_postscript</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata, not is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Font styles are named canonically? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/canonical_style_names">com.google.fonts/check/metadata/canonical_style_names</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Version number has increased since previous release on Google Fonts? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/version_bump">com.google.fonts/check/version_bump</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: api_gfonts_ttFont, github_gfonts_ttFont
</div></details><details><summary>💤 <b>SKIP:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: api_gfonts_ttFont
</div></details><details><summary>💤 <b>SKIP:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: style
</div></details><details><summary>💤 <b>SKIP:</b> Checking post.italicAngle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than -20°, never more than -30°, and never greater than 0°. Note that in the OpenType specification, the value is negative for a lean rightwards.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 💤 **SKIP** Unfulfilled Conditions: style
</div></details><details><summary>💤 <b>SKIP:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>

>
>The values of the flags on the macStyle entry on the 'head' OpenType table that describe whether a font is bold and/or italic must be coherent with the actual style of the font as inferred by its filename.
>
* 💤 **SKIP** Unfulfilled Conditions: style
</div></details><details><summary>💤 <b>SKIP:</b> Copyright field for this font on METADATA.pb matches all copyright notice entries on the name table ? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/copyright">com.google.fonts/check/metadata/nameid/copyright</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: font_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Font has all mandatory 'name' table entries? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/mandatory_entries">com.google.fonts/check/name/mandatory_entries</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: style
</div></details><details><summary>💤 <b>SKIP:</b> PPEM must be an integer on hinted fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted">com.google.fonts/check/integer_ppem_if_hinted</a>)</summary><div>

>
>Hinted fonts must have head table flag bit 3 set.
>
>Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of Head::flags decides whether PPEM should be rounded. This bit should always be set for hinted fonts.
>
>Note: Bit 3 = Force ppem to integer values for all internal scaler math; May use fractional ppem sizes if this bit is clear;
>
* 💤 **SKIP** Unfulfilled Conditions: is_hinted
</div></details><details><summary>💤 <b>SKIP:</b> Directory name in GFonts repo structure must match NameID 1 of the regular. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/dirname_matches_nameid_1">com.google.fonts/check/repo/dirname_matches_nameid_1</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure, not is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> A static fonts directory with at least two fonts must accompany variable fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/vf_has_static_fonts">com.google.fonts/check/repo/vf_has_static_fonts</a>)</summary><div>

>
>Variable font family directories kept in the google/fonts git repo may include a static/ subdir containing static fonts.
>
>These files are meant to be served for users that still lack support for variable fonts in their web browsers.
>
* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure
</div></details><details><summary>💤 <b>SKIP:</b> Check upstream.yaml file contains all required fields (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/upstream_yaml_has_required_fields">com.google.fonts/check/repo/upstream_yaml_has_required_fields</a>)</summary><div>

>
>If a family has been pushed using the gftools packager, we must check that all the required fields in the upstream.yaml file have been populated.
>
* 💤 **SKIP** Unfulfilled Conditions: upstream_yaml
</div></details><details><summary>💤 <b>SKIP:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>

>
>If the family already exists on Google Fonts, we need to ensure that the checked family's vertical metrics are similar. This check will test the following schema which was outlined in Fontbakery issue #1162 [1]:
>
>- The family should visually have the same vertical metrics as the Regular style hosted on Google Fonts.
>
>- If the family on Google Fonts has differing hhea and typo metrics, the family being checked should use the typo metrics for both the hhea and typo entries.
>
>- If the family on Google Fonts has use typo metrics not enabled and the family being checked has it enabled, the hhea and typo metrics should use the family on Google Fonts winAscent and winDescent values.
>
>- If the upms differ, the values must be scaled so the visual appearance is the same.
>
>[1] https://github.com/googlefonts/fontbakery/issues/1162
>
* 💤 **SKIP** Unfulfilled Conditions: regular_remote_style
</div></details><details><summary>💤 <b>SKIP:</b> Check font follows the Google Fonts CJK vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_vertical_metrics">com.google.fonts/check/cjk_vertical_metrics</a>)</summary><div>

>
>CJK fonts have different vertical metrics when compared to Latin fonts. We follow the schema developed by dr Ken Lunde for Source Han Sans and the Noto CJK fonts.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/Spec#cjk-vertical-metrics
>
* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font
</div></details><details><summary>💤 <b>SKIP:</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_vertical_metrics_regressions">com.google.fonts/check/cjk_vertical_metrics_regressions</a>)</summary><div>

>
>Check CJK family has the same vertical metrics as the same family hosted on Google Fonts.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font, regular_remote_style
</div></details><details><summary>💤 <b>SKIP:</b> Does the font contain less than 40 CJK characters? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_not_enough_glyphs">com.google.fonts/check/cjk_not_enough_glyphs</a>)</summary><div>

>
>Hangul has 40 characters and it's the smallest CJK writing system.
>
>If a font contains less CJK glyphs than this writing system, we inform the user that some glyphs may be encoded incorrectly.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font
</div></details><details><summary>💤 <b>SKIP:</b> Ensure VFs with the GRAD axis do not vary horizontal advance.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/grade_reflow">com.google.fonts/check/varfont/grade_reflow</a>)</summary><div>

>
>The grade (GRAD) axis should not change any advanceWidth or kerning data across its design space. This is because altering the advance width of glyphs can cause text reflow.
>
* 💤 **SKIP** This font has no GRAD axis [code: no-grad]
</div></details><details><summary>💤 <b>SKIP:</b> Validate METADATA.pb axes values are within gf_axisregistry bounds.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/gf_axisregistry_bounds">com.google.fonts/check/metadata/gf_axisregistry_bounds</a>)</summary><div>

>
>Each axis range in a METADATA.pb file must be registered, and within the bounds of the axis definition in the Google Fonts Axis Registry, available at https://github.com/google/fonts/tree/main/axisregistry
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Validate METADATA.pb axes tags are defined in gf_axisregistry.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/gf_axisregistry_valid_tags">com.google.fonts/check/metadata/gf_axisregistry_valid_tags</a>)</summary><div>

>
>Ensure all axes in a METADATA.pb file are registered in the Google Fonts Axis Registry, available at https://github.com/google/fonts/tree/main/axisregistry
>
>Why does Google Fonts have its own Axis Registry?
>
>We support a superset of the OpenType axis registry axis set, and use additional metadata for each axis. Axes present in a font file but not in this registry will not function via our API. No variable font is expected to support all of the axes here.
>
>Any font foundry or distributor library that offers variable fonts has a implicit, latent, de-facto axis registry, which can be extracted by scanning the library for axes' tags, labels, and min/def/max values. While in 2016 Microsoft originally offered to include more axes in the OpenType 1.8 specification (github.com/microsoft/OpenTypeDesignVariationAxisTags), as of August 2020, this effort has stalled. We hope more foundries and distributors will publish documents like this that make their axes explicit, to encourage of adoption of variable fonts throughout the industry, and provide source material for a future update to the OpenType specification's axis registry.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Validate VF axes match the ones declared on METADATA.pb.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/consistent_axis_enumeration">com.google.fonts/check/metadata/consistent_axis_enumeration</a>)</summary><div>

>
>All font variation axes present in the font files must be properly declared on METADATA.pb so that they can be served by the GFonts API.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Ensure METADATA.pb does not use escaped strings. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/escaped_strings">com.google.fonts/check/metadata/escaped_strings</a>)</summary><div>

>
>In some cases we've seen designer names and other fields with escaped strings in METADATA files. Nowadays the strings can be full unicode strings and do not need escaping.
>
* 💤 **SKIP** Unfulfilled Conditions: metadata_file
</div></details><details><summary>💤 <b>SKIP:</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/designer_profiles">com.google.fonts/check/metadata/designer_profiles</a>)</summary><div>

>
>Google Fonts has a catalog of designers.
>
>This check ensures that the online entries of the catalog can be found based on the designer names listed on the METADATA.pb file.
>
>It also validates the URLs and file formats are all correctly set.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> On a family update, the DESCRIPTION.en_us.html file should ideally also be updated. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/family_update">com.google.fonts/check/description/family_update</a>)</summary><div>

>
>We want to ensure that any significant changes to the font family are properly mentioned in the DESCRIPTION file.
>
>In general, it means that the contents of the DESCRIPTION.en_us.html file will typically change if when font files are updated. Please treat this check as a reminder to do so whenever appropriate!
>
* 💤 **SKIP** Unfulfilled Conditions: description, github_gfonts_description
</div></details><details><summary>💤 <b>SKIP:</b> Check font family directory name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/family_directory_name">com.google.fonts/check/metadata/family_directory_name</a>)</summary><div>

>
>We want the directory name of a font family to be predictable and directly derived from the family name, all lowercased and removing spaces.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Check samples can be rendered. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/can_render_samples">com.google.fonts/check/metadata/can_render_samples</a>)</summary><div>

>
>In order to prevent tofu from being seen on fonts.google.com, this check verifies that all samples provided on METADATA.pb can be properly rendered by the font.
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Check if category on METADATA.pb matches what can be inferred from the family name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/category_hints">com.google.fonts/check/metadata/category_hints</a>)</summary><div>

>
>Sometimes the font familyname contains words that hint at which is the most likely correct category to be declared on METADATA.pb
>
* 💤 **SKIP** Unfulfilled Conditions: family_metadata
</div></details><details><summary>💤 <b>SKIP:</b> Each font in set of sibling families must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/vertical_metrics">com.google.fonts/check/superfamily/vertical_metrics</a>)</summary><div>

>
>We may want all fonts within a super-family (all sibling families) to have the same vertical metrics so their line spacing is consistent across the super-family.
>
>This is an experimental extended version of com.google.fonts/check/family/vertical_metrics and for now it will only result in WARNs.
>
* 💤 **SKIP** Sibling families were not detected.
</div></details><details><summary>💤 <b>SKIP:</b> Ensure indic fonts have the Indian Rupee Sign glyph.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/rupee">com.google.fonts/check/rupee</a>)</summary><div>

>
>Per Bureau of Indian Standards every font supporting one of the official Indian languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.
>
* 💤 **SKIP** Unfulfilled Conditions: is_indic_font
</div></details><details><summary>💤 <b>SKIP:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>

>
>Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
>
>However, a quotedbl should have 2 contours, unless the font belongs to a display family.
>
>This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.
>
* 💤 **SKIP** Unfulfilled Conditions: not is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Does the font contain chws and vchw features? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/cjk_chws_feature">com.google.fonts/check/cjk_chws_feature</a>)</summary><div>

>
>The W3C recommends the addition of chws and vchw features to CJK fonts to enhance the spacing of glyphs in environments which do not fully support JLREQ layout rules.
>
>The chws_tool utility (https://github.com/googlefonts/chws_tool) can be used to add these features automatically.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font
</div></details><details><summary>💤 <b>SKIP:</b> Is the CFF subr/gsubr call depth > 10? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_call_depth">com.adobe.fonts/check/cff_call_depth</a>)</summary><div>

>
>Per "The Type 2 Charstring Format, Technical Note #5177", the "Subr nesting, stack limit" is 10.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff
</div></details><details><summary>💤 <b>SKIP:</b> Is the CFF2 subr/gsubr call depth > 10? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff2_call_depth">com.adobe.fonts/check/cff2_call_depth</a>)</summary><div>

>
>Per "The CFF2 CharString Format", the "Subr nesting, stack limit" is 10.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff2
</div></details><details><summary>💤 <b>SKIP:</b> Does the font use deprecated CFF operators or operations? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_deprecated_operators">com.adobe.fonts/check/cff_deprecated_operators</a>)</summary><div>

>
>The 'dotsection' operator and the use of 'endchar' to build accented characters from the Adobe Standard Encoding Character Set ("seac") are deprecated in CFF. Adobe recommends repairing any fonts that use these, especially endchar-as-seac, because a rendering issue was discovered in Microsoft Word with a font that makes use of this operation. The check treats that usage as a FAIL. There are no known ill effects of using dotsection, so that check is a WARN.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff
</div></details><details><summary>💤 <b>SKIP:</b> Checking unitsPerEm value is reasonable. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/unitsperem">com.google.fonts/check/unitsperem</a>)</summary><div>

>
>According to the OpenType spec:
>
>The value of unitsPerEm at the head table must be a value between 16 and 16384. Any value in this range is valid.
>
>In fonts that have TrueType outlines, a power of 2 is recommended as this allows performance optimizations in some rasterizers.
>
>But 1000 is a commonly used value. And 2000 may become increasingly more common on Variable Fonts.
>
* 💤 **SKIP** Filtered: Google Fonts has a stricter policy which is enforced by com.google.fonts/check/unitsperem_strict
</div></details><details><summary>💤 <b>SKIP:</b> CFF table FontName must match name table ID 6 (PostScript name). (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_vs_cff">com.adobe.fonts/check/name/postscript_vs_cff</a>)</summary><div>

>
>The PostScript name entries in the font's 'name' table should match the FontName string in the 'CFF ' table.
>
>The 'CFF ' table has a lot of information that is duplicated in other tables. This information should be consistent across tables, because there's no guarantee which table an app will get the data from.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wdth_coord">com.google.fonts/check/varfont/regular_wdth_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wdth' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
>
>If a variable font has a 'wdth' (Width) axis, then the coordinate of its 'Regular' instance is required to be 100.
>
* 💤 **SKIP** Unfulfilled Conditions: has_wdth_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate must be zero on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_slnt_coord">com.google.fonts/check/varfont/regular_slnt_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'slnt' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_slnt
>
>If a variable font has a 'slnt' (Slant) axis, then the coordinate of its 'Regular' instance is required to be zero.
>
* 💤 **SKIP** Unfulfilled Conditions: has_slnt_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'ital' (Italic) axis coordinate must be zero on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_ital_coord">com.google.fonts/check/varfont/regular_ital_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'ital' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_ital
>
>If a variable font has a 'ital' (Italic) axis, then the coordinate of its 'Regular' instance is required to be zero.
>
* 💤 **SKIP** Unfulfilled Conditions: has_ital_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'opsz' (Optical Size) axis coordinate should be between 10 and 16 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_opsz_coord">com.google.fonts/check/varfont/regular_opsz_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'opsz' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_opsz
>
>If a variable font has an 'opsz' (Optical Size) axis, then the coordinate of its 'Regular' instance is recommended to be a value in the range 10 to 16.
>
* 💤 **SKIP** Unfulfilled Conditions: regular_opsz_coord
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'wdth' (Width) axis coordinate must be within spec range of 1 to 1000 on all instances. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wdth_valid_range">com.google.fonts/check/varfont/wdth_valid_range</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wdth' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
>
>On the 'wdth' (Width) axis, the valid coordinate range is 1-1000
>
* 💤 **SKIP** Unfulfilled Conditions: has_wdth_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate specifies positive values in its range?  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/slnt_range">com.google.fonts/check/varfont/slnt_range</a>)</summary><div>

>
>The OpenType spec says at https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_slnt that:
>
>[...] the scale for the Slant axis is interpreted as the angle of slant in counter-clockwise degrees from upright. This means that a typical, right-leaning oblique design will have a negative slant value. This matches the scale used for the italicAngle field in the post table.
>
* 💤 **SKIP** Unfulfilled Conditions: has_slnt_axis
</div></details><details><summary>💤 <b>SKIP:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>

>
>This check looks for outline segments which seem particularly short (less than 0.6% of the overall path length).
>
>This check is not run for variable fonts, as they may legitimately have short segments. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported short segments.
>
* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>

>
>This check looks for consecutive line segments which have the same angle. This normally happens if an outline point has been added by accident.
>
>This check is not run for variable fonts, as they may legitimately have colinear vectors.
>
* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>

>
>This check detects line segments which are nearly, but not quite, exactly horizontal or vertical. Sometimes such lines are created by design, but often they are indicative of a design error.
>
>This check is disabled for italic styles, which often contain nearly-upright lines.
>
* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Check that texts shape as per expectation (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/regression">com.google.fonts/check/shaping/regression</a>)</summary><div>

>
>Fonts with complex layout rules can benefit from regression tests to ensure that the rules are behaving as designed. This checks runs a shaping test suite and compares expected shaping against actual shaping, reporting any differences.
>
>Shaping test suites should be written by the font engineer and referenced in the fontbakery configuration file. For more information about write shaping test files and how to configure fontbakery to read the shaping test suites, see https://simoncozens.github.io/tdd-for-otl/
>
* 💤 **SKIP** Shaping test directory not defined in configuration file
</div></details><details><summary>💤 <b>SKIP:</b> Check that no forbidden glyphs are found while shaping (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/forbidden">com.google.fonts/check/shaping/forbidden</a>)</summary><div>

>
>Fonts with complex layout rules can benefit from regression tests to ensure that the rules are behaving as designed. This checks runs a shaping test suite and reports if any glyphs are generated in the shaping which should not be produced. (For example, .notdef glyphs, visible viramas, etc.)
>
>Shaping test suites should be written by the font engineer and referenced in the Font Bakery configuration file. For more information about write shaping test files and how to configure fontbakery to read the shaping test suites, see https://simoncozens.github.io/tdd-for-otl/
>
* 💤 **SKIP** Shaping test directory not defined in configuration file
</div></details><details><summary>💤 <b>SKIP:</b> Check that no collisions are found while shaping (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/collides">com.google.fonts/check/shaping/collides</a>)</summary><div>

>
>Fonts with complex layout rules can benefit from regression tests to ensure that the rules are behaving as designed. This checks runs a shaping test suite and reports instances where the glyphs collide in unexpected ways.
>
>Shaping test suites should be written by the font engineer and referenced in the fontbakery configuration file. For more information about write shaping test files and how to configure fontbakery to read the shaping test suites, see https://simoncozens.github.io/tdd-for-otl/
>
* 💤 **SKIP** Shaping test directory not defined in configuration file
</div></details><details><summary>ℹ <b>INFO:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>

>
>This check is merely informative, displaying and useful comparison of filesizes of hinted versus unhinted font files.
>
* ℹ **INFO** Hinting filesize impact:

 |               | fonts/Handjet[ELGR,ELSH,wght].ttf          |
 |:------------- | ---------------:|
 | Dehinted Size | 277.2kb |
 | Hinted Size   | 277.3kb   |
 | Increase      | 24 bytes      |
 | Change        | 0.0 %  |
 [code: size-impact]
</div></details><details><summary>ℹ <b>INFO:</b> Font has old ttfautohint applied? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint">com.google.fonts/check/old_ttfautohint</a>)</summary><div>

>
>Check if font has been hinted with an outdated version of ttfautohint.
>
* ℹ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 2.003'] [code: version-not-detected]
</div></details><details><summary>ℹ <b>INFO:</b> EPAR table present in font? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/epar">com.google.fonts/check/epar</a>)</summary><div>

>
>The EPAR table is/was a way of expressing common licensing permissions and restrictions in metadata; while almost nothing supported it, Dave Crossland wonders that adding it to everything in Google Fonts could help make it more popular.
>
>More info is available at: https://davelab6.github.io/epar/
>
* ℹ **INFO** EPAR table not present in font. To learn more see https://github.com/googlefonts/fontbakery/issues/818 [code: lacks-EPAR]
</div></details><details><summary>ℹ <b>INFO:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>

>
>Traditionally version 0 'gasp' tables were set so that font sizes below 8 ppem had no grid fitting but did have antialiasing. From 9-16 ppem, just grid fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled on. The use of accelerated graphics cards and higher resolution screens make this approach obsolete. Microsoft's DirectWrite pushed this even further with much improved rendering built into the OS and apps.
>
>In this scenario it makes sense to simply toggle all 4 flags ON for all font sizes.
>
* ℹ **INFO** These are the ppm ranges declared on the gasp table:

PPM <= 65535:
	flag = 0x0F
	- Use grid-fitting
	- Use grayscale rendering
	- Use gridfitting with ClearType symmetric smoothing
	- Use smoothing along multiple axes with ClearType®
 [code: ranges]
* 🍞 **PASS** The 'gasp' table is correctly set, with one gaspRange:value of 0xFFFF:0x0F.
</div></details><details><summary>ℹ <b>INFO:</b> Check for font-v versioning. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontv">com.google.fonts/check/fontv</a>)</summary><div>

>
>The git sha1 tagging and dev/release features of Source Foundry `font-v` tool are awesome and we would love to consider upstreaming the approach into fontmake someday. For now we only emit a WARN if a given font does not yet follow the experimental versioning style, but at some point we may start enforcing it.
>
* ℹ **INFO** Version string is: "Version 2.003"
The version string must ideally include a git commit hash and either a "dev" or a "release" suffix such as in the example below:
"Version 1.3; git-0d08353-release" [code: bad-format]
</div></details><details><summary>ℹ <b>INFO:</b> Font contains all required tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/required_tables">com.google.fonts/check/required_tables</a>)</summary><div>

>
>According to the OpenType spec https://docs.microsoft.com/en-us/typography/opentype/spec/otff#required-tables
>
>Whether TrueType or CFF outlines are used in an OpenType font, the following tables are required for the font to function correctly:
>
>- cmap (Character to glyph mapping)
>- head (Font header)
>- hhea (Horizontal header)
>- hmtx (Horizontal metrics)
>- maxp (Maximum profile)
>- name (Naming table)
>- OS/2 (OS/2 and Windows specific metrics)
>- post (PostScript information)
>
>The spec also documents that variable fonts require the following table:
>
>- STAT (Style attributes)
>
>Depending on the typeface and coverage of a font, certain tables are recommended for optimum quality.
>
>For example:
>- the performance of a non-linear font is improved if the VDMX, LTSH, and hdmx tables are present.
>- Non-monospaced Latin fonts should have a kern table.
>- A gasp table is necessary if a designer wants to influence the sizes at which grayscaling is used under Windows. Etc.
>
* ℹ **INFO** This font contains the following optional tables:

	- loca

	- prep

	- GPOS

	- GSUB 

	- And gasp [code: optional-tables]
* 🍞 **PASS** Font contains all required tables.
</div></details><details><summary>ℹ <b>INFO:</b> List all superfamily filepaths (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/list">com.google.fonts/check/superfamily/list</a>)</summary><div>

>
>This is a merely informative check that lists all sibling families detected by fontbakery.
>
>Only the fontfiles in these directories will be considered in superfamily-level checks.
>
* ℹ **INFO** fonts [code: family-path]
</div></details><details><summary>🍞 <b>PASS:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>

>
>A font's filename must be composed as "<familyname>-<stylename>.ttf":
>
>- Nunito-Regular.ttf
>
>- Oswald-BoldItalic.ttf
>
>Variable fonts must list the axis tags in alphabetical order in square brackets and separated by commas:
>
>- Roboto[wdth,wght].ttf
>
>- Familyname-Italic[wght].ttf
>
* 🍞 **PASS** Font filename is correct, "Handjet[ELGR,ELSH,wght].ttf".
</div></details><details><summary>🍞 <b>PASS:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>

>
>The fsType in the OS/2 table is a legacy DRM-related field. Fonts in the Google Fonts collection must have it set to zero (also known as "Installable Embedding"). This setting indicates that the fonts can be embedded in documents and permanently installed by applications on remote systems.
>
>More detailed info is available at: https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fstype
>
* 🍞 **PASS** OS/2 fsType is properly set to zero.
</div></details><details><summary>🍞 <b>PASS:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>

>
>Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
>
>Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
>
>https://docs.microsoft.com/en-us/typography/vendors/
>
>This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
>
>Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.
>
* 🍞 **PASS** OS/2 VendorID 'RST ' looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>

>
>Google Fonts expects that fonts in its collection support at least the minimal set of characters defined in the `GF-latin-core` glyph-set.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Substitute copyright, registered and trademark symbols in name table entries. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/unwanted_chars">com.google.fonts/check/name/unwanted_chars</a>)</summary><div>


* 🍞 **PASS** No need to substitute copyright, registered and trademark symbols in name table entries of this font.
</div></details><details><summary>🍞 <b>PASS:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>

>
>Google Fonts expects variable fonts, static ttfs and static otfs to have differing OS/2 usWeightClass values.
>
>- For Variable Fonts, Thin-Black must be 100-900
>
>- For static ttfs, Thin-Black can be 100-900 or 250-900
>
>- For static otfs, Thin-Black must be 250-900
>
>If static otfs are set lower than 250, text may appear blurry in legacy Windows applications.
>
>Glyphsapp users can change the usWeightClass value of an instance by adding a 'weightClass' customParameter.
>
* 🍞 **PASS** OS/2 usWeightClass is good
</div></details><details><summary>🍞 <b>PASS:</b> Check license file has good copyright string. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_copyright">com.google.fonts/check/license/OFL_copyright</a>)</summary><div>

>
>An OFL.txt file's first line should be the font copyright e.g: "Copyright 2019 The Montserrat Project Authors (https://github.com/julietaula/montserrat)"
>
* 🍞 **PASS** looks good
</div></details><details><summary>🍞 <b>PASS:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>

>
>Check OFL body text is correct. Often users will accidently delete parts of the body text.
>
* 🍞 **PASS** OFL license body text is correct
</div></details><details><summary>🍞 <b>PASS:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>

>
>A known licensing description must be provided in the NameID 14 (LICENSE DESCRIPTION) entries of the name table.
>
>The source of truth for this check (to determine which license is in use) is a file placed side-by-side to your font project including the licensing terms.
>
>Depending on the chosen license, one of the following string snippets is expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name table:
>
>- "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL"
>
>- "Licensed under the Apache License, Version 2.0"
>
>- "Licensed under the Ubuntu Font Licence 1.0."
>
>Currently accepted licenses are Apache or Open Font License. For a small set of legacy families the Ubuntu Font License may be acceptable as well.
>
>When in doubt, please choose OFL for new font projects.
>
* 🍞 **PASS** Licensing entry on name table is correctly set.
</div></details><details><summary>🍞 <b>PASS:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>

>
>A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry of the name table.
>
>The source of truth for this check is the licensing text found on the NameID 13 entry (LICENSE DESCRIPTION).
>
>The string snippets used for detecting licensing terms are:
>
>- "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL"
>
>- "Licensed under the Apache License, Version 2.0"
>
>- "Licensed under the Ubuntu Font Licence 1.0."
>
>Currently accepted licenses are Apache or Open Font License. For a small set of legacy families the Ubuntu Font License may be acceptable as well.
>
>When in doubt, please choose OFL for new font projects.
>
* 🍞 **PASS** Font has a valid license URL in NAME table.
</div></details><details><summary>🍞 <b>PASS:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>

>
>An old FontLab version had a bug which caused it to store copyright notices in nameID 10 entries.
>
>In order to detect those and distinguish them from actual legitimate usage of this name table entry, we expect that such strings do not exceed a reasonable length of 200 chars.
>
>Longer strings are likely instances of the FontLab bug.
>
* 🍞 **PASS** All description name records have reasonably small lengths.
</div></details><details><summary>🍞 <b>PASS:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>

>
>Serving extremely large font files on Google Fonts causes usability issues. This check ensures that file sizes are reasonable.
>
* 🍞 **PASS** Font had a reasonable file size
</div></details><details><summary>🍞 <b>PASS:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🍞 **PASS** Version format in NAME table entries is correct.
</div></details><details><summary>🍞 <b>PASS:</b> Make sure family name does not begin with a digit. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname_first_char">com.google.fonts/check/name/familyname_first_char</a>)</summary><div>

>
>Font family names which start with a numeral are often not discoverable in Windows applications.
>
* 🍞 **PASS** Font family name first character is not a digit.
</div></details><details><summary>🍞 <b>PASS:</b> Are there non-ASCII characters in ASCII-only NAME table entries? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/ascii_only_entries">com.google.fonts/check/name/ascii_only_entries</a>)</summary><div>

>
>The OpenType spec requires ASCII for the POSTSCRIPT_NAME (nameID 6).
>
>For COPYRIGHT_NOTICE (nameID 0) ASCII is required because that string should be the same in CFF fonts which also have this requirement in the OpenType spec.
>
>Note: A common place where we find non-ASCII strings is on name table entries with NameID > 18, which are expressly for localising the ASCII-only IDs into Hindi / Arabic / etc.
>
* 🍞 **PASS** None of the ASCII-only NAME table entries contain non-ASCII characteres.
</div></details><details><summary>🍞 <b>PASS:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🍞 **PASS** Name Table entry: Copyright field 'Copyright 2018 The Handjet Project Authors (https://github.com/rosettatype/Handjet/)' matches canonical pattern.
* 🍞 **PASS** Name table copyright entries are good
</div></details><details><summary>🍞 <b>PASS:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>

>
>Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families
>
* 🍞 **PASS** Font names are good:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Handjet | Handjet |
| Subfamily Name | Regular | Regular |
| Full Name | Handjet Regular | Handjet Regular |
| Poscript Name | Handjet-Regular | Handjet-Regular |
</div></details><details><summary>🍞 <b>PASS:</b> Length of copyright notice must not exceed 500 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/copyright_length">com.google.fonts/check/name/copyright_length</a>)</summary><div>

>
>This is an arbitrary max length for the copyright notice field of the name table. We simply don't want such notices to be too long. Typically such notices are actually much shorter than this with a length of roughly 70 or 80 characters.
>
* 🍞 **PASS** All copyright notice name entries on the 'name' table are shorter than 500 characters.
</div></details><details><summary>🍞 <b>PASS:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>

>
>We need to check names are not already used, and today the best place to check that is http://namecheck.fontdata.com
>
* 🍞 **PASS** Font familyname seems to be unique.
</div></details><details><summary>🍞 <b>PASS:</b> Check a static ttf can be generated from a variable font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/generate_static">com.google.fonts/check/varfont/generate_static</a>)</summary><div>

>
>Google Fonts may serve static fonts which have been generated from variable fonts. This test will attempt to generate a static ttf using fontTool's varLib mutator.
>
>The target font will be the mean of each axis e.g:
>
>## VF font axes
>
>- min weight, max weight = 400, 800
>
>- min width, max width = 50, 100
>
>## Target Instance
>
>- weight = 600
>
>- width = 75
>
* 🍞 **PASS** fontTools.varLib.mutator generated a static font instance
</div></details><details><summary>🍞 <b>PASS:</b> Check that variable fonts have an HVAR table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/has_HVAR">com.google.fonts/check/varfont/has_HVAR</a>)</summary><div>

>
>Not having a HVAR table can lead to costly text-layout operations on some platforms, which we want to avoid.
>
>So, all variable fonts on the Google Fonts collection should have an HVAR with valid values.
>
>More info on the HVAR table can be found at: https://docs.microsoft.com/en-us/typography/opentype/spec/otvaroverview#variation-data-tables-and-miscellaneous-requirements
>
* 🍞 **PASS** This variable font contains an HVAR table.
</div></details><details><summary>🍞 <b>PASS:</b> Font enables smart dropout control in "prep" table instructions? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout">com.google.fonts/check/smart_dropout</a>)</summary><div>

>
>This setup is meant to ensure consistent rendering quality for fonts across all devices (with different rendering/hinting capabilities).
>
>Below is the snippet of instructions we expect to see in the fonts: B8 01 FF    PUSHW 0x01FF 85          SCANCTRL (unconditinally turn on dropout control mode) B0 04       PUSHB 0x04 8D          SCANTYPE (enable smart dropout control)
>
>"Smart dropout control" means activating rules 1, 2 and 5: Rule 1: If a pixel's center falls within the glyph outline, that pixel is turned on. Rule 2: If a contour falls exactly on a pixel's center, that pixel is turned on. Rule 5: If a scan line between two adjacent pixel centers (either vertical or horizontal) is intersected by both an on-Transition contour and an off-Transition contour and neither of the pixels was already turned on by rules 1 and 2, turn on the pixel which is closer to the midpoint between the on-Transition contour and off-Transition contour. This is "Smart" dropout control.
>
>For more detailed info (such as other rules not enabled in this snippet), please refer to the TrueType Instruction Set documentation.
>
* 🍞 **PASS** 'prep' table contains instructions enabling smart dropout control.
</div></details><details><summary>🍞 <b>PASS:</b> There must not be VTT Talk sources in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vttclean">com.google.fonts/check/vttclean</a>)</summary><div>

>
>The goal here is to reduce filesizes and improve pageloading when dealing with webfonts.
>
>The VTT Talk sources are not necessary at runtime and endup being just dead weight when left embedded in the font binaries. The sources should be kept on the project files but stripped out when building release binaries.
>
* 🍞 **PASS** There are no tables with VTT Talk sources embedded in the font.
</div></details><details><summary>🍞 <b>PASS:</b> Are there unwanted Apple tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/aat">com.google.fonts/check/aat</a>)</summary><div>

>
>Apple's TrueType reference manual [1] describes SFNT tables not in the Microsoft OpenType specification [2] and these can sometimes sneak into final release files, but Google Fonts should only have OpenType tables.
>
>[1] https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6.html [2] https://docs.microsoft.com/en-us/typography/opentype/spec/
>
* 🍞 **PASS** There are no unwanted AAT tables.
</div></details><details><summary>🍞 <b>PASS:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>

>
>Check a font's fvar instance coordinates comply with our guidelines: https://googlefonts.github.io/gf-guide/variable.html#fvar-instances
>
* 🍞 **PASS** fvar instances are good:

| Name | current | expected |
| :--- | :--- | :--- |
| Thin | wght=100.0, ELGR=1.0, ELSH=2.0 | wght=100.0, ELGR=1.0, ELSH=2.0 |
| ExtraLight | wght=200.0, ELGR=1.0, ELSH=2.0 | wght=200.0, ELGR=1.0, ELSH=2.0 |
| Light | wght=300.0, ELGR=1.0, ELSH=2.0 | wght=300.0, ELGR=1.0, ELSH=2.0 |
| Regular | wght=400.0, ELGR=1.0, ELSH=2.0 | wght=400.0, ELGR=1.0, ELSH=2.0 |
| Medium | wght=500.0, ELGR=1.0, ELSH=2.0 | wght=500.0, ELGR=1.0, ELSH=2.0 |
| SemiBold | wght=600.0, ELGR=1.0, ELSH=2.0 | wght=600.0, ELGR=1.0, ELSH=2.0 |
| Bold | wght=700.0, ELGR=1.0, ELSH=2.0 | wght=700.0, ELGR=1.0, ELSH=2.0 |
| ExtraBold | wght=800.0, ELGR=1.0, ELSH=2.0 | wght=800.0, ELGR=1.0, ELSH=2.0 |
| Black | wght=900.0, ELGR=1.0, ELSH=2.0 | wght=900.0, ELGR=1.0, ELSH=2.0 |
</div></details><details><summary>🍞 <b>PASS:</b> All name entries referenced by fvar instances exist on the name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_name_entries">com.google.fonts/check/fvar_name_entries</a>)</summary><div>

>
>The purpose of this check is to make sure that all name entries referenced by variable font instances do exist in the name table.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>

>
>All ligatures in a font must have corresponding caret (text cursor) positions defined in the GDEF table, otherwhise, users may experience issues with caret rendering.
>
>If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names starting with 'caret_'. These can be compiled with fontmake as of version v2.4.0.
>
* 🍞 **PASS** Looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/googlefonts/fontbakery/issues/2179
>
* 🍞 **PASS** All name entries are good.
</div></details><details><summary>🍞 <b>PASS:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>

>
>There are some entries on the name table that may include more than one line of text. The Google Fonts team, though, prefers to keep the name table entries short and simple without line breaks.
>
>For instance, some designers like to include the full text of a font license in the "copyright notice" entry, but for the GFonts collection this entry should only mention year, author and other basic info in a manner enforced by com.google.fonts/check/font_copyright
>
* 🍞 **PASS** Name table entries are all single-line (no line-breaks found).
</div></details><details><summary>🍞 <b>PASS:</b> Name table strings must not contain the string 'Reserved Font Name'. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/rfn">com.google.fonts/check/name/rfn</a>)</summary><div>

>
>Some designers adopt the "Reserved Font Name" clause of the OFL license. This means that the original author reserves the rights to the family name and other people can only distribute modified versions using a different family name.
>
>Google Fonts published updates to the fonts in the collection in order to fix issues and/or implement further improvements to the fonts. It is important to keep the family name so that users of the webfonts can benefit from the updates. Since it would forbid such usage scenario, all families in the GFonts collection are required to not adopt the RFN clause.
>
>This check ensures "Reserved Font Name" is not mentioned in the name table.
>
* 🍞 **PASS** None of the name table strings contain "Reserved Font Name".
</div></details><details><summary>🍞 <b>PASS:</b> A font repository should not include fontbakery report files (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/fb_report">com.google.fonts/check/repo/fb_report</a>)</summary><div>

>
>A FontBakery report is ephemeral and so should be used for posting issues on a bug-tracker instead of being hosted in the font project repository.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> A font repository should not include ZIP files (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/zip_files">com.google.fonts/check/repo/zip_files</a>)</summary><div>

>
>Sometimes people check in ZIPs into their font project repositories. While we accept the practice of checking in binaries, we believe that a ZIP is a step too far ;)
>
>Note: a source purist position is that only source files and build scripts should be checked in.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Check variable font instances don't have duplicate names (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_duplicate_instance_names">com.google.fonts/check/varfont_duplicate_instance_names</a>)</summary><div>

>
>This check's purpose is to detect duplicate named instances names in a given variable font. Repeating instance names may be the result of instances for several VF axes defined in `fvar`, but since currently only weight+italic tokens are allowed in instance names as per GF specs, they ended up repeating. Instead, only a base set of fonts for the most default representation of the family can be defined through instances in the `fvar` table, all other instances will have to be left to access through the `STAT` table.
>
* 🍞 **PASS** Instance names are unique
</div></details><details><summary>🍞 <b>PASS:</b> Ensure VFs do not contain the ital axis.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/unsupported_axes">com.google.fonts/check/varfont/unsupported_axes</a>)</summary><div>

>
>The 'ital' axis is not supported yet in Google Chrome.
>
>For the time being, we need to ensure that VFs do not contain this axis. Once browser support is better, we can deprecate this check.
>
>For more info regarding browser support, see: https://arrowtype.github.io/vf-slnt-test/
>
* 🍞 **PASS** Looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gf_axisregistry/fvar_axis_defaults">com.google.fonts/check/gf_axisregistry/fvar_axis_defaults</a>)</summary><div>

>
>Check that axis defaults have a corresponding fallback name registered at the Google Fonts Axis Registry, available at https://github.com/google/fonts/tree/main/axisregistry
>
>This is necessary for the following reasons:
>
>To get ZIP files downloads on Google Fonts to be accurate — otherwise the chosen default font is not generated. The Newsreader family, for instance, has a default value on the 'opsz' axis of 16pt. If 16pt was not a registered fallback position, then the ZIP file would instead include another position as default (such as 14pt).
>
>For the Variable fonts to display the correct location on the specimen page.
>
>For VF with no weight axis to be displayed at all. For instance, Ballet, which has no weight axis, was not appearing in sandbox because default position on 'opsz' axis was 16pt, and it was not yet a registered fallback positon.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT/gf_axisregistry">com.google.fonts/check/STAT/gf_axisregistry</a>)</summary><div>

>
>Check that particle names and values on STAT table match the fallback names in each axis entry at the Google Fonts Axis Registry, available at https://github.com/google/fonts/tree/main/axisregistry
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Check small caps glyphs are available. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/missing_small_caps_glyphs">com.google.fonts/check/missing_small_caps_glyphs</a>)</summary><div>

>
>Ensure small caps glyphs are available if a font declares smcp or c2sc OT features.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>

>
>Stylistic sets should provide description text. Programs such as InDesign, TextEdit and Inkscape use that info to display to the users so that they know what a given stylistic set offers.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>

>
>All fonts on the Google Fonts collection should have OS/2.fsSelection bit 7 (USE_TYPO_METRICS) set. This requirement is part of the vertical metrics scheme established as a Google Fonts policy aiming at a common ground supported by all major font rendering environments.
>
>For more details, read: https://github.com/googlefonts/gf-docs/blob/main/VerticalMetrics/README.md
>
>Below is the portion of that document that is most relevant to this check:
>
>Use_Typo_Metrics must be enabled. This will force MS Applications to use the OS/2 Typo values instead of the Win values. By doing this, we can freely set the Win values to avoid clipping and control the line height with the typo values. It has the added benefit of future line height compatibility. When a new script is added, we simply change the Win values to the new yMin and yMax, without needing to worry if the line height have changed.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Ensure fonts do not contain any pre-production tables. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/no_debugging_tables">com.google.fonts/check/no_debugging_tables</a>)</summary><div>

>
>Tables such as `Debg` are useful in the pre-production stages of font development, but add unnecessary bloat to a production font and should be removed before release.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>

>
>A base expectation is that a font family's regular/default (400 roman) style can render its 'menu name' (nameID 1) in itself.
>
* 🍞 **PASS** Font can successfully render its own name (Handjet)
</div></details><details><summary>🍞 <b>PASS:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🍞 **PASS** No trailing spaces on name table entries.
</div></details><details><summary>🍞 <b>PASS:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🍞 **PASS** OS/2 usWinAscent & usWinDescent values look good!
</div></details><details><summary>🍞 <b>PASS:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>

>
>OS/2 and hhea vertical metric values should match. This will produce the same linespacing on Mac, GNU+Linux and Windows.
>
>- Mac OS X uses the hhea values.
>- Windows uses OS/2 or Win, depending on the OS or fsSelection bit value.
>
>When OS/2 and hhea vertical metrics match, the same linespacing results on macOS, GNU+Linux and Windows. Unfortunately as of 2018, Google Fonts has released many fonts with vertical metrics that don't match in this way. When we fix this issue in these existing families, we will create a visible change in line/paragraph layout for either Windows or macOS users, which will upset some of them.
>
>But we have a duty to fix broken stuff, and inconsistent paragraph layout is unacceptably broken when it is possible to avoid it.
>
>If users complain and prefer the old broken version, they have the freedom to take care of their own situation.
>
* 🍞 **PASS** OS/2.sTypoAscender/Descender values match hhea.ascent/descent.
</div></details><details><summary>🍞 <b>PASS:</b> Checking with ots-sanitize. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/ots">com.google.fonts/check/ots</a>)</summary><div>


* 🍞 **PASS** ots-sanitize passed this file
</div></details><details><summary>🍞 <b>PASS:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>

>
>Running old versions of FontBakery can lead to a poor report which may include false WARNs and FAILs due do bugs, as well as outdated quality assurance criteria.
>
>Older versions will also not report problems that are detected by new checks added to the tool in more recent updates.
>
* 🍞 **PASS** Font Bakery is up-to-date.
</div></details><details><summary>🍞 <b>PASS:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>

>
>The OpenType specification v1.8.2 recommends that the first glyph is the '.notdef' glyph without a codepoint assigned and with a drawing.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/recom#glyph-0-the-notdef-glyph
>
>Pre-v1.8, it was recommended that fonts should also contain 'space', 'CR' and '.null' glyphs. This might have been relevant for MacOS 9 applications.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🍞 **PASS** Font contains glyphs for whitespace characters.
</div></details><details><summary>🍞 <b>PASS:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>

>
>This check enforces adherence to recommended whitespace (codepoints 0020 and 00A0) glyph names according to the Adobe Glyph List.
>
* 🍞 **PASS** Font has **AGL recommended** names for whitespace glyphs.
</div></details><details><summary>🍞 <b>PASS:</b> Whitespace glyphs have ink? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_ink">com.google.fonts/check/whitespace_ink</a>)</summary><div>


* 🍞 **PASS** There is no whitespace glyph with ink.
</div></details><details><summary>🍞 <b>PASS:</b> Are there unwanted tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unwanted_tables">com.google.fonts/check/unwanted_tables</a>)</summary><div>

>
>Some font editors store source data in their own SFNT tables, and these can sometimes sneak into final release files, which should only have OpenType spec tables.
>
* 🍞 **PASS** There are no unwanted tables.
</div></details><details><summary>🍞 <b>PASS:</b> Check correctness of STAT table strings  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/STAT_strings">com.google.fonts/check/STAT_strings</a>)</summary><div>

>
>On the STAT table, the "Italic" keyword must not be used on AxisValues for variation axes other than 'ital'.
>
* 🍞 **PASS** Looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Font contains unique glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unique_glyphnames">com.google.fonts/check/unique_glyphnames</a>)</summary><div>

>
>Duplicate glyph names prevent font installation on Mac OS X.
>
* 🍞 **PASS** Font contains unique glyph names.
</div></details><details><summary>🍞 <b>PASS:</b> Checking with fontTools.ttx (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/ttx_roundtrip">com.google.fonts/check/ttx_roundtrip</a>)</summary><div>


* 🍞 **PASS** Hey! It all looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>

>
>Some families have glyphs which have been constructed by using transformed components e.g the 'u' being constructed from a flipped 'n'.
>
>From a designers point of view, this sounds like a win (less work). However, such approaches can lead to rasterization issues, such as having the 'u' not sitting on the baseline at certain sizes after running the font through ttfautohint.
>
>Other issues are outlines that end up reversed when only one dimension is flipped while the other isn't.
>
>As of July 2019, Marc Foley observed that ttfautohint assigns cvt values to transformed glyphs as if they are not transformed and the result is they render very badly, and that vttLib does not support flipped components.
>
>When building the font with fontmake, the problem can be fixed by adding this to the command line:
>
>--filter DecomposeTransformedComponentsFilter
>
* 🍞 **PASS** No glyphs had components with scaling or rotation
</div></details><details><summary>🍞 <b>PASS:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>

>
>The dotted circle character (U+25CC) is inserted by shaping engines before mark glyphs which do not have an associated base, especially in the context of broken syllabic clusters.
>
>For fonts containing combining marks, it is recommended that the dotted circle character be included so that these isolated marks can be displayed properly; for fonts supporting complex scripts, this should be considered mandatory.
>
>Additionally, when a dotted circle glyph is present, it should be able to display all marks correctly, meaning that it should contain anchors for all attaching marks.
>
* 🍞 **PASS** All marks were anchored to dotted circle
</div></details><details><summary>🍞 <b>PASS:</b> Ensure no GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/gpos7">com.google.fonts/check/gpos7</a>)</summary><div>

>
>Versions of fonttools >=4.14.0 (19 August 2020) perform an optimisation on chained contextual lookups, expressing GSUB6 as GSUB5 and GPOS8 and GPOS7 where possible (when there are no suffixes/prefixes for all rules in the lookup).
>
>However, makeotf has never generated these lookup types and they are rare in practice. Perhaps before of this, Mac's CoreText shaper does not correctly interpret GPOS7, meaning that these lookups will be ignored by the shaper, and fonts containing these lookups will have unintended positioning errors.
>
>To fix this warning, rebuild the font with a recent version of fonttools.
>
* 🍞 **PASS** Font has no GPOS7 lookups
</div></details><details><summary>🍞 <b>PASS:</b> Font has the proper sfntVersion value? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.adobe.fonts/check/sfnt_version">com.adobe.fonts/check/sfnt_version</a>)</summary><div>

>
>OpenType fonts that contain TrueType outlines should use the value of 0x00010000 for the sfntVersion. OpenType fonts containing CFF data (version 1 or 2) should use 0x4F54544F ('OTTO', when re-interpreted as a Tag) for sfntVersion.
>
>Fonts with the wrong sfntVersion value are rejected by FreeType.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/otff#table-directory
>
* 🍞 **PASS** Font has the correct sfntVersion value.
</div></details><details><summary>🍞 <b>PASS:</b> Space and non-breaking space have the same width? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_widths">com.google.fonts/check/whitespace_widths</a>)</summary><div>

>
>If the space and nbspace glyphs have different widths, then Google Workspace has problems with the font.
>
>The nbspace is used to replace the space character in multiple situations in documents; such as the space before punctuation in languages that do that. It avoids the punctuation to be separated from the last word and go to next line.
>
>This is automatic substitution by the text editors, not by fonts. It is also used by designers in text composition practice to create nicely shaped paragraphs. If the space and the nbspace are not the same width, it breaks the text composition of documents.
>
* 🍞 **PASS** Space and non-breaking space have the same width.
</div></details><details><summary>🍞 <b>PASS:</b> Check all glyphs have codepoints assigned. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cmap.html#com.google.fonts/check/all_glyphs_have_codepoints">com.google.fonts/check/all_glyphs_have_codepoints</a>)</summary><div>


* 🍞 **PASS** All glyphs have a codepoint value assigned.
</div></details><details><summary>🍞 <b>PASS:</b> Checking font version fields (head and name table). (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/font_version">com.google.fonts/check/font_version</a>)</summary><div>


* 🍞 **PASS** All font version fields match.
</div></details><details><summary>🍞 <b>PASS:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* 🍞 **PASS** OS/2 xAvgCharWidth value is correct.
</div></details><details><summary>🍞 <b>PASS:</b> Check if OS/2 fsSelection matches head macStyle bold and italic bits. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.adobe.fonts/check/fsselection_matches_macstyle">com.adobe.fonts/check/fsselection_matches_macstyle</a>)</summary><div>

>
>The bold and italic bits in OS/2.fsSelection must match the bold and italic bits in head.macStyle per the OpenType spec.
>
* 🍞 **PASS** The OS/2.fsSelection and head.macStyle bold and italic settings match.
</div></details><details><summary>🍞 <b>PASS:</b> Check code page character ranges (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/code_pages">com.google.fonts/check/code_pages</a>)</summary><div>

>
>At least some programs (such as Word and Sublime Text) under Windows 7 do not recognize fonts unless code page bits are properly set on the ulCodePageRange1 (and/or ulCodePageRange2) fields of the OS/2 table.
>
>More specifically, the fonts are selectable in the font menu, but whichever Windows API these applications use considers them unsuitable for any character set, so anything set in these fonts is rendered with Arial as a fallback font.
>
>This check currently does not identify which code pages should be set. Auto-detecting coverage is not trivial since the OpenType specification leaves the interpretation of whether a given code page is "functional" or not open to the font developer to decide.
>
>So here we simply detect as a FAIL when a given font has no code page declared at all.
>
* 🍞 **PASS** At least one code page is defined.
</div></details><details><summary>🍞 <b>PASS:</b> Font has correct post table version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/post_table_version">com.google.fonts/check/post_table_version</a>)</summary><div>

>
>Format 2.5 of the 'post' table was deprecated in OpenType 1.3 and should not be used.
>
>According to Thomas Phinney, the possible problem with post format 3 is that under the right combination of circumstances, one can generate PDF from a font with a post format 3 table, and not have accurate backing store for any text that has non-default glyphs for a given codepoint.
>
>It will look fine but not be searchable. This can affect Latin text with high-end typography, and some complex script writing systems, especially with higher-quality fonts. Those circumstances generally involve creating a PDF by first printing a PostScript stream to disk, and then creating a PDF from that stream without reference to the original source document. There are some workflows where this applies,but these are not common use cases.
>
>Apple recommends against use of post format version 4 as "no longer necessary and should be avoided". Please see the Apple TrueType reference documentation for additional details.
>
>https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6post.html
>
>Acceptable post format versions are 2 and 3 for TTF and OTF CFF2 builds, and post format 3 for CFF builds.
>
* 🍞 **PASS** Font has an acceptable post format 2.0 table version.
</div></details><details><summary>🍞 <b>PASS:</b> Check name table for empty records. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/name/empty_records">com.adobe.fonts/check/name/empty_records</a>)</summary><div>

>
>Check the name table for empty records, as this can cause problems in Adobe apps.
>
* 🍞 **PASS** No empty name table records found.
</div></details><details><summary>🍞 <b>PASS:</b> Description strings in the name table must not contain copyright info. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description">com.google.fonts/check/name/no_copyright_on_description</a>)</summary><div>


* 🍞 **PASS** Description strings in the name table do not contain any copyright string.
</div></details><details><summary>🍞 <b>PASS:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>

>
>There are various metadata in the OpenType spec to specify if a font is monospaced or not. If the font is not truly monospaced, then no monospaced metadata should be set (as sometimes they mistakenly are...)
>
>Requirements for monospace fonts:
>
>* post.isFixedPitch - "Set to 0 if the font is proportionally spaced, non-zero if the font is not proportionally spaced (monospaced)" (https://www.microsoft.com/typography/otspec/post.htm)
>
>* hhea.advanceWidthMax must be correct, meaning no glyph's width value is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
>
>* OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
>
>* OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written or latin symbol fonts.
>
>* Spec says: "The PANOSE definition contains ten digits each of which currently describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font mapper to determine family type. It also uses bProportion to determine if the font is monospaced." (https://www.microsoft.com/typography/otspec/os2.htm#pan https://monotypecom-test.monotype.de/services/pan2)
>
>* OS/2.xAvgCharWidth must be set accurately. "OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by Windows GDI" (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
>
>Also we should report an error for glyphs not of average width.
>
>Please also note:
>
>Thomas Phinney told us that a few years ago (as of December 2019), if you gave a font a monospace flag in Panose, Microsoft Word would ignore the actual advance widths and treat it as monospaced.
>
>Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
>
* 🍞 **PASS** Font is not monospaced and all related metadata look good. [code: good]
</div></details><details><summary>🍞 <b>PASS:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>

>
>The FULL_FONT_NAME entry in the ‘name’ table should start with the same string as the Family Name (FONT_FAMILY_NAME, TYPOGRAPHIC_FAMILY_NAME or WWS_FAMILY_NAME).
>
>If the Family Name is not included as the first part of the Full Font Name, and the user embeds the font in a document using a Microsoft Office app, the app will fail to render the font when it opens the document again.
>
>NOTE: Up until version 1.5, the OpenType spec included the following exception in the definition of Full Font Name:
>
>"An exception to the [above] definition of Full font name is for Microsoft platform strings for CFF OpenType fonts: in this case, the Full font name string must be identical to the PostScript FontName in the CFF Name INDEX."
>
>https://docs.microsoft.com/en-us/typography/opentype/otspec150/name#name-ids
>
* 🍞 **PASS** Full font name begins with the font family name.
</div></details><details><summary>🍞 <b>PASS:</b> Font follows the family naming recommendations? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/family_naming_recommendations">com.google.fonts/check/family_naming_recommendations</a>)</summary><div>


* 🍞 **PASS** Font follows the family naming recommendations.
</div></details><details><summary>🍞 <b>PASS:</b> Name table ID 6 (PostScript name) must be consistent across platforms. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_name_consistency">com.adobe.fonts/check/name/postscript_name_consistency</a>)</summary><div>

>
>The PostScript name entries in the font's 'name' table should be consistent across platforms.
>
>This is the TTF/CFF2 equivalent of the CFF 'name/postscript_vs_cff' check.
>
* 🍞 **PASS** Entries in the "name" table for ID 6 (PostScript name) are consistent.
</div></details><details><summary>🍞 <b>PASS:</b> Does the number of glyphs in the loca table match the maxp table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/loca.html#com.google.fonts/check/loca/maxp_num_glyphs">com.google.fonts/check/loca/maxp_num_glyphs</a>)</summary><div>


* 🍞 **PASS** 'loca' table matches numGlyphs in 'maxp' table.
</div></details><details><summary>🍞 <b>PASS:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* 🍞 **PASS** OS/2 sTypoLineGap and hhea lineGap are both 0.
</div></details><details><summary>🍞 <b>PASS:</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/maxadvancewidth">com.google.fonts/check/maxadvancewidth</a>)</summary><div>


* 🍞 **PASS** MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables.
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have a DSIG table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig">com.google.fonts/check/dsig</a>)</summary><div>

>
>Microsoft Office 2013 and below products expect fonts to have a digital signature declared in a DSIG table in order to implement OpenType features. The EOL date for Microsoft Office 2013 products is 4/11/2023. This issue does not impact Microsoft Office 2016 and above products.
>
>As we approach the EOL date, it is now considered better to completely remove the table.
>
>But if you still want your font to support OpenType features on Office 2013, then you may find it handy to add a fake signature on a placeholder DSIG table by running one of the helper scripts provided at https://github.com/googlefonts/gftools
>
>Reference: https://github.com/googlefonts/fontbakery/issues/1845
>
* 🍞 **PASS** ok
</div></details><details><summary>🍞 <b>PASS:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* 🍞 **PASS** Font does not has spacing glyphs in the GDEF mark glyph class.
</div></details><details><summary>🍞 <b>PASS:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>

>
>Mark characters should be in the GDEF mark glyph class.
>
* 🍞 **PASS** Font does not have mark characters not in the GDEF mark glyph class.
</div></details><details><summary>🍞 <b>PASS:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned if they have mark anchors.
>
>Only combining mark glyphs should be in that class. Any non-mark glyph must not be in that class, in particular spacing glyphs.
>
* 🍞 **PASS** Font does not have non-mark characters in the GDEF mark glyph class.
</div></details><details><summary>🍞 <b>PASS:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* 🍞 **PASS** GPOS table check for kerning information passed.
</div></details><details><summary>🍞 <b>PASS:</b> Is there a usable "kern" table declared in the font? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/kern.html#com.google.fonts/check/kern_table">com.google.fonts/check/kern_table</a>)</summary><div>

>
>Even though all fonts should have their kerning implemented in the GPOS table, there may be kerning info at the kern table as well.
>
>Some applications such as MS PowerPoint require kerning info on the kern table. More specifically, they require a format 0 kern subtable from a kern table version 0 with only glyphs defined in the cmap table, which is the only one that Windows understands (and which is also the simplest and more limited of all the kern subtables).
>
>Google Fonts ingests fonts made for download and use on desktops, and does all web font optimizations in the serving pipeline (using libre libraries that anyone can replicate.)
>
>Ideally, TTFs intended for desktop users (and thus the ones intended for Google Fonts) should have both KERN and GPOS tables.
>
>Given all of the above, we currently treat kerning on a v0 kern table as a good-to-have (but optional) feature.
>
* 🍞 **PASS** Font does not declare an optional "kern" table.
</div></details><details><summary>🍞 <b>PASS:</b> Is there any unused data at the end of the glyf table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_unused_data">com.google.fonts/check/glyf_unused_data</a>)</summary><div>


* 🍞 **PASS** There is no unused data at the end of the glyf table.
</div></details><details><summary>🍞 <b>PASS:</b> Check for points out of bounds. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds">com.google.fonts/check/points_out_of_bounds</a>)</summary><div>


* 🍞 **PASS** All glyph paths have coordinates within bounds!
</div></details><details><summary>🍞 <b>PASS:</b> Check glyphs do not have duplicate components which have the same x,y coordinates. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components">com.google.fonts/check/glyf_non_transformed_duplicate_components</a>)</summary><div>

>
>There have been cases in which fonts had faulty double quote marks, with each of them containing two single quote marks as components with the same x, y coordinates which makes them visually look like single quote marks.
>
>This check ensures that glyphs do not contain duplicate components which have the same x,y coordinates.
>
* 🍞 **PASS** Glyphs do not contain duplicate components which have the same x,y coordinates.
</div></details><details><summary>🍞 <b>PASS:</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wght_coord">com.google.fonts/check/varfont/regular_wght_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wght' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
>
>If a variable font has a 'wght' (Weight) axis, then the coordinate of its 'Regular' instance is required to be 400.
>
* 🍞 **PASS** Regular:wght is 400.
</div></details><details><summary>🍞 <b>PASS:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/bold_wght_coord">com.google.fonts/check/varfont/bold_wght_coord</a>)</summary><div>

>
>The Open-Type spec's registered design-variation tag 'wght' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght does not specify a required value for the 'Bold' instance of a variable font.
>
>But Dave Crossland suggested that we should enforce a required value of 700 in this case.
>
* 🍞 **PASS** Bold:wght is 700.
</div></details><details><summary>🍞 <b>PASS:</b> The variable font 'wght' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wght_valid_range">com.google.fonts/check/varfont/wght_valid_range</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wght' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
>
>On the 'wght' (Weight) axis, the valid coordinate range is 1-1000.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Validates that the value of axisNameID used by each VariationAxisRecord is greater than 255 and less than 32768. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_axis_nameid">com.adobe.fonts/check/varfont/valid_axis_nameid</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The axisNameID field provides a name ID that can be used to obtain strings from the 'name' table that can be used to refer to the axis in application user interfaces. The name ID must be greater than 255 and less than 32768.
>
* 🍞 **PASS** All axisNameID values are valid.
</div></details><details><summary>🍞 <b>PASS:</b> Validates that the value of subfamilyNameID used by each InstanceRecord is 2, 17, or greater than 255 and less than 32768. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_subfamily_nameid">com.adobe.fonts/check/varfont/valid_subfamily_nameid</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The subfamilyNameID field provides a name ID that can be used to obtain strings from the 'name' table that can be treated as equivalent to name ID 17 (typographic subfamily) strings for the given instance. Values of 2 or 17 can be used; otherwise, values must be greater than 255 and less than 32768.
>
* 🍞 **PASS** All subfamilyNameID values are valid.
</div></details><details><summary>🍞 <b>PASS:</b> Validates that the value of postScriptNameID used by each InstanceRecord is 6, 0xFFFF, or greater than 255 and less than 32768. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_postscript_nameid">com.adobe.fonts/check/varfont/valid_postscript_nameid</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The postScriptNameID field provides a name ID that can be used to obtain strings from the 'name' table that can be treated as equivalent to name ID 6 (PostScript name) strings for the given instance. Values of 6 and 0xFFFF can be used; otherwise, values must be greater than 255 and less than 32768.
>
* 🍞 **PASS** All postScriptNameID values are valid.
</div></details><details><summary>🍞 <b>PASS:</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to either 2 or 17 (or something with the same value as 2), and its postScriptNameID value is set to 6 (or something with the same value as 6). (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_default_instance_nameids">com.adobe.fonts/check/varfont/valid_default_instance_nameids</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9.1 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The default instance of a font is that instance for which the coordinate value of each axis is the defaultValue specified in the corresponding variation axis record. An instance record is not required for the default instance, though an instance record can be provided. When enumerating named instances, the default instance should be enumerated even if there is no corresponding instance record. If an instance record is included for the default instance (that is, an instance record has coordinates set to default values), then the nameID value should be set to either 2 or 17  or to a name ID with the same value as name ID 2. Also, if a postScriptNameID is included in instance records, and the postScriptNameID value should be set to 6 or to a name ID with the same value as name ID 6.
>
* 🍞 **PASS** All default instance nameID values are valid.
</div></details><details><summary>🍞 <b>PASS:</b> Validates that all of the instance records in a given font have the same size. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/same_size_instance_records">com.adobe.fonts/check/varfont/same_size_instance_records</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>All of the instance records in a given font must be the same size, with all either including or omitting the postScriptNameID field. [...] If the value is 0xFFFF, then the value is ignored, and no PostScript name equivalent is provided for the instance.
>
* 🍞 **PASS** All instance records have the same size.
</div></details><details><summary>🍞 <b>PASS:</b> Validates that all of the instance records in a given font have distinct data. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/distinct_instance_records">com.adobe.fonts/check/varfont/distinct_instance_records</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>All of the instance records in a font should have distinct coordinates and distinct subfamilyNameID and postScriptName ID values. If two or more records share the same coordinates, the same nameID values or the same postScriptNameID values, then all but the first can be ignored.
>
* 🍞 **PASS** All instance records are distinct.
</div></details><details><summary>🍞 <b>PASS:</b> All fvar axes have a correspondent Axis Record on STAT table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/stat.html#com.google.fonts/check/varfont/stat_axis_record_for_each_axis">com.google.fonts/check/varfont/stat_axis_record_for_each_axis</a>)</summary><div>

>
>According to the OpenType spec, there must be an Axis Record for every axis defined in the fvar table.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-records
>
* 🍞 **PASS** STAT table has all necessary Axis Records.
</div></details><details><summary>🍞 <b>PASS:</b> STAT table has Axis Value tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/stat.html#com.adobe.fonts/check/stat_has_axis_value_tables">com.adobe.fonts/check/stat_has_axis_value_tables</a>)</summary><div>

>
>According to the OpenType spec, in a variable font, it is strongly recommended that axis value tables be included for every element of typographic subfamily names for all of the named instances defined in the 'fvar' table.
>
>Axis value tables are particularly important for variable fonts, but can also be used in non-variable fonts. When used in non-variable fonts, axis value tables for particular values should be implemented consistently across fonts in the family.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-value-tables
>
* 🍞 **PASS** STAT table has Axis Value tables.
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have any invalid feature tags? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/layout.html#com.google.fonts/check/layout_valid_feature_tags">com.google.fonts/check/layout_valid_feature_tags</a>)</summary><div>

>
>Incorrect tags can be indications of typos, leftover debugging code or questionable approaches, or user error in the font editor. Such typos can cause features and language support to fail to work as intended.
>
* 🍞 **PASS** No invalid feature tags were found
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have any invalid script tags? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/layout.html#com.google.fonts/check/layout_valid_script_tags">com.google.fonts/check/layout_valid_script_tags</a>)</summary><div>

>
>Incorrect script tags can be indications of typos, leftover debugging code or questionable approaches, or user error in the font editor. Such typos can cause features and language support to fail to work as intended.
>
* 🍞 **PASS** No invalid script tags were found
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have any invalid language tags? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/layout.html#com.google.fonts/check/layout_valid_language_tags">com.google.fonts/check/layout_valid_language_tags</a>)</summary><div>

>
>Incorrect language tags can be indications of typos, leftover debugging code or questionable approaches, or user error in the font editor. Such typos can cause features and language support to fail to work as intended.
>
* 🍞 **PASS** No invalid language tags were found
</div></details><details><summary>🍞 <b>PASS:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>

>
>This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
>
>Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.
>
* 🍞 **PASS** Y-coordinates of points fell on appropriate boundaries.
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 5 | 5 | 100 | 8 | 109 | 0 |
| 0% | 2% | 2% | 44% | 4% | 48% | 0% |
