function HugoThemeCistercian_ToggleAnnotations() {
  const numerals = document.getElementsByClassName("hugo-theme-cistercian-annotatable");
  Array.prototype.forEach.call(numerals, function(numeral) {
    const rts = numeral.getElementsByTagName("rt");
    const rps = numeral.getElementsByTagName("rp");
    // This is a little weird because getElementsByTagName() does not return an array
    // <https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection>
    [rts, rps].forEach(function(collection) {
      Array.prototype.forEach.call(collection, function(childElem) {
        childElem.classList.toggle("hugo-theme-cistercian-label-hidden");
      })
    })
  })
}

window.HugoThemeCistercian_ToggleAnnotations = HugoThemeCistercian_ToggleAnnotations;
