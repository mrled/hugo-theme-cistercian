+++
title = "Cistercian Example Site"
+++

`hugo-theme-cistercian` is a utility theme for displaying
[Cistercian numerals](https://cistercian.micahrl.com).
[See the code on GitHub](https://github.com/mrled/hugo-theme-cistercian).

It's not designed to be your site's main theme,
it only concerns itself with displaying the numerals,
and doesn't affect the rest of your styles.

## How it looks

In all examples, I use a div with lightblue background to show what the Hugo partial prints to the page.

You can show annotatable numerals, with the decimal values visible above the Cistercian numerals:

```go-html-template
<div style="background: lightblue; padding: 1em;">
{{</* cistercian/cistercianContainer num="1985" annotatable=true */>}}
</div>
```

<div style="background: lightblue; padding: 1em;">
{{< cistercian/cistercianContainer num="1985" annotatable=true >}}
</div>

You can control annotations with an included button. This button works on this page and will toggle the annotations on/off!

```go-html-template
<div style="background: lightblue; padding: 1em;">
{{</* cistercian/cistercianToggleAnnotationsControl */>}}
</div>
```

<div style="background: lightblue; padding: 1em;">
{{< cistercian/cistercianToggleAnnotationsControl >}}
</div>

You can also display unannotatable numerals that never show annotations no matter the state of the button toggle:

```go-html-template
<div style="background: lightblue; padding: 1em;">
{{</* cistercian/cistercianContainer num="1985" annotatable=false */>}}
</div>
```

<div style="background: lightblue; padding: 1em;">
{{< cistercian/cistercianContainer num="1985" annotatable=false >}}
</div>

And there is special support for supporting YYYY MMDD HHMM datetimestamps
(with or without `annotatable=`):

```go-html-template
<div style="background: lightblue; padding: 1em;">
{{</* cistercian/cistercianDate date="2021-10-29T11:39:00" */>}}
</div>
```

<div style="background: lightblue; padding: 1em;">
{{< cistercian/cistercianDate date="2021-10-29T11:39:00" >}}
</div>

## Test cases

To make sure that everything renders properly, this page includes some test cases.

<table id="cistercian-theme-tests">
  <thead>
    <tr>
      <th>Cistercian</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{{< cistercian/cistercianContainer num="6969" >}}</td>
      <td>Cistercian container basic test, number as string</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianContainer num=6969 >}}</td>
      <td>Cistercian container basic test, number as int</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianContainer num=6969 annotatable=true >}}</td>
      <td>Cistercian container basic test, annotatable</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianContainer num=6969 annotatable=false >}}</td>
      <td>Cistercian container basic test, not annotatable</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianDate date="2021-10-29T11:39:00" >}}</td>
      <td>Cistercian date with a date + time stamp of "2021-10-29T11:39:00"</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianDate date="2021-10-29T11:39:00" showdate=false showtime=true >}}</td>
      <td>Cistercian date with a date + time stamp of "2021-10-29T11:39:00", not showing the date, showing the time</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianDate date="2021-10-29T11:39:00" showdate=true showtime=false >}}</td>
      <td>Cistercian date with a date + time stamp of "2021-10-29T11:39:00", not showing the time, showing the date</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianDate date="2021-10-29T11:39:00" annotatable=true >}}</td>
      <td>Cistercian date, annotatable</td>
    </tr>
    <tr>
      <td>{{< cistercian/cistercianDate date="2021-10-29T11:39:00" annotatable=false >}}</td>
      <td>Cistercian date, not annotatable</td>
    </tr>
  </tbody>
</table>
