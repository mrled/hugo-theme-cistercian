# hugo-theme-cistercian

A small utility theme for displaying Cistercian numerals in Hugo.

Here's a screenshot of how it is used in your site content:

[![screenshot](/images/tn.png)](/images/screenshot.png)

See live examples at <https://me.micahrl.com/blog/hugo-theme-cistercian>.

## How to use it

### 1. Clone the theme into `themes/cistercian` in your site repo.

```sh
git submodule add https://github.com/mrled/hugo-themes-cistercian themes/cistercian
```

### 2. Add the theme to your theme list.

If your site config is YAML:

```yaml
theme:
- cistercian
- your-theme-here
```

Or if it's TOML:

```toml
theme = ["cistercian", "your-theme-here"]
```

### 3. Add the theme's head partial to the `<head>` element

You can do this site-wide if you like, or just for the `<head>` of any page which will display Cistercian numerals. (Typically you'll need to do this in your site's theme somehow.)

```go-html-template
<head>
...
  {{ partial "cistercian.head.html" . }}
</head>
```

### 4. Use the theme's shortcodes in your page content

Now you can use the shortcodes defined in the theme in your page content.

You can show annotated numerals:

```go-html-template
{{< cistercianAnnotated "420" >}}
```

Or unannotated ones:

```go-html-template
{{< cistercian "420" >}}
```

And there is special support for supporting (annotated) YYYY MMDD HHMM datetimestamps:

```go-html-template
{{< cistercianDate "2021-10-29T11:39:00" >}}
```

You can control annotations with an included checkbox:

```go-html-template
{{< cistercianToggleAnnotationsControl >}}
```

### 5. Use the theme's partials in your own layout

There is a corresponding partial for each shortcode listed above, which can be used in your site's layout (e.g. under `layouts/index.html` in your site's repo). This is useful if you want to include Cistercian in your site's templates.

They work mostly the same as the shortcodes above. For instance:

```go-html-template
{{ partial "cistercian.html" "420" }}
```

### 6. Style the elements to your liking

The CSS classes and HTML element IDs are prefixed with `hugo-theme-cistercian-`, so you can add or override the (very light) included styles as you please.

The annotations toggling button requires some JavaScript.

Both are in [cistercian.head.html](layouts/partials/cistercian.head.html). See that file for details.
