---
tags: [windows, account, permission, remote-desktop]
updated: 2026-11-04
---
# Windows Accounts & Permissions

> [!summary] Contents
> 1. Create a local user
> 2. Give a domain account admin rights
> 3. Shared folder password expired
> 4. Enable Remote Desktop

> [!tip] Two key tools (`Win + R`)
> - `lusrmgr.msc`: Local Users and Groups (Pro / Enterprise only)
> - `netplwiz`: User Accounts, can add domain accounts

---

## 1. Create a Local User

**Settings → Accounts → Family & other users → Add someone else to this PC**

Then choose: *I don't have this person's sign-in information* → *Add a user without a Microsoft account* → enter name & password.

> [!example]- Screenshots (Win10)
> 1. Settings → Accounts
> ![image](_resources/98950345bd53697f3364b13d81a8e123.png)
> ![image](_resources/736a92066cc6380df87e5a561cea0a51.png)
> 2. Family & other users → Add someone else to this PC
> ![image](_resources/8435418ab056fac7689043cf67e29f4f.png)
> 3. No sign-in information
> ![image](_resources/29941288d7f4b1ac6ca56b4c2f4f6f3c.png)
> 4. Without Microsoft account
> ![image](_resources/6136e04dd4107b832ae9f00fdfda8e9a.png)
> 5. Enter name & password
> ![image](_resources/ead49068754fc40ee3cd5093399e8ef4.png)

---

## 2. Give a Domain Account Admin Rights

1. Run `C:\Windows\System32\Netplwiz.exe`
2. **Add** → enter the domain account (e.g. `DOMAIN\username`)
3. Set the group to **Administrators**

---

## 3. Shared Folder Password Expired

> [!warning] Symptom → cause
> Shared folder suddenly asks for a password / access denied → the **share account's password expired** (Windows expires passwords by default).

1. `Win + R` → `lusrmgr.msc`
2. **Users** → right-click the share account → **Properties**
3. ☐ Uncheck **User must change password at next logon**
4. ☑ Check **Password never expires**

![image](_resources/d73d93a5ea07cb1a0018625026dcdd24.png)

---

## 4. Enable Remote Desktop

1. **This PC → Properties → Remote settings** → enable **Allow remote connections to this computer**
2. `lusrmgr.msc` → set a user and password for remote login
3. Connect with that user via `mstsc`

> [!note] The account must have a password
> Remote Desktop refuses accounts with an empty password.
