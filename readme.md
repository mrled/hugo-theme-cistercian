# hugo-theme-cistercian

> Can I just say that I love that you made an open-source plugin, and publicized it, for probably one of the most niche applications I have ever seen in my life.

- pelican_chorus on Reddit

A small utility theme for displaying Cistercian numerals in Hugo.

Here's a screenshot of how it is used in your site content:

[![screenshot](/images/tn.png)](/images/screenshot.png)

See the `exampleSite` deployed at <https://pages.micahrl.com/hugo-theme-cistercian>.

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
