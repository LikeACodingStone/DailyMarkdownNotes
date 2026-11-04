---
gists:
  - id: ea85fdbb22279def0882de0e8ac3fd76
    url: 'https://gist.github.com/LikeACodingStone/ea85fdbb22279def0882de0e8ac3fd76'
    createdAt: '2026-09-10T08:28:01Z'
    updatedAt: '2026-09-10T08:28:18Z'
    filename: README-Obsidian-GitHub-Gist.md
    isPublic: true
    baseUrl: 'https://api.github.com'
tags: [tools, obsidian, github, gist]
updated: 2026-11-04
---
# Obsidian + GitHub Gist Guide

> [!summary] Summary
> Share an Obsidian note as a GitHub Gist, and have the Gist update automatically whenever you edit the note.

```text
Obsidian note ── Share as Gist ──► GitHub Gist
      ▲                                │
      └── `gists` property (id + url) ◄┘
```

> [!danger] Never delete the `gists` property
> It is the link between the note and its Gist (id + url). Without it the plugin can't tell which Gist to update.

---

## 1. Create a GitHub Token

GitHub → Settings → Developer settings → Personal access tokens (`github.com/settings/tokens`).

| Token type | Permission needed |
|---|---|
| **Fine-grained** (recommended) | **Gists: Read and write** |
| Classic | `gist` scope |

> [!warning] Treat the token like a password
> Never put it in a note, a README, a Gist, a Git repository, or send it to anyone.

## 2. Plugin Setup

**Obsidian → Settings → Community plugins → Share as Gist** → paste the token into **Personal access token**.

Recommended settings:

| Setting | Value | Why |
|---|---|---|
| Enable updating Gists after creation | **ON** | Lets the plugin update Gists it already created |
| Enable auto-saving Gists after edit | **ON** | Edit a linked note → the Gist updates automatically |
| Include front matter in gists | **OFF** | Don't upload the properties. The local `gists` property stays |
| Enable auto-save notice | ON / OFF | Shows a toast on each auto-save; turn off if noisy |
| Include table of contents | **OFF** | No auto-generated TOC |

## 3. Share a Note

1. Open the note
2. `Ctrl + P` → type `gist`
3. Choose **Share as public gist on GitHub.com** or **Share as secret gist on GitHub.com**

On success the note gets a `gists:` property with the Gist `id` and `url`; that means the Gist is created **and** linked.

> [!warning] Secret Gist is not private
> Secret = not listed publicly, but **anyone with the URL can read it**. Truly sensitive content belongs in a **private GitHub repository**.

## 4. Sync & Verify

- Edit the note and save: the Gist updates automatically (with auto-saving ON)
- Verify: open the Gist page and refresh with `Ctrl + R`
- Manual sync: `Ctrl + P` → `gist` → run the **Update / Save Gist** command

## 5. Troubleshooting

| Problem | Check |
|---|---|
| Token doesn't work | Expired? Permission correct (fine-grained: **Gists → Read and write**; classic: `gist`)? |
| Edits don't update the Gist | Both **Enable updating Gists after creation** and **Enable auto-saving Gists after edit** are ON, and the note still has the `gists` property |
| Gist page looks unchanged | Refresh with `Ctrl + R`; if still old, run **Update / Save Gist** manually |
| Deleted the `gists` property | The plugin can't find the Gist any more; run **Share as Gist** again (this may create a new Gist) |

## 6. How I Use It

- **Obsidian = local knowledge base.** **Gist = online sharing page with version history.** A Gist is a Git repo, so you can see every revision and diff.
- Share only the notes you want to publish. Don't auto-publish the whole vault.
- **A Gist is not a backup.** Back up the whole vault with a Git repository; use Gists to share single notes.
- Use English file names, so Gist pages and Raw URLs are easier to use (e.g. `ubuntu-install-tools.md`, `adb-wifi.md`).

## 7. References

- GitHub Gists docs: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists
- Creating Gists: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists
- Gists REST API: https://docs.github.com/en/rest/gists/gists

---

> [!success] One-line summary
> Token (**Gists: Read and write**) → both switches **ON** → **Share as Gist** once → every later edit syncs automatically.
