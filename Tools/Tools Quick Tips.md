---
tags: [tools, tips, jdk, chrome, audacity, word]
updated: 2026-11-04
---
# Tools Quick Tips

> [!summary] Contents
> 1. JDK install pitfall + download links
> 2. Chrome can't get online
> 3. Audacity "another copy is running"
> 4. Word: can't add a next page

---

## 1. JDK

> [!warning] Install the JDK and the JRE in **different** folders
> The (older) installer asks for two paths: first the JDK, then the JRE. If both are the same, the JRE **overwrites** the JDK's files, and afterwards `tools.jar` and `dt.jar` are missing.
>
> Mostly an old-installer problem (JDK 8 and earlier).

**Archive downloads** (an Oracle account is needed):

| Version | Link |
|---|---|
| JDK 1.8 | https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html |
| JDK 1.7 | https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html |
| JDK 1.6 | https://www.oracle.com/java/technologies/javase-java-archive-javase6-downloads.html |

---

## 2. Chrome Can't Get Online

1. Search for **proxy** in Windows and turn the proxy **off**
2. Control Panel → **Internet Options → Content → Clear SSL state**

---

## 3. Audacity: "Another copy of Audacity is running"

> [!bug] Message
> `The system has detected that another copy of Audacity is running`

**Fix:** delete the Audacity lock file in `/var/tmp`.

```bash
ls -la /var/tmp        # find the lock file
```

---

## 4. Word: Can't Add a Next Page

> [!bug] Problem
> In a template-based document you can't add a next page.

1. `Ctrl + A` to select the whole page
2. `Ctrl + End` to move the cursor to the end
3. **Insert → Blank Page**
