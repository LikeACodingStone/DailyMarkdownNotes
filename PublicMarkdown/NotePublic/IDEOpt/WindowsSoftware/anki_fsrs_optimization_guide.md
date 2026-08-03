# Comprehensive Guide: Optimizing Anki FSRS Settings for Daily Review Reduction

This guide provides a step-by-step procedure to enable and configure the **Free Spaced Repetition Scheduler (FSRS)** in Anki. Following these settings will significantly optimize your flashcard review intervals and reduce your daily review workload by **20%–30%** without compromising overall long-term retention.

---

## 1. Accessing Deck Options

1. Open **Anki**.
2. On the main deck screen, locate the deck (or subdeck) you are currently studying.
3. Click the **gear icon (⚙️)** on the far-right side of the deck name.
4. Select **Options** from the dropdown menu.

> **Tip:** If you want these settings to apply across all decks, select your primary profile preset under the **Preset** dropdown at the top of the settings page.

---

## 2. Enabling and Configuring FSRS

Scroll down to the bottom of the Options page until you reach the **FSRS** section.

### Step 1: Enable FSRS
* Locate the **FSRS** toggle switch at the top of the section.
* **Action:** Ensure the toggle switch is turned **ON** (highlighted in blue).

### Step 2: Adjust Desired Retention
* Locate the **Desired retention** input box (default is usually `90%`).
* **Recommended Setting:** **`85%`** (or `0.85`).
* **Why change this:** 
  * A 90%+ retention target creates an exponential increase in daily review load.
  * Dropping the target to **85%** substantially increases card review intervals, cutting daily review counts by roughly 20%–30% while retaining nearly the same level of recall performance.

### Step 3: Optimize FSRS Parameters
* Locate the blue **`Optimise`** button below the parameter list box.
* **Action:** Click **`Optimise`**.
* **What this does:** Anki analyzes your complete personal review history and computes custom weights (`FSRS parameters`) tailored specifically to your memory retention characteristics.

### Step 4: Enable Card Rescheduling
* Locate **Reschedule cards on change**.
* **Action:** Turn this switch **ON** (highlighted in blue).
* **Why change this:** 
  * **ON (Recommended):** Immediately recalculates and redistributes all due dates for existing cards using the updated FSRS algorithm. This provides an immediate reduction in backlog and daily review volume.
  * **OFF:** New intervals apply only as cards are reviewed over time, taking much longer to relieve daily pressure.

---

## 3. Summary of Final Configuration

| Setting Option | Target Value / State | Action Required |
| :--- | :--- | :--- |
| **FSRS Toggle** | `Enabled` | Switch **ON** |
| **Desired retention** | `85%` | Change text input to `85%` |
| **FSRS parameters** | *Auto-generated* | Click **`Optimise`** |
| **Reschedule cards on change** | `Enabled` | Switch **ON** |

---

## 4. Post-Configuration Best Practices

To maintain a healthy review count and maximize FSRS performance:

1. **Click `Save`:** Ensure you click **Save** at the bottom/top of the screen to apply all changes.
2. **Review Button Usage:**
   * **Good (Pass):** Press **Good** if you can recall the core meaning or main definition without excessive effort. Avoid being an over-strict perfectionist.
   * **Again (Fail):** Use **Again** only when you completely fail to recognize or recall the card.
   * **Avoid Ease Hell:** FSRS accounts for button choices accurately, but overusing **Again** on manageable cards will artificially inflate your daily load.
3. **Handling Leech Cards:** If specific cards constantly reappear and trigger frequent fails, consider suspending them (`Ctrl + J` / `Cmd + J`) to rebuild or modify them with better context or visuals later.
