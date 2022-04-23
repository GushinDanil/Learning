import html

print(html.escape("This HTML fragment <p>contains</p> a <script>script</script> tag."))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))