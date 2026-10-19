---
gists:
  - id: 7e30eb9387482eee8eb9db966dbc686f
    url: 'https://gist.github.com/LikeACodingStone/7e30eb9387482eee8eb9db966dbc686f'
    createdAt: '2026-09-25T09:17:36Z'
    updatedAt: '2026-10-16T05:35:27Z'
    filename: 000_Markdown_Grammer.md
    isPublic: true
    baseUrl: 'https://api.github.com'
---
# Markdown Quick Reference

| Purpose          | Markdown                                                     | Example     |
| ---------------- | ------------------------------------------------------------ | ----------- |
| Bold             | `**text**`                                                   | **text**    |
| Italic           | `*text*`                                                     | *text*      |
| Bold + Italic    | `***text***`                                                 | ***text***  |
| Strikethrough    | `~~text~~`                                                   | ~~text~~    |
| Link             | `[text](URL)`                                                | [text](URL) |
| Image            | `![alt](URL)`                                                | Image       |
| Nested list      | `  - item`                                                   | ↳ item      |
| Task unchecked   | `- [ ] task`                                                 | ☐ task      |
| Task checked     | `- [x] task`                                                 | ☑ task      |
| Horizontal line  | `---`                                                        | —           |
| Bash code        | ```` ```bash ````                                            | Bash code   |
| Table            | `\| A \| B \|`                                               | Table       |
| Table separator  | `\|---\|---\|`                                               | —           |
| Left align       | `:---`                                                       | Left        |
| Center align     | `:---:`                                                      | Center      |
| Right align      | `---:`                                                       | Right       |
| Line break       | `  `                                                         | New line    |
| HTML line break  | `<br>`                                                       | New line    |
| Escape character | `\*`                                                         | *           |
| Footnote         | `[^1]`                                                       | Footnote    |
| Footnote text    | `[^1]: text`                                                 | —           |
| HTML comment     | `<!-- text -->`                                              | Hidden      |
| Collapsible      | `<details>...</details>`                                     | Expandable  |
| HTML colour      | <span style="color: red;">红色文字</span>                        | Red         |
| HTML colour      | <span style="color: #00AAFF;">蓝色文字</span>                    | Blue        |
| HTML colour      | <span style="color: green; font-weight: bold;">绿色加粗文字</span> | Green       |

[A_14_Kernel6.1_Download] (https://rb-cmbinex-fe-p1.de.bosch.com/artifactory/rnm-ccs2.0/bosch/deployment/android_a14/)
## Table Template

| Name   | Description | Example   |
| ------ | ----------- | --------- |
| Item 1 | Description | `example` |
| Item 2 | Description | `example` |

```markdown
| Name | Description | Example |
|---|---|---|
| Item 1 | Description | `example` |
| Item 2 | Description | `example` |
```

## Task List
- [ ] Todo
- [x] Done
```
- [ ] Todo 
- [x] Done
```

## Code Block
```cpp
your code here
````

````

```cpp
your code here
```
````

### Block
<div style="border: 1px solid #999; padding: 12px; border-radius: 6px;">
这里是方框内部的内容。
可以写多行，也可以使用其他 HTML 标签。`<br>`
<-div style="border: 1px solid #999; padding: 12px; border-radius: 6px;">`<br>`
<-/div>

</div>
