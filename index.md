---
title: Test Page
---
{% raw %}
<script type="text/javascript">
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  },
  svg: { fontCache: 'global' },
  startup: {
    pageReady: () => {
      return MathJax.startup.defaultPageReady().then(() => {
        MathJax.typesetPromise(); // ensure all math is rendered
      });
    }
  }
};
</script>

<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
{% endraw %}

# Welcome to My Page

Here’s some inline math: $E = mc^2$  

And a display equation:

$$
\int_0^\infty e^{-x} dx = 1
$$

