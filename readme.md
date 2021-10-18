# hugo-theme-cistercian

A small utility theme for displaying Cistercian numerals in Hugo.

Here's a screenshot of the rendered example (blue background is optional):

![screenshot](rendered-example.png)

See live examples at <https://me.micahrl.com/blog/hugo-theme-cistercian>.

## How to use it

First, clone the theme into `themes/cistercian` in your site repo.

Second, this theme to your theme list.
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

Third, add the theme's head partial to the `<head>` element of any page which should display Cistercian numerals. (Typically you'll need to do this in your site's theme somehow.)

```go-html-template
<head>
...
  {{ partial "cistercian.head.html" . }}
</head>
```

Now you can use the partials defined in the theme in your page content.

```go-html-template
You can show annotated numerals:

{{< cistercianAnnotated "420" >}}

Or unannotated ones:

{{< cistercian "420" >}}

And there is special support for supporting (annotated) YYYY MMDD HHMM datetimestamps:

{{< cistercianPostDate "2021-10-29T11:39:00" >}}

You can control annotations with an included checkbox:

{{< cistercianToggleAnnotationsControl >}}
```
