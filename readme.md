# hugo-theme-cistercian

> Can I just say that I love that you made an open-source plugin, and publicized it, for probably one of the most niche applications I have ever seen in my life.

- pelican_chorus on Reddit

A small utility theme for displaying Cistercian numerals in Hugo.

See the `exampleSite` deployed at <https://pages.micahrl.com/hugo-theme-cistercian>.
Here is a screenshot:

[![screenshot](/images/tn.png)](/images/screenshot.png)

## About Cistercian numerals

[Cistercian numerals](https://en.wikipedia.org/wiki/Cistercian_numerals) are an archaic way of writing numbers originating in the thirteenth century.

I've also written a React component for converting from decimal numbers, which can be used interactively at <https://cistercian.micahrl.com>.

Cistercian numerals are not found in Unicode, and the [FRBCistercian font](https://github.com/ctrlcctrlv/FRBCistercian) that displays them places the glyphs in a [private use area](https://en.wikipedia.org/wiki/Private_Use_Areas). This means that the characters can be copied to the clipboard, but pasting them elsewhere will not make sense in any context unless FRBCistercian is used to display them.
To use FRBCistercian, we must calculate an offset from the font's base digit for the ones, tens, hundreds, and thousands place. We do this in the [`cistercian.html` partial](layouts/partials/cistercian.html).

## How to use it

You can now use this theme as a `go` module.
This saves a step over the old git submodule method.

### 1. Add the theme to your theme list

(See [Hugo's configuration documentation](https://gohugo.io/getting-started/configuration/).)

```toml
[module]
[[module.imports]]
path = "github.com/mrled/hugo-theme-cistercian"
```

### 2. Add the theme's head partial to the `<head>` element

You can do this site-wide if you like, or just for the `<head>` of any page which will display Cistercian numerals. (Typically you'll need to do this in your site's theme somehow.)

This gets the font files, some very light CSS that is only used for displaying the numerals, and sets a JavaScript function for toggling annotations on annotatable numerals.

```go-html-template
<head>
...
  {{ partial "cistercian.head.html" . }}
</head>
```

### 3. Use the theme's shortcodes in your page content

Now you can use the shortcodes defined in the theme in your page content.
The `num` parameter is required, and `annotatable` is `false` by default.

```go-html-template
{{< cistercianContainer num="1985" annotatable=true >}}
```

There is special support for displaying YYYY MMDD HHMM datetimestamps.
The `date` parameter is required, `annotatable` is `false` by default,
and `showdate` and `showtime` are both `true` by default
and control showing the YYYY MMDD and HHMM components of the datestamp respectively.

```go-html-template
{{< cistercianDate date="2021-10-29T11:39:00" annotatable=true showdate=true showtime=true >}}
```

You can control annotations with an included checkbox:

```go-html-template
{{< cistercianToggleAnnotationsControl >}}
```

You can also convert a 1-4 digit decimal number to a dict containing Cistercian bytes:

```go-html-template
{{ $cisterciaBirthYYYY := partial "cistercianRaw.html" 1985 }}

{{/*-----------------------------------------------------------------------------------------------
----Given a 1-4 digit decimal number,
----return a dict with the following properties:
----  input:            the original input, unmodified (either an int or a string)
----  cistercianBytes:  a string containing Unicode codepoints suitable for FRBCistercian font
----  decimal:          the original decimal number, as an integer (even if passed a string), with leading zeroes trimmed
----  thousands:        the thousands place in decimal
----  hundreds:         the hundreds place in decimal
----  tens:             the tens place in decimal
----  ones:             the ones place in decimal
----*/}}

{{ $birthCistercianBytes := index $cisterciaBirthYYYY "cistercianBytes" }}
{{ $birthDecimal := index $cisterciaBirthYYYY "decimal" }}
{{/* ...etc */}}
```

### 4. Use the theme's partials in your own layout

There is a corresponding partial for each shortcode listed above, which can be used in your site's layout (e.g. under `layouts/index.html` in your site's repo). This is useful if you want to include Cistercian in your site's templates.

They work mostly the same as the shortcodes above,
using `dict`s to pass arguments. For instance:

```go-html-template
{{ partial "cistercianContainer.html" (dict "num" $num "annotatable" $annotatable) }}
{{ partial "cistercianDate.html" (dict "date" $date "showdate" $showdate "showtime" $showtime "annotatable" $annotatable) }}
```

### 5. Style the elements to your liking

The CSS classes and HTML element IDs are prefixed with `hugo-theme-cistercian-`, so you can add or override the (very light) included styles as you please.

The annotations toggling button requires some JavaScript.

Both are in [cistercian.head.html](layouts/partials/cistercian.head.html). See that file for details.

Note that you should not add styles to the `hugo-theme-cistercian-font-frbcistercian` class, which is the class for the `<span>` element containing the actual Cistercian Unicode codepoints found in the `cistercian.html` partial. If you apply the `font-size` style to that class and use annotations, Firefox will display the annotations overlaid over the center of the Cistercian character. (Chrome does not exhibit this behavior.) You should avoid using the `cistercian.html` partial directly, instead use `cistercianAnnotated.html` and `cistercianUnannotated.html` partials, and style the `hugo-theme-cistercian-container` class which contains the Cistercian numeral's parent element and, if annotated, child `<rt>` and `<rp>` elements. These elements are styled in the `cistercian.head.html` partial and you could modify or override this for your own site.
